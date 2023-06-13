# <center>**FF compared to backpropagation**</center>
Here are compared the results obtained with the two different approaches to better understand if the Forward Froward approach would be a viable option compared to standard systems.<br>

Since the best results were obtained using TSNE, the images displayed here will be the ones obtained using that approach.

## <center>**Normalized TSNE**</center>
Here the layer has been normalized before plotting using TSNE.

### **Hidden layer dimension 256**
| layer | FF or backprop | epoch0 | epoch60 | epoch99 |
|:-----:|:--------------:|:------:|:-------:|:-------:|
|  0    | backprop | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch60/0/classifier/0.png) | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch99/0/classifier/0.png) |
|  0    | FF | ![](/results/hdim256/images/FF/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/FF/normalizedTSNE/epoch60/0/classifier/0.png) | ![](/results/hdim256/images/FF/normalizedTSNE/epoch99/0/classifier/0.png) |
|  1    | backprop | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch60/0/classifier/1.png) | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch99/0/classifier/1.png) |
|  1    | FF | ![](/results/hdim256/images/FF/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/FF/normalizedTSNE/epoch60/0/classifier/1.png) | ![](/results/hdim256/images/FF/normalizedTSNE/epoch99/0/classifier/1.png) |
|  2    | backprop | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch60/0/classifier/2.png) | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch99/0/classifier/2.png) |
|  2    | FF | ![](/results/hdim256/images/FF/normalizedTSNE/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/FF/normalizedTSNE/epoch60/0/classifier/2.png) | ![](/results/hdim256/images/FF/normalizedTSNE/epoch99/0/classifier/2.png) |



### **Hidden layer dimension 512**
| layer | FF or backprop | epoch0 | epoch60 | epoch99 |
|:-----:|:--------------:|:------:|:-------:|:-------:|
|  0    | backprop | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch60/0/classifier/0.png) | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch99/0/classifier/0.png) |
|  0    | FF | ![](/results/hdim512/images/FF/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/FF/normalizedTSNE/epoch60/0/classifier/0.png) | ![](/results/hdim512/images/FF/normalizedTSNE/epoch99/0/classifier/0.png) |
|  1    | backprop | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch60/0/classifier/1.png) | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch99/0/classifier/1.png) |
|  1    | FF | ![](/results/hdim512/images/FF/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/FF/normalizedTSNE/epoch60/0/classifier/1.png) | ![](/results/hdim512/images/FF/normalizedTSNE/epoch99/0/classifier/1.png) |
|  2    | backprop | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch60/0/classifier/2.png) | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch99/0/classifier/2.png) |
|  2    | FF | ![](/results/hdim512/images/FF/normalizedTSNE/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/FF/normalizedTSNE/epoch60/0/classifier/2.png) | ![](/results/hdim512/images/FF/normalizedTSNE/epoch99/0/classifier/2.png) |


### **Hidden layer dimension 1000**
| layer | FF or backprop | epoch0 | epoch60 | epoch99 |
|:-----:|:--------------:|:------:|:-------:|:-------:|
|  0    | backprop | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch60/0/classifier/0.png) | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch99/0/classifier/0.png) |
|  0    | FF | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch60/0/classifier/0.png) | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch99/0/classifier/0.png) |
|  1    | backprop | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch60/0/classifier/1.png) | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch99/0/classifier/1.png) |
|  1    | FF | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch60/0/classifier/1.png) | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch99/0/classifier/1.png) |
|  2    | backprop | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch60/0/classifier/2.png) | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch99/0/classifier/2.png) |
|  2    | FF | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch60/0/classifier/2.png) | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch99/0/classifier/2.png) |


## <center>**Standard TSNE**</center>
Here the layer has been left untouched before plotting using TSNE.

### **Hidden layer dimension 256**
| layer | FF or backprop | epoch0 | epoch60 | epoch99 |
|:-----:|:--------------:|:------:|:-------:|:-------:|
|  0    | backprop | ![](/results/hdim256/images/backprop/TSNE/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/backprop/TSNE/epoch60/0/classifier/0.png) | ![](/results/hdim256/images/backprop/TSNE/epoch99/0/classifier/0.png) |
|  0    | FF | ![](/results/hdim256/images/FF/TSNE/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/FF/TSNE/epoch60/0/classifier/0.png) | ![](/results/hdim256/images/FF/TSNE/epoch99/0/classifier/0.png) |
|  1    | backprop | ![](/results/hdim256/images/backprop/TSNE/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/backprop/TSNE/epoch60/0/classifier/1.png) | ![](/results/hdim256/images/backprop/TSNE/epoch99/0/classifier/1.png) |
|  1    | FF | ![](/results/hdim256/images/FF/TSNE/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/FF/TSNE/epoch60/0/classifier/1.png) | ![](/results/hdim256/images/FF/TSNE/epoch99/0/classifier/1.png) |
|  2    | backprop | ![](/results/hdim256/images/backprop/TSNE/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/backprop/TSNE/epoch60/0/classifier/2.png) | ![](/results/hdim256/images/backprop/TSNE/epoch99/0/classifier/2.png) |
|  2    | FF | ![](/results/hdim256/images/FF/TSNE/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/FF/TSNE/epoch60/0/classifier/2.png) | ![](/results/hdim256/images/FF/TSNE/epoch99/0/classifier/2.png) |


