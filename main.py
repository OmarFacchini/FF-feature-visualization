import time
from collections import defaultdict

import hydra
import torch
from omegaconf import DictConfig
import omegaconf
import pynvml as nvm


from src import utils

import wandb


def train(opt, model, optimizer):
    start_time = time.time()
    train_loader = utils.get_data(opt, "train")
    num_steps_per_epoch = len(train_loader)

    for epoch in range(opt.training.epochs):
        #sets the non-existing keys of the dictionary to default to float to avoid errors for missing values
        train_results = defaultdict(float)
        optimizer = utils.update_learning_rate(optimizer, opt, epoch)
        batch = 0

        for inputs, labels in train_loader:
            inputs, labels = utils.preprocess_inputs(opt, inputs, labels)

            optimizer.zero_grad()

            scalar_outputs = model(inputs, labels, batch, epoch)
            
            #print(f"did the forward {batch}")
            #calculates derivative of loss
            scalar_outputs["Loss"].backward()
            #print(f"did the backprop {batch}")

            optimizer.step()

            train_results = utils.log_results(
                train_results, scalar_outputs, num_steps_per_epoch
            )

            batch += 1

        utils.print_results("train", time.time() - start_time, train_results, epoch)


        #adding log of the important data on wandb
        #if not backpropagation store every layer value
        #if backpropagation is active store only classification values
        if(not opt.backprop):
            wandb.log({ 'epoch': epoch,
                        'loss_layer_0': scalar_outputs[f"loss_layer_0"],
                        'loss_layer_1': scalar_outputs[f"loss_layer_1"],
                        'loss_layer_2': scalar_outputs[f"loss_layer_2"],
                        'accuracy_layer_0': scalar_outputs[f"ff_accuracy_layer_0"] ,
                        'accuracy_layer_1': scalar_outputs[f"ff_accuracy_layer_1"] ,
                        'accuracy_layer_2': scalar_outputs[f"ff_accuracy_layer_2"] ,
                        'peer norm': scalar_outputs["Peer Normalization"],
                        'train_classification_accuracy': scalar_outputs["classification_accuracy"],
                        'train_classification_loss': scalar_outputs["classification_loss"],
                        'train_total_loss': scalar_outputs["Loss"]})
        else:
             wandb.log({'epoch': epoch,
                        'train_classification_accuracy': scalar_outputs["classification_accuracy"],
                        'train_classification_loss': scalar_outputs["classification_loss"]})
        
        start_time = time.time()

        

        # Validate.
        if epoch % opt.training.val_idx == 0 and opt.training.val_idx != -1:
            validate_or_test(opt, model, "val", epoch=epoch)

    return model



def validate_or_test(opt, model, partition, epoch=None):
    test_time = time.time()
    test_results = defaultdict(float)

    data_loader = utils.get_data(opt, partition)
    num_steps_per_epoch = len(data_loader)

    model.eval()
    print(partition)
    with torch.no_grad():
        for inputs, labels in data_loader:
            inputs, labels = utils.preprocess_inputs(opt, inputs, labels)

            scalar_outputs = model.forward_downstream_classification_model(
                inputs, labels
            )
            test_results = utils.log_results(
                test_results, scalar_outputs, num_steps_per_epoch
            )

    utils.print_results(partition, time.time() - test_time, test_results, epoch=epoch)

    wandb.log({'epoch': epoch,
               'eval_classification_accuracy': scalar_outputs["classification_accuracy"],
               'eval_classification_loss': scalar_outputs["classification_loss"]})
    
    #set the model in train mode again
    model.train()


@hydra.main(config_path=".", config_name="config", version_base=None)
def my_main(opt: DictConfig) -> None:
    opt = utils.parse_args(opt)
    model, optimizer = utils.get_model_and_optimizer(opt)
    trainable_params = 0
    total_params = 0

    for param in model.parameters():
        if param.requires_grad:
            trainable_params += param.numel()
        total_params += param.numel()
    print(f"trainable params: {trainable_params},\ntotal params: {total_params}")
    #total_params = sum(p.numel() for p in model.parameters())
    #print(f"total params: {total_params}")

    #print(f"device name: {torch.cuda.get_device_name()}\nallocated memory: {round(torch.cuda.memory_allocated()/1024**3,2)} GB\nmax memory: {torch.cuda.memory_usage()}")
    #print(torch.cuda.memory_usage())
    '''nvm.nvmlInit()
    #will put this in train() after every epoch probably
    deviceCount = nvm.nvmlDeviceGetCount()
    for i in range(deviceCount):
        handle = nvm.nvmlDeviceGetHandleByIndex(i)
        info = nvm.nvmlDeviceGetMemoryInfo(handle)
        print("Device", i, ":", nvm.nvmlDeviceGetName(handle), "total memory:", info.total/1024**3, "GB ","free memory:", info.free/1024**3, "GB ","used memory:", info.used/1024**3, "GB ", "load:", (info.used/info.total)*100)
    
    nvm.nvmlShutdown()'''
    #model = train(opt, model, optimizer)
    #return
    wandb_config = omegaconf.OmegaConf.to_container(
        opt, resolve=True, throw_on_missing=True
    )

    wandb_logger = wandb.init(
        project="forward forward comparison",
        name=opt.run_name,
        config=wandb_config
    )


    #pynvml.nvmlUnitGetHandleByIndex()
    model = train(opt, model, optimizer)
    validate_or_test(opt, model, "val")




    '''if opt.training.final_test:
        validate_or_test(opt, model, "test")
    '''

if __name__ == "__main__":
    my_main()
