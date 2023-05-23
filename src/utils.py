import os
import random
from datetime import timedelta

import numpy as np
import torch
import torchvision
from hydra.utils import get_original_cwd
from omegaconf import OmegaConf
import matplotlib.pyplot as plt
import matplotlib.colors as pltColors

from src import ff_mnist, ff_model

#not sure what this does, seems to setting the seed used in the config.yaml also for the numpy,torch and random
def parse_args(opt):
    np.random.seed(opt.seed)
    torch.manual_seed(opt.seed)
    random.seed(opt.seed)

    #basically prints the optimized in yaml format
    #if there are no modifications it prints the exact config.yaml
    print(OmegaConf.to_yaml(opt))
    return opt


def get_model_and_optimizer(opt):
    #get the model from the optimizer
    model = ff_model.FF_model(opt)

    #if possible put it in cuda
    if "cuda" in opt.device:
        model = model.cuda()
    #print(model, "\n")

    # Create optimizer with different hyper-parameters for the main model
    # and the downstream classification model.
    main_model_params = [
        p
        for p in model.parameters()
        if all(p is not x for x in model.linear_classifier.parameters())
    ]
    optimizer = torch.optim.SGD(
        [
            {
                "params": main_model_params,
                "lr": opt.training.learning_rate,
                "weight_decay": opt.training.weight_decay,
                "momentum": opt.training.momentum,
            },
            {
                "params": model.linear_classifier.parameters(),
                "lr": opt.training.downstream_learning_rate,
                "weight_decay": opt.training.downstream_weight_decay,
                "momentum": opt.training.momentum,
            },
        ]
    )
    #print(optimizer, "\n")
    return model, optimizer


def get_data(opt, partition):
    dataset = ff_mnist.FF_MNIST(opt, partition)

    # Improve reproducibility in dataloader.
    g = torch.Generator()
    g.manual_seed(opt.seed)

    return torch.utils.data.DataLoader(
        dataset,
        batch_size=opt.input.batch_size,
        drop_last=True,
        shuffle=True,
        worker_init_fn=seed_worker,
        generator=g,
        num_workers=4,
        persistent_workers=True,
    )


def seed_worker(worker_id):
    worker_seed = torch.initial_seed() % 2 ** 32
    np.random.seed(worker_seed)
    random.seed(worker_seed)


def get_MNIST_partition(opt, partition):
    #check if we want to get data for training/evaluation/both
    if partition in ["train", "val", "train_val"]:
        mnist = torchvision.datasets.MNIST(
            os.path.join(get_original_cwd(), opt.input.path),
            train=True,
            download=True,
            transform=torchvision.transforms.ToTensor(),
        )
    #else we are just testing and there is no need for train flag
    elif partition in ["test"]:
        mnist = torchvision.datasets.MNIST(
            os.path.join(get_original_cwd(), opt.input.path),
            train=False,
            download=True,
            transform=torchvision.transforms.ToTensor(),
        )
    else:
        raise NotImplementedError

    if partition == "train":
        mnist = torch.utils.data.Subset(mnist, range(50000))
    elif partition == "val":
        #not sure why this is done again rather than just taking the subset for evaluation
        mnist = torchvision.datasets.MNIST(
            os.path.join(get_original_cwd(), opt.input.path),
            train=True,
            download=True,
            transform=torchvision.transforms.ToTensor(),
        )
        mnist = torch.utils.data.Subset(mnist, range(50000, 60000))

    return mnist


def dict_to_cuda(dict):
    for key, value in dict.items():
        dict[key] = value.cuda(non_blocking=True)
    return dict


def preprocess_inputs(opt, inputs, labels):
    if "cuda" in opt.device:
        inputs = dict_to_cuda(inputs)
        labels = dict_to_cuda(labels)
    return inputs, labels


def get_linear_cooldown_lr(opt, epoch, lr):
    if epoch > (opt.training.epochs // 2):
        return lr * 2 * (1 + opt.training.epochs - epoch) / opt.training.epochs
    else:
        return lr


def update_learning_rate(optimizer, opt, epoch):
    optimizer.param_groups[0]["lr"] = get_linear_cooldown_lr(
        opt, epoch, opt.training.learning_rate
    )
    optimizer.param_groups[1]["lr"] = get_linear_cooldown_lr(
        opt, epoch, opt.training.downstream_learning_rate
    )
    return optimizer


def get_accuracy(opt, output, target):
    """Computes the accuracy."""
    with torch.no_grad():
        prediction = torch.argmax(output, dim=1)
        return (prediction == target).sum() / opt.input.batch_size


def print_results(partition, iteration_time, scalar_outputs, epoch=None):
    if epoch is not None:
        print(f"Epoch {epoch} \t", end="")

    print(
        f"{partition} \t"
        f"Time: {timedelta(seconds=iteration_time)} \t",
        end="",
    )
    if scalar_outputs is not None:
        for key, value in scalar_outputs.items():
            print(f"{key}: {value:.4f} \t", end="")
    print("\n")


def log_results(result_dict, scalar_outputs, num_steps):
    for key, value in scalar_outputs.items():
        if isinstance(value, float):
            result_dict[key] += value / num_steps
        else:
            result_dict[key] += value.item() / num_steps
    return result_dict

def plot(data, labels, batchsize, layer, batch, epoch, norm, classifier, oldData=False):
    myLabels = labels['class_labels']
    #myLabels = myLabels.cpu()
    myLabels = myLabels.cpu().numpy()
    #data = data.detach().numpy()
    runType = 'backprop'

    plt.figure(figsize=(8,6))
    plot = plt.scatter(data[:batchsize][:,0], data[:batchsize][:,1], c=myLabels)
    plt.legend(handles=plot.legend_elements()[0], labels=list(set(myLabels)), loc=(1.02,0))
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.title("First two principal components after scaling")
    if(oldData):
        #plot = plt.scatter(data[:batchsize][:,2], data[:batchsize][:,3], c=myLabels)
        #plt.legend(handles=plot.legend_elements()[0], labels=list(set(myLabels)), loc=(1.02,0))
        if(not classifier):
            if(not norm):
                plt.savefig(f"./images/{runType}Test/PCA/epoch{epoch}/{batch}/{layer}.png") 
            elif norm:
                plt.savefig(f"./images/{runType}Test/normalizedPCA/epoch{epoch}/{batch}/{layer}.png")
        else:
            if(not norm):
                plt.savefig(f"./images/{runType}Test/PCA/epoch{epoch}/{batch}/classifier/{layer}.png") 
            elif norm:
                plt.savefig(f"./images/{runType}Test/normalizedPCA/epoch{epoch}/{batch}/classifier/{layer}.png")
    else:
        #plot = plt.scatter(data[:batchsize][:,0], data[:batchsize][:,1], c=myLabels)
        #plt.legend(handles=plot.legend_elements()[0], labels=list(set(myLabels)), loc=(1.02,0))
        if(not classifier):
            if(not norm):
                plt.savefig(f"./images/{runType}/PCA/epoch{epoch}/{batch}/{layer}.png") 
            elif norm:
                plt.savefig(f"./images/{runType}/normalizedPCA/epoch{epoch}/{batch}/{layer}.png")
        else:
            if(not norm):
                plt.savefig(f"./images/{runType}/PCA/epoch{epoch}/{batch}/classifier/{layer}.png") 
            elif norm:
                plt.savefig(f"./images/{runType}/normalizedPCA/epoch{epoch}/{batch}/classifier/{layer}.png")


    plt.close()
    #plt.show()

    return