### **Hidden layer dimension 512**
| layer | FF or backprop | epoch0 | epoch60 | epoch99 |
|:-----:|:--------------:|:------:|:-------:|:-------:|
|  0    | backprop | ![](/results/hdim512/images/backprop/TSNE/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/backprop/TSNE/epoch60/0/classifier/0.png) | ![](/results/hdim512/images/backprop/TSNE/epoch99/0/classifier/0.png) |
|  0    | FF | ![](/results/hdim512/images/FF/TSNE/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/FF/TSNE/epoch60/0/classifier/0.png) | ![](/results/hdim512/images/FF/TSNE/epoch99/0/classifier/0.png) |
|  1    | backprop | ![](/results/hdim512/images/backprop/TSNE/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/backprop/TSNE/epoch60/0/classifier/1.png) | ![](/results/hdim512/images/backprop/TSNE/epoch99/0/classifier/1.png) |
|  1    | FF | ![](/results/hdim512/images/FF/TSNE/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/FF/TSNE/epoch60/0/classifier/1.png) | ![](/results/hdim512/images/FF/TSNE/epoch99/0/classifier/1.png) |
|  2    | backprop | ![](/results/hdim512/images/backprop/TSNE/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/backprop/TSNE/epoch60/0/classifier/2.png) | ![](/results/hdim512/images/backprop/TSNE/epoch99/0/classifier/2.png) |
|  2    | FF | ![](/results/hdim512/images/FF/TSNE/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/FF/TSNE/epoch60/0/classifier/2.png) | ![](/results/hdim512/images/FF/TSNE/epoch99/0/classifier/2.png) |

### **Hidden layer dimension 1000**
| layer | FF or backprop | epoch0 | epoch60 | epoch99 |
|:-----:|:--------------:|:------:|:-------:|:-------:|
|  0    | backprop | ![](/results/hdim1000/images/backprop/TSNE/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/backprop/TSNE/epoch60/0/classifier/0.png) | ![](/results/hdim1000/images/backprop/TSNE/epoch99/0/classifier/0.png) |
|  0    | FF | ![](/results/hdim1000/images/FF/TSNE/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/FF/TSNE/epoch60/0/classifier/0.png) | ![](/results/hdim1000/images/FF/TSNE/epoch99/0/classifier/0.png) |
|  1    | backprop | ![](/results/hdim1000/images/backprop/TSNE/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/backprop/TSNE/epoch60/0/classifier/1.png) | ![](/results/hdim1000/images/backprop/TSNE/epoch99/0/classifier/1.png) |
|  1    | FF | ![](/results/hdim1000/images/FF/TSNE/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/FF/TSNE/epoch60/0/classifier/1.png) | ![](/results/hdim1000/images/FF/TSNE/epoch99/0/classifier/1.png) |
|  2    | backprop | ![](/results/hdim1000/images/backprop/TSNE/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/backprop/TSNE/epoch60/0/classifier/2.png) | ![](/results/hdim1000/images/backprop/TSNE/epoch99/0/classifier/2.png) |
|  2    | FF | ![](/results/hdim1000/images/FF/TSNE/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/FF/TSNE/epoch60/0/classifier/2.png) | ![](/results/hdim1000/images/FF/TSNE/epoch99/0/classifier/2.png) |


## <center>**Classifier with TSNE**</center>

### **Hidden layer dimension 256**
|FF or backprop | epoch0 | epoch60 | epoch99 |
|:--------------:|:------:|:-------:|:-------:|
|backprop | ![](/results/hdim256/images/backprop/TSNE/epoch0/0/actualClassifier/2.png) | ![](/results/hdim256/images/backprop/TSNE/epoch60/0/actualClassifier/2.png) | ![](/results/hdim256/images/backprop/TSNE/epoch99/0/actualClassifier/2.png) |
|FF | ![](/results/hdim256/images/FF/TSNE/epoch0/0/actualClassifier/2.png) | ![](/results/hdim256/images/FF/TSNE/epoch60/0/actualClassifier/2.png) | ![](/results/hdim256/images/FF/TSNE/epoch99/0/actualClassifier/2.png) |


### **Hidden layer dimension 512**
|FF or backprop | epoch0 | epoch60 | epoch99 |
|:--------------:|:------:|:-------:|:-------:|
|backprop | ![](/results/hdim512/images/backprop/TSNE/epoch0/0/actualClassifier/2.png) | ![](/results/hdim512/images/backprop/TSNE/epoch60/0/actualClassifier/2.png) | ![](/results/hdim512/images/backprop/TSNE/epoch99/0/actualClassifier/2.png) |
|FF | ![](/results/hdim512/images/FF/TSNE/epoch0/0/actualClassifier/2.png) | ![](/results/hdim512/images/FF/TSNE/epoch60/0/actualClassifier/2.png) | ![](/results/hdim512/images/FF/TSNE/epoch99/0/actualClassifier/2.png) |


### **Hidden layer dimension 1000**
|FF or backprop | epoch0 | epoch60 | epoch99 |
|:--------------:|:------:|:-------:|:-------:|
|backprop | ![](/results/hdim1000/images/backprop/TSNE/epoch0/0/actualClassifier/2.png) | ![](/results/hdim1000/images/backprop/TSNE/epoch60/0/actualClassifier/2.png) | ![](/results/hdim1000/images/backprop/TSNE/epoch99/0/actualClassifier/2.png) |
|FF | ![](/results/hdim1000/images/FF/TSNE/epoch0/0/actualClassifier/2.png) | ![](/results/hdim1000/images/FF/TSNE/epoch60/0/actualClassifier/2.png) | ![](/results/hdim1000/images/FF/TSNE/epoch99/0/actualClassifier/2.png) |
