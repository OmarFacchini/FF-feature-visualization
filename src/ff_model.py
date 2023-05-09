import math

import torch
import torch.nn as nn

from sklearn.decomposition import PCA
from src import utils
import numpy as np



class FF_model(torch.nn.Module):
    """The model trained with Forward-Forward (FF)."""

    def __init__(self, opt):
        super(FF_model, self).__init__()


        self.pca = PCA(n_components=2)
        self.opt = opt
        self.num_channels = [self.opt.model.hidden_dim] * self.opt.model.num_layers
        self.act_fn = ReLU_full_grad()

        # Initialize the model.
        self.model = nn.ModuleList([nn.Linear(784, self.num_channels[0])])
        for i in range(1, len(self.num_channels)):
            self.model.append(nn.Linear(self.num_channels[i - 1], self.num_channels[i]))

        # Initialize forward-forward loss.
        self.ff_loss = nn.BCEWithLogitsLoss()

        # Initialize peer normalization loss.
        self.running_means = [
            torch.zeros(self.num_channels[i], device=self.opt.device) + 0.5
            for i in range(self.opt.model.num_layers)
        ]

        # Initialize downstream classification loss.
        channels_for_classification_loss = sum(
            self.num_channels[-i] for i in range(self.opt.model.num_layers - 1)
        )
        if(not self.opt.backprop):
            self.linear_classifier = nn.Sequential(
                # using mnmist we get 10 classes (numbers from 0 to 9)
                nn.Linear(channels_for_classification_loss, 10, bias=False)
            )
        else:
            self.linear_classifier = nn.Sequential(
                # using mnmist we get 10 classes (numbers from 0 to 9)
                nn.Linear(self.num_channels[-1], 10, bias=False)
            )
        self.classification_loss = nn.CrossEntropyLoss()

        # Initialize weights.
        self._init_weights()

    def _init_weights(self):
        for m in self.model.modules():
            if isinstance(m, nn.Linear):
                torch.nn.init.normal_(
                    m.weight, mean=0, std=1 / math.sqrt(m.weight.shape[0])
                )
                torch.nn.init.zeros_(m.bias)

        for m in self.linear_classifier.modules():
            if isinstance(m, nn.Linear):
                nn.init.zeros_(m.weight)

    def _layer_norm(self, z, eps=1e-8):
        return z / (torch.sqrt(torch.mean(z ** 2, dim=-1, keepdim=True)) + eps)

    def _calc_peer_normalization_loss(self, idx, z):
        # Only calculate mean activity over positive samples.
        mean_activity = torch.mean(z[:self.opt.input.batch_size], dim=0)
        #print(z[self.opt.input.batch_size:])

        if(not self.opt.backprop):
            self.running_means[idx] = self.running_means[
                idx
            ].detach() * self.opt.model.momentum + mean_activity * (
                1 - self.opt.model.momentum
            )
        else:
            self.running_means[idx] = self.running_means[idx] * self.opt.model.momentum + mean_activity * (1 - self.opt.model.momentum)

        peer_loss = (torch.mean(self.running_means[idx]) - self.running_means[idx]) ** 2
        return torch.mean(peer_loss)

    def _calc_ff_loss(self, z, labels):
        sum_of_squares = torch.sum(z ** 2, dim=-1)

        logits = sum_of_squares - z.shape[1]
        ff_loss = self.ff_loss(logits, labels.float())

        with torch.no_grad():
            ff_accuracy = (
                torch.sum((torch.sigmoid(logits) > 0.5) == labels)
                / z.shape[0]
            ).item()
        return ff_loss, ff_accuracy

    def forward(self, inputs, labels, batch, epoch):
        #save a bit of memory in case we have backprop as we only store the loss
        if(not self.opt.backprop):
            scalar_outputs = {
                "Loss": torch.zeros(1, device=self.opt.device),
                "Peer Normalization": torch.zeros(1, device=self.opt.device),
            }
        else:
            scalar_outputs = {
                "Loss": torch.zeros(1, device=self.opt.device)
            }


        # Concatenate positive and negative samples and create corresponding labels.
        #batch, channel, width, height
        # z.size() is a tensor [200,1,28,28]
        # z[0].size() is the array of array 28*28 (equal 784 which is input of first layer)
        # correct as we concat two tensors(pos and neg) of size 100(batch)
        #z.shape[0] is batch
        z = torch.cat([inputs["pos_images"], inputs["neg_images"]], dim=0)
        posneg_labels = torch.zeros(z.shape[0], device=self.opt.device)
        posneg_labels[: self.opt.input.batch_size] = 1


        #tensor of size 200 filled with 1s for the first half and 0 in the rest
        #print(posneg_labels)
 
        #reshape z to have a single concat array rather than having an array of array, get a tensor [200,784]
        z = z.reshape(z.shape[0], -1)


        #normalize the layer, does nothing to shape, just normalizes values
        z = self._layer_norm(z)



        # there are 3 layers with size 1000
        for idx, layer in enumerate(self.model):
            #z.shape is tensor [200, 1000], values are init when generating the model
            z = layer(z)

            #pca actuator
            with torch.no_grad():
                myArray = z.detach().cpu().numpy()
                self.pca.fit_transform(myArray)

                #plot every 20 epochs and every 100 batches
                #basically get total check on 5 epochs and 5 batches per epoch
                if( ((epoch % 20) == 0 or epoch == self.opt.training.epochs - 1) and (batch % 100) == 0):
                    utils.plot(myArray, labels, self.opt.input.batch_size, idx, batch, epoch, norm=False, classifier=False)


            #apply activation function, removing negative values and setting them to 0
            z = self.act_fn.apply(z)

            #if no backpropagation calculate peer norm and loss/accuracy for each layer
            #if backprop we do nothing as we only calculate the loss/accuracy on the classification layer
            if(not self.opt.backprop):
                if self.opt.model.peer_normalization > 0:
                    peer_loss = self._calc_peer_normalization_loss(idx, z)
                    scalar_outputs["Peer Normalization"] += peer_loss
                    scalar_outputs["Loss"] += self.opt.model.peer_normalization * peer_loss

                ff_loss, ff_accuracy = self._calc_ff_loss(z, posneg_labels)
                scalar_outputs[f"loss_layer_{idx}"] = ff_loss
                scalar_outputs[f"ff_accuracy_layer_{idx}"] = ff_accuracy
                scalar_outputs["Loss"] += ff_loss

            #if no backprop stop chain rule
            if(not self.opt.backprop):
                z = z.detach()

            #normalize layer
            z = self._layer_norm(z)

            #pca actuator
            with torch.no_grad():
                myArray = z.detach().cpu().numpy()
                self.pca.fit_transform(myArray)

                #plot every 20 epochs and every 100 batches
                #basically get total check on 5 epochs and 5 batches per epoch
                if( ((epoch % 20) == 0 or epoch == self.opt.training.epochs - 1) and (batch % 100) == 0):
                    utils.plot(myArray, labels, self.opt.input.batch_size, idx, batch, epoch, norm=True, classifier=False)
            

        #classify
        scalar_outputs = self.forward_downstream_classification_model(
            inputs, labels, scalar_outputs=scalar_outputs, batch=batch, epoch=epoch
        )

        return scalar_outputs

    def forward_downstream_classification_model(
        self, inputs, labels, scalar_outputs=None,
        batch=-1, epoch=-1
    ):
        if scalar_outputs is None:
            scalar_outputs = {
                "Loss": torch.zeros(1, device=self.opt.device),
            }

        #z is the layer
        z = inputs["neutral_sample"]
        z = z.reshape(z.shape[0], -1)
        z = self._layer_norm(z)

        input_classification_model = []

        with torch.no_grad():
            for idx, layer in enumerate(self.model):
                z = layer(z)

                myArray = z.detach().cpu().numpy()
                self.pca.fit_transform(myArray)

                #plot every 20 epochs and every 100 batches
                #basically get total check on 5 epochs and 5 batches per epoch
                if( ((epoch % 20) == 0 or epoch == self.opt.training.epochs - 1) and (batch % 100) == 0):
                    utils.plot(myArray, labels, self.opt.input.batch_size, idx, batch, epoch, norm=False, classifier=True)

                z = self.act_fn.apply(z)
                z = self._layer_norm(z)

                myArray = z.detach().cpu().numpy()
                self.pca.fit_transform(myArray)

                #plot every 20 epochs and every 100 batches
                #basically get total check on 5 epochs and 5 batches per epoch
                if( ((epoch % 20) == 0 or epoch == self.opt.training.epochs - 1) and (batch % 100) == 0):
                    utils.plot(myArray, labels, self.opt.input.batch_size, idx, batch, epoch, norm=True, classifier=True)

                if idx >= 1:
                    input_classification_model.append(z)

        input_classification_model = torch.concat(input_classification_model, dim=-1)

        if(not self.opt.backprop):
            output = self.linear_classifier(input_classification_model.detach())
        else:
            output = self.linear_classifier(z)
        output = output - torch.max(output, dim=-1, keepdim=True)[0]
        classification_loss = self.classification_loss(output, labels["class_labels"])
        classification_accuracy = utils.get_accuracy(
            self.opt, output.data, labels["class_labels"]
        )

        scalar_outputs["Loss"] += classification_loss
        scalar_outputs["classification_loss"] = classification_loss
        scalar_outputs["classification_accuracy"] = classification_accuracy
        return scalar_outputs


class ReLU_full_grad(torch.autograd.Function):
    """ ReLU activation function that passes through the gradient irrespective of its input value. """

    @staticmethod
    def forward(ctx, input):
        return input.clamp(min=0)

    @staticmethod
    def backward(ctx, grad_output):
        return grad_output.clone()
