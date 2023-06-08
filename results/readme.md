# <center>**results obtained**</center>

Here are shown the images obtained from the various test run on both the standard backpropagation and for the Forward-Forward approach with also the application of PCA and TSNE. <br>
This was done in order to see how the features would be extracted using the different structures for the model and the different visualization in 2D.<br>
Different sized of layers were used in the structure to also see how it would vary the features.

# <center>**1. backpropagation results**</center>
In this chapter the results for the standard backpropagation approach are displayed.

## <center>**1.1 compare layer with itself in different epochs**</center>
This allows us to see the evolution of the layer itself over time.

`batch of reference:0 `
### <center>**1.1.1 Normalized TSNE**</center>
Here the layer has been normalized before plotting using TSNE.

#### **Hidden layer dimension 256**

| layer | epoch0 | epoch60  | epoch99 |
|:-----:|:------: |:-------:|:-------:|
| 0     |![](/results/hdim256/images/backprop/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch60/0/classifier/0.png) | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch99/0/classifier/0.png) |
1       | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch60/0/classifier/1.png) | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch99/0/classifier/1.png) |
2       | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch60/0/classifier/2.png) | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch99/0/classifier/2.png) |

#### **Hidden layer dimension 512**

| layer | epoch0 | epoch60  | epoch99 |
|:-----:|:------: |:-------:|:-------:|
| 0     |![](/results/hdim512/images/backprop/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch60/0/classifier/0.png) | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch99/0/classifier/0.png) |
1       | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch60/0/classifier/1.png) | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch99/0/classifier/1.png) |
2       | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch60/0/classifier/2.png) | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch99/0/classifier/2.png) |

#### **Hidden layer dimension 1000**

| layer | epoch0 | epoch60  | epoch99 |
|:-----:|:------: |:-------:|:-------:|
| 0     |![](/results/hdim1000/images/backprop/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch60/0/classifier/0.png) | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch99/0/classifier/0.png) |
1       | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch60/0/classifier/1.png) | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch99/0/classifier/1.png) |
2       | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch60/0/classifier/2.png) | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch99/0/classifier/2.png) |

-----------------------------

### <center>**1.1.2 standard TSNE**</center>
Here the layer is clean and untouched for plotting using TSNE.

#### **Hidden layer dimension 256**

| layer | epoch0 | epoch60  | epoch99 |
|:-----:|:------: |:-------:|:-------:|
| 0     |![](/results/hdim256/images/backprop/TSNE/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/backprop/TSNE/epoch60/0/classifier/0.png) | ![](/results/hdim256/images/backprop/TSNE/epoch99/0/classifier/0.png) |
1       | ![](/results/hdim256/images/backprop/TSNE/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/backprop/TSNE/epoch60/0/classifier/1.png) | ![](/results/hdim256/images/backprop/TSNE/epoch99/0/classifier/1.png) |
2       | ![](/results/hdim256/images/backprop/TSNE/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/backprop/TSNE/epoch60/0/classifier/2.png) | ![](/results/hdim256/images/backprop/TSNE/epoch99/0/classifier/2.png) |

#### **Hidden layer dimension 512**

| layer | epoch0 | epoch60  | epoch99 |
|:-----:|:------: |:-------:|:-------:|
| 0     |![](/results/hdim512/images/backprop/TSNE/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/backprop/TSNE/epoch60/0/classifier/0.png) | ![](/results/hdim512/images/backprop/TSNE/epoch99/0/classifier/0.png) |
1       | ![](/results/hdim512/images/backprop/TSNE/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/backprop/TSNE/epoch60/0/classifier/1.png) | ![](/results/hdim512/images/backprop/TSNE/epoch99/0/classifier/1.png) |
2       | ![](/results/hdim512/images/backprop/TSNE/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/backprop/TSNE/epoch60/0/classifier/2.png) | ![](/results/hdim512/images/backprop/TSNE/epoch99/0/classifier/2.png) |

#### **Hidden layer dimension 1000**

| layer | epoch0 | epoch60  | epoch99 |
|:-----:|:------: |:-------:|:-------:|
| 0     |![](/results/hdim1000/images/backprop/TSNE/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/backprop/TSNE/epoch60/0/classifier/0.png) | ![](/results/hdim1000/images/backprop/TSNE/epoch99/0/classifier/0.png) |
1       | ![](/results/hdim1000/images/backprop/TSNE/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/backprop/TSNE/epoch60/0/classifier/1.png) | ![](/results/hdim1000/images/backprop/TSNE/epoch99/0/classifier/1.png) |
2       | ![](/results/hdim1000/images/backprop/TSNE/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/backprop/TSNE/epoch60/0/classifier/2.png) | ![](/results/hdim1000/images/backprop/TSNE/epoch99/0/classifier/2.png) |

-----------------------------

### <center>**1.1.3 Normalized PCA**</center>
Here the layer has been normalized before plotting using PCA.

#### **Hidden layer dimension 256**

| layer | epoch0 | epoch60  | epoch99 |
|:-----:|:------: |:-------:|:-------:|
| 0     |![](/results/hdim256/images/backprop/normalizedPCA/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/backprop/normalizedPCA/epoch60/0/classifier/0.png) | ![](/results/hdim256/images/backprop/normalizedPCA/epoch99/0/classifier/0.png) |
1       | ![](/results/hdim256/images/backprop/normalizedPCA/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/backprop/normalizedPCA/epoch60/0/classifier/1.png) | ![](/results/hdim256/images/backprop/normalizedPCA/epoch99/0/classifier/1.png) |
2       | ![](/results/hdim256/images/backprop/normalizedPCA/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/backprop/normalizedPCA/epoch60/0/classifier/2.png) | ![](/results/hdim256/images/backprop/normalizedPCA/epoch99/0/classifier/2.png) |

#### **Hidden layer dimension 512**

| layer | epoch0 | epoch60  | epoch99 |
|:-----:|:------: |:-------:|:-------:|
| 0     |![](/results/hdim512/images/backprop/normalizedPCA/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/backprop/normalizedPCA/epoch60/0/classifier/0.png) | ![](/results/hdim512/images/backprop/normalizedPCA/epoch99/0/classifier/0.png) |
1       | ![](/results/hdim512/images/backprop/normalizedPCA/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/backprop/normalizedPCA/epoch60/0/classifier/1.png) | ![](/results/hdim512/images/backprop/normalizedPCA/epoch99/0/classifier/1.png) |
2       | ![](/results/hdim512/images/backprop/normalizedPCA/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/backprop/normalizedPCA/epoch60/0/classifier/2.png) | ![](/results/hdim512/images/backprop/normalizedPCA/epoch99/0/classifier/2.png) |

#### **Hidden layer dimension 1000**

| layer | epoch0 | epoch60  | epoch99 |
|:-----:|:------: |:-------:|:-------:|
| 0     |![](/results/hdim1000/images/backprop/normalizedPCA/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/backprop/normalizedPCA/epoch60/0/classifier/0.png) | ![](/results/hdim1000/images/backprop/normalizedPCA/epoch99/0/classifier/0.png) |
1       | ![](/results/hdim1000/images/backprop/normalizedPCA/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/backprop/normalizedPCA/epoch60/0/classifier/1.png) | ![](/results/hdim1000/images/backprop/normalizedPCA/epoch99/0/classifier/1.png) |
2       | ![](/results/hdim1000/images/backprop/normalizedPCA/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/backprop/normalizedPCA/epoch60/0/classifier/2.png) | ![](/results/hdim1000/images/backprop/normalizedPCA/epoch99/0/classifier/2.png) |

-----------------------------

### <center>**1.1.4 standard PCA**</center>
Here the layer is clean and untouched for plotting using PCA.

#### **Hidden layer dimension 256**

| layer | epoch0 | epoch60  | epoch99 |
|:-----:|:------: |:-------:|:-------:|
| 0     |![](/results/hdim256/images/backprop/PCA/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/backprop/PCA/epoch60/0/classifier/0.png) | ![](/results/hdim256/images/backprop/PCA/epoch99/0/classifier/0.png) |
1       | ![](/results/hdim256/images/backprop/PCA/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/backprop/PCA/epoch60/0/classifier/1.png) | ![](/results/hdim256/images/backprop/PCA/epoch99/0/classifier/1.png) |
2       | ![](/results/hdim256/images/backprop/PCA/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/backprop/PCA/epoch60/0/classifier/2.png) | ![](/results/hdim256/images/backprop/PCA/epoch99/0/classifier/2.png) |

#### **Hidden layer dimension 512**

| layer | epoch0 | epoch60  | epoch99 |
|:-----:|:------: |:-------:|:-------:|
| 0     |![](/results/hdim512/images/backprop/PCA/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/backprop/PCA/epoch60/0/classifier/0.png) | ![](/results/hdim512/images/backprop/PCA/epoch99/0/classifier/0.png) |
1       | ![](/results/hdim512/images/backprop/PCA/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/backprop/PCA/epoch60/0/classifier/1.png) | ![](/results/hdim512/images/backprop/PCA/epoch99/0/classifier/1.png) |
2       | ![](/results/hdim512/images/backprop/PCA/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/backprop/PCA/epoch60/0/classifier/2.png) | ![](/results/hdim512/images/backprop/PCA/epoch99/0/classifier/2.png) |

#### **Hidden layer dimension 1000**

| layer | epoch0 | epoch60  | epoch99 |
|:-----:|:------: |:-------:|:-------:|
| 0     |![](/results/hdim1000/images/backprop/PCA/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/backprop/PCA/epoch60/0/classifier/0.png) | ![](/results/hdim1000/images/backprop/PCA/epoch99/0/classifier/0.png) |
1       | ![](/results/hdim1000/images/backprop/PCA/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/backprop/PCA/epoch60/0/classifier/1.png) | ![](/results/hdim1000/images/backprop/PCA/epoch99/0/classifier/1.png) |
2       | ![](/results/hdim1000/images/backprop/PCA/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/backprop/PCA/epoch60/0/classifier/2.png) | ![](/results/hdim1000/images/backprop/PCA/epoch99/0/classifier/2.png) |

-----------------------------


## <center>**1.2 Comparison of Normalization vs Non-normalization of the layer with itself in different epochs**</center>
This is used to compare if better results are obtained with or without normalization of the layer.

`batch of reference:0 `

### <center>**1.2.1 TSNE plotting**</center>
Here the plotting is done using TSNE

#### **Hidden layer dim 256**
| layer | normalized | epoch0 | epoch60 | epoch99 |
|:-----:|:----------:|:------:|:-------:|:-------:|
| 0     | yes | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch60/0/classifier/0.png) | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch99/0/classifier/0.png) |
| 0     | no  | ![](/results/hdim256/images/backprop/TSNE/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/backprop/TSNE/epoch60/0/classifier/0.png) | ![](/results/hdim256/images/backprop/TSNE/epoch99/0/classifier/0.png) |
| 1     | yes | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch60/0/classifier/1.png) | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch99/0/classifier/1.png) |
| 1     | no  | ![](/results/hdim256/images/backprop/TSNE/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/backprop/TSNE/epoch60/0/classifier/1.png) | ![](/results/hdim256/images/backprop/TSNE/epoch99/0/classifier/1.png) |
| 2     | yes | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch60/0/classifier/2.png) | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch99/0/classifier/2.png) |
| 2     | no  | ![](/results/hdim256/images/backprop/TSNE/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/backprop/TSNE/epoch60/0/classifier/2.png) | ![](/results/hdim256/images/backprop/TSNE/epoch99/0/classifier/2.png) |


#### **Hidden layer dim 512**
| layer | normalized | epoch0 | epoch60 | epoch99 |
|:-----:|:----------:|:------:|:-------:|:-------:|
| 0     | yes | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch60/0/classifier/0.png) | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch99/0/classifier/0.png) |
| 0     | no  | ![](/results/hdim512/images/backprop/TSNE/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/backprop/TSNE/epoch60/0/classifier/0.png) | ![](/results/hdim512/images/backprop/TSNE/epoch99/0/classifier/0.png) |
| 1     | yes | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch60/0/classifier/1.png) | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch99/0/classifier/1.png) |
| 1     | no  | ![](/results/hdim512/images/backprop/TSNE/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/backprop/TSNE/epoch60/0/classifier/1.png) | ![](/results/hdim512/images/backprop/TSNE/epoch99/0/classifier/1.png) |
| 2     | yes | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch60/0/classifier/2.png) | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch99/0/classifier/2.png) |
| 2     | no  | ![](/results/hdim512/images/backprop/TSNE/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/backprop/TSNE/epoch60/0/classifier/2.png) | ![](/results/hdim512/images/backprop/TSNE/epoch99/0/classifier/2.png) |


#### **Hidden layer dim 1000**
| layer | normalized | epoch0 | epoch60 | epoch99 |
|:-----:|:----------:|:------:|:-------:|:-------:|
| 0     | yes | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch60/0/classifier/0.png) | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch99/0/classifier/0.png) |
| 0     | no  | ![](/results/hdim1000/images/backprop/TSNE/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/backprop/TSNE/epoch60/0/classifier/0.png) | ![](/results/hdim1000/images/backprop/TSNE/epoch99/0/classifier/0.png) |
| 1     | yes | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch60/0/classifier/1.png) | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch99/0/classifier/1.png) |
| 1     | no  | ![](/results/hdim1000/images/backprop/TSNE/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/backprop/TSNE/epoch60/0/classifier/1.png) | ![](/results/hdim1000/images/backprop/TSNE/epoch99/0/classifier/1.png) |
| 2     | yes | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch60/0/classifier/2.png) | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch99/0/classifier/2.png) |
| 2     | no  | ![](/results/hdim1000/images/backprop/TSNE/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/backprop/TSNE/epoch60/0/classifier/2.png) | ![](/results/hdim1000/images/backprop/TSNE/epoch99/0/classifier/2.png) |

-----------------------------

### <center>**1.2.2 PCA plotting**</center>
Here the plotting is done using PCA

#### **Hidden layer dim 256**
| layer | normalized | epoch0 | epoch60 | epoch99 |
|:-----:|:----------:|:------:|:-------:|:-------:|
| 0     | yes | ![](/results/hdim256/images/backprop/normalizedPCA/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/backprop/normalizedPCA/epoch60/0/classifier/0.png) | ![](/results/hdim256/images/backprop/normalizedPCA/epoch99/0/classifier/0.png) |
| 0     | no  | ![](/results/hdim256/images/backprop/PCA/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/backprop/PCA/epoch60/0/classifier/0.png) | ![](/results/hdim256/images/backprop/PCA/epoch99/0/classifier/0.png) |
| 1     | yes | ![](/results/hdim256/images/backprop/normalizedPCA/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/backprop/normalizedPCA/epoch60/0/classifier/1.png) | ![](/results/hdim256/images/backprop/normalizedPCA/epoch99/0/classifier/1.png) |
| 1     | no  | ![](/results/hdim256/images/backprop/PCA/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/backprop/PCA/epoch60/0/classifier/1.png) | ![](/results/hdim256/images/backprop/PCA/epoch99/0/classifier/1.png) |
| 2     | yes | ![](/results/hdim256/images/backprop/normalizedPCA/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/backprop/normalizedPCA/epoch60/0/classifier/2.png) | ![](/results/hdim256/images/backprop/normalizedPCA/epoch99/0/classifier/2.png) |
| 2     | no  | ![](/results/hdim256/images/backprop/PCA/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/backprop/PCA/epoch60/0/classifier/2.png) | ![](/results/hdim256/images/backprop/PCA/epoch99/0/classifier/2.png) |


#### **Hidden layer dim 512**
| layer | normalized | epoch0 | epoch60 | epoch99 |
|:-----:|:----------:|:------:|:-------:|:-------:|
| 0     | yes | ![](/results/hdim512/images/backprop/normalizedPCA/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/backprop/normalizedPCA/epoch60/0/classifier/0.png) | ![](/results/hdim512/images/backprop/normalizedPCA/epoch99/0/classifier/0.png) |
| 0     | no  | ![](/results/hdim512/images/backprop/PCA/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/backprop/PCA/epoch60/0/classifier/0.png) | ![](/results/hdim512/images/backprop/PCA/epoch99/0/classifier/0.png) |
| 1     | yes | ![](/results/hdim512/images/backprop/normalizedPCA/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/backprop/normalizedPCA/epoch60/0/classifier/1.png) | ![](/results/hdim512/images/backprop/normalizedPCA/epoch99/0/classifier/1.png) |
| 1     | no  | ![](/results/hdim512/images/backprop/PCA/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/backprop/PCA/epoch60/0/classifier/1.png) | ![](/results/hdim512/images/backprop/PCA/epoch99/0/classifier/1.png) |
| 2     | yes | ![](/results/hdim512/images/backprop/normalizedPCA/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/backprop/normalizedPCA/epoch60/0/classifier/2.png) | ![](/results/hdim512/images/backprop/normalizedPCA/epoch99/0/classifier/2.png) |
| 2     | no  | ![](/results/hdim512/images/backprop/PCA/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/backprop/PCA/epoch60/0/classifier/2.png) | ![](/results/hdim512/images/backprop/PCA/epoch99/0/classifier/2.png) |


#### **Hidden layer dim 1000**
| layer | normalized | epoch0 | epoch60 | epoch99 |
|:-----:|:----------:|:------:|:-------:|:-------:|
| 0     | yes | ![](/results/hdim1000/images/backprop/normalizedPCA/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/backprop/normalizedPCA/epoch60/0/classifier/0.png) | ![](/results/hdim1000/images/backprop/normalizedPCA/epoch99/0/classifier/0.png) |
| 0     | no  | ![](/results/hdim1000/images/backprop/PCA/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/backprop/PCA/epoch60/0/classifier/0.png) | ![](/results/hdim1000/images/backprop/PCA/epoch99/0/classifier/0.png) |
| 1     | yes | ![](/results/hdim1000/images/backprop/normalizedPCA/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/backprop/normalizedPCA/epoch60/0/classifier/1.png) | ![](/results/hdim1000/images/backprop/normalizedPCA/epoch99/0/classifier/1.png) |
| 1     | no  | ![](/results/hdim1000/images/backprop/PCA/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/backprop/PCA/epoch60/0/classifier/1.png) | ![](/results/hdim1000/images/backprop/PCA/epoch99/0/classifier/1.png) |
| 2     | yes | ![](/results/hdim1000/images/backprop/normalizedPCA/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/backprop/normalizedPCA/epoch60/0/classifier/2.png) | ![](/results/hdim1000/images/backprop/normalizedPCA/epoch99/0/classifier/2.png) |
| 2     | no  | ![](/results/hdim1000/images/backprop/PCA/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/backprop/PCA/epoch60/0/classifier/2.png) | ![](/results/hdim1000/images/backprop/PCA/epoch99/0/classifier/2.png) |

-----------------------------


## <center>**1.3 Compare layer with itself in different epochs and layer dimension**</center>
This is used to compare how different layer dimensions act on the features.

`batch of reference:0 `

### <center>**1.3.1 TSNE plotting**</center>
Here the plotting is done using TSNE.

#### **Normalized TSNE**
Here the layer has been normalized before plotting using TSNE.

##### **layer 0**
| hdim | epoch0 | epoch60  | epoch99 |
|:----:|:------: |:-------:|:-------:|
| 256  | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch60/0/classifier/0.png) |![](/results/hdim256/images/backprop/normalizedTSNE/epoch99/0/classifier/0.png) |
| 512  | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch60/0/classifier/0.png) | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch99/0/classifier/0.png) |
| 1000 | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch60/0/classifier/0.png) | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch99/0/classifier/0.png) |

##### **layer 1**
| hdim | epoch0 | epoch60  | epoch99 |
|:----:|:------: |:-------:|:-------:|
| 256  | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch60/0/classifier/1.png) |![](/results/hdim256/images/backprop/normalizedTSNE/epoch99/0/classifier/1.png) |
| 512  | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch60/0/classifier/1.png) | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch99/0/classifier/1.png) |
| 1000 | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch60/0/classifier/1.png) | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch99/0/classifier/1.png) |

##### **layer 2**
| hdim | epoch0 | epoch60  | epoch99 |
|:----:|:------: |:-------:|:-------:|
| 256  | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch60/0/classifier/2.png) |![](/results/hdim256/images/backprop/normalizedTSNE/epoch99/0/classifier/2.png) |
| 512  | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch60/0/classifier/2.png) | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch99/0/classifier/2.png) |
| 1000 | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch60/0/classifier/2.png) | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch99/0/classifier/2.png) |

-----------------------------

#### **Standard TSNE**
Here the layer is clean and untouched for plotting using TSNE.

##### **layer 0**
| hdim | epoch0 | epoch60  | epoch99 |
|:----:|:------: |:-------:|:-------:|
| 256  | ![](/results/hdim256/images/backprop/TSNE/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/backprop/TSNE/epoch60/0/classifier/0.png) |![](/results/hdim256/images/backprop/TSNE/epoch99/0/classifier/0.png) |
| 512  | ![](/results/hdim512/images/backprop/TSNE/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/backprop/TSNE/epoch60/0/classifier/0.png) | ![](/results/hdim512/images/backprop/TSNE/epoch99/0/classifier/0.png) |
| 1000 | ![](/results/hdim1000/images/backprop/TSNE/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/backprop/TSNE/epoch60/0/classifier/0.png) | ![](/results/hdim1000/images/backprop/TSNE/epoch99/0/classifier/0.png) |

##### **layer 1**
| hdim | epoch0 | epoch60  | epoch99 |
|:----:|:------: |:-------:|:-------:|
| 256  | ![](/results/hdim256/images/backprop/TSNE/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/backprop/TSNE/epoch60/0/classifier/1.png) |![](/results/hdim256/images/backprop/TSNE/epoch99/0/classifier/1.png) |
| 512  | ![](/results/hdim512/images/backprop/TSNE/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/backprop/TSNE/epoch60/0/classifier/1.png) | ![](/results/hdim512/images/backprop/TSNE/epoch99/0/classifier/1.png) |
| 1000 | ![](/results/hdim1000/images/backprop/TSNE/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/backprop/TSNE/epoch60/0/classifier/1.png) | ![](/results/hdim1000/images/backprop/TSNE/epoch99/0/classifier/1.png) |

##### **layer 2**
| hdim | epoch0 | epoch60  | epoch99 |
|:----:|:------: |:-------:|:-------:|
| 256  | ![](/results/hdim256/images/backprop/TSNE/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/backprop/TSNE/epoch60/0/classifier/2.png) |![](/results/hdim256/images/backprop/TSNE/epoch99/0/classifier/2.png) |
| 512  | ![](/results/hdim512/images/backprop/TSNE/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/backprop/TSNE/epoch60/0/classifier/2.png) | ![](/results/hdim512/images/backprop/TSNE/epoch99/0/classifier/2.png) |
| 1000 | ![](/results/hdim1000/images/backprop/TSNE/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/backprop/TSNE/epoch60/0/classifier/2.png) | ![](/results/hdim1000/images/backprop/TSNE/epoch99/0/classifier/2.png) |

-----------------------------

### <center>**1.3.2 PCA plotting**</center>
Here the plotting is done using PCA.

#### **Normalized PCA**
Here the layer has been normalized before plotting using PCA.

##### **layer 0**
| hdim | epoch0 | epoch60  | epoch99 |
|:----:|:------: |:-------:|:-------:|
| 256  | ![](/results/hdim256/images/backprop/normalizedPCA/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/backprop/normalizedPCA/epoch60/0/classifier/0.png) |![](/results/hdim256/images/backprop/normalizedPCA/epoch99/0/classifier/0.png) |
| 512  | ![](/results/hdim512/images/backprop/normalizedPCA/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/backprop/normalizedPCA/epoch60/0/classifier/0.png) | ![](/results/hdim512/images/backprop/normalizedPCA/epoch99/0/classifier/0.png) |
| 1000 | ![](/results/hdim1000/images/backprop/normalizedPCA/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/backprop/normalizedPCA/epoch60/0/classifier/0.png) | ![](/results/hdim1000/images/backprop/normalizedPCA/epoch99/0/classifier/0.png) |

##### **layer 1**
| hdim | epoch0 | epoch60  | epoch99 |
|:----:|:------: |:-------:|:-------:|
| 256  | ![](/results/hdim256/images/backprop/normalizedPCA/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/backprop/normalizedPCA/epoch60/0/classifier/1.png) |![](/results/hdim256/images/backprop/normalizedPCA/epoch99/0/classifier/1.png) |
| 512  | ![](/results/hdim512/images/backprop/normalizedPCA/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/backprop/normalizedPCA/epoch60/0/classifier/1.png) | ![](/results/hdim512/images/backprop/normalizedPCA/epoch99/0/classifier/1.png) |
| 1000 | ![](/results/hdim1000/images/backprop/normalizedPCA/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/backprop/normalizedPCA/epoch60/0/classifier/1.png) | ![](/results/hdim1000/images/backprop/normalizedPCA/epoch99/0/classifier/1.png) |

##### **layer 2**
| hdim | epoch0 | epoch60  | epoch99 |
|:----:|:------: |:-------:|:-------:|
| 256  | ![](/results/hdim256/images/backprop/normalizedPCA/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/backprop/normalizedPCA/epoch60/0/classifier/2.png) |![](/results/hdim256/images/backprop/normalizedPCA/epoch99/0/classifier/2.png) |
| 512  | ![](/results/hdim512/images/backprop/normalizedPCA/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/backprop/normalizedPCA/epoch60/0/classifier/2.png) | ![](/results/hdim512/images/backprop/normalizedPCA/epoch99/0/classifier/2.png) |
| 1000 | ![](/results/hdim1000/images/backprop/normalizedPCA/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/backprop/normalizedPCA/epoch60/0/classifier/2.png) | ![](/results/hdim1000/images/backprop/normalizedPCA/epoch99/0/classifier/2.png) |

-----------------------------

#### **Standard PCA**
Here the layer is clean and untouched for plotting using PCA.

##### **layer 0**
| hdim | epoch0 | epoch60  | epoch99 |
|:----:|:------: |:-------:|:-------:|
| 256  | ![](/results/hdim256/images/backprop/PCA/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/backprop/PCA/epoch60/0/classifier/0.png) |![](/results/hdim256/images/backprop/PCA/epoch99/0/classifier/0.png) |
| 512  | ![](/results/hdim512/images/backprop/PCA/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/backprop/PCA/epoch60/0/classifier/0.png) | ![](/results/hdim512/images/backprop/PCA/epoch99/0/classifier/0.png) |
| 1000 | ![](/results/hdim1000/images/backprop/PCA/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/backprop/PCA/epoch60/0/classifier/0.png) | ![](/results/hdim1000/images/backprop/PCA/epoch99/0/classifier/0.png) |

##### **layer 1**
| hdim | epoch0 | epoch60  | epoch99 |
|:----:|:------: |:-------:|:-------:|
| 256  | ![](/results/hdim256/images/backprop/PCA/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/backprop/PCA/epoch60/0/classifier/1.png) |![](/results/hdim256/images/backprop/PCA/epoch99/0/classifier/1.png) |
| 512  | ![](/results/hdim512/images/backprop/PCA/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/backprop/PCA/epoch60/0/classifier/1.png) | ![](/results/hdim512/images/backprop/PCA/epoch99/0/classifier/1.png) |
| 1000 | ![](/results/hdim1000/images/backprop/PCA/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/backprop/PCA/epoch60/0/classifier/1.png) | ![](/results/hdim1000/images/backprop/PCA/epoch99/0/classifier/1.png) |

##### **layer 2**
| hdim | epoch0 | epoch60  | epoch99 |
|:----:|:------: |:-------:|:-------:|
| 256  | ![](/results/hdim256/images/backprop/PCA/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/backprop/PCA/epoch60/0/classifier/2.png) |![](/results/hdim256/images/backprop/PCA/epoch99/0/classifier/2.png) |
| 512  | ![](/results/hdim512/images/backprop/PCA/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/backprop/PCA/epoch60/0/classifier/2.png) | ![](/results/hdim512/images/backprop/PCA/epoch99/0/classifier/2.png) |
| 1000 | ![](/results/hdim1000/images/backprop/PCA/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/backprop/PCA/epoch60/0/classifier/2.png) | ![](/results/hdim1000/images/backprop/PCA/epoch99/0/classifier/2.png) |




## <center>**1.4 PCA vs TSNE**</center>

### <center>**1.4.1 compare layer with itself in different epochs with PCA and TSNE**</center>
This is to compare how a layer evolves in comparison between PCA and TSNE

`batch of reference:0 `


### **Normalized**

#### layer 0
| hdim  | PCA or TSNE | epoch0 | epoch60 | epoch99 |
|:-----:|:-----------:|:------:|:-------:|:-------:|
|  256  |  PCA   | ![](/results/hdim256/images/backprop/normalizedPCA/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/backprop/normalizedPCA/epoch60/0/classifier/0.png) |![](/results/hdim256/images/backprop/normalizedPCA/epoch99/0/classifier/0.png) |
|  256  |  TSNE  | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch60/0/classifier/0.png) |![](/results/hdim256/images/backprop/normalizedTSNE/epoch99/0/classifier/0.png) |
|  512  |  PCA   | ![](/results/hdim512/images/backprop/normalizedPCA/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/backprop/normalizedPCA/epoch60/0/classifier/0.png) |![](/results/hdim512/images/backprop/normalizedPCA/epoch99/0/classifier/0.png) |
|  512  |  TSNE  | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch60/0/classifier/0.png) |![](/results/hdim512/images/backprop/normalizedTSNE/epoch99/0/classifier/0.png) |
| 1000  |  PCA   | ![](/results/hdim1000/images/backprop/normalizedPCA/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/backprop/normalizedPCA/epoch60/0/classifier/0.png) |![](/results/hdim1000/images/backprop/normalizedPCA/epoch99/0/classifier/0.png) |
| 1000  |  TSNE  | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch60/0/classifier/0.png) |![](/results/hdim1000/images/backprop/normalizedTSNE/epoch99/0/classifier/0.png) |


#### layer 1
| hdim  | PCA or TSNE | epoch0 | epoch60 | epoch99 |
|:-----:|:-----------:|:------:|:-------:|:-------:|
|  256  |  PCA   | ![](/results/hdim256/images/backprop/normalizedPCA/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/backprop/normalizedPCA/epoch60/0/classifier/1.png) |![](/results/hdim256/images/backprop/normalizedPCA/epoch99/0/classifier/1.png) |
|  256  |  TSNE  | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch60/0/classifier/1.png) |![](/results/hdim256/images/backprop/normalizedTSNE/epoch99/0/classifier/1.png) |
|  512  |  PCA   | ![](/results/hdim512/images/backprop/normalizedPCA/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/backprop/normalizedPCA/epoch60/0/classifier/1.png) |![](/results/hdim512/images/backprop/normalizedPCA/epoch99/0/classifier/1.png) |
|  512  |  TSNE  | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch60/0/classifier/1.png) |![](/results/hdim512/images/backprop/normalizedTSNE/epoch99/0/classifier/1.png) |
| 1000  |  PCA   | ![](/results/hdim1000/images/backprop/normalizedPCA/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/backprop/normalizedPCA/epoch60/0/classifier/1.png) |![](/results/hdim1000/images/backprop/normalizedPCA/epoch99/0/classifier/1.png) |
| 1000  |  TSNE  | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/backprop/normalizedTSNE/epoch60/0/classifier/1.png) |![](/results/hdim1000/images/backprop/normalizedTSNE/epoch99/0/classifier/1.png) |


#### layer 2
| hdim  | PCA or TSNE | epoch0 | epoch60 | epoch99 |
|:-----:|:-----------:|:------:|:-------:|:-------:|
|  256  |  PCA   | ![](/results/hdim256/images/backprop/normalizedPCA/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/backprop/normalizedPCA/epoch60/0/classifier/2.png) |![](/results/hdim256/images/backprop/normalizedPCA/epoch99/0/classifier/2.png) |
|  256  |  TSNE  | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/backprop/normalizedTSNE/epoch60/0/classifier/2.png) |![](/results/hdim256/images/backprop/normalizedTSNE/epoch99/0/classifier/2.png) |
|  512  |  PCA   | ![](/results/hdim512/images/backprop/normalizedPCA/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/backprop/normalizedPCA/epoch60/0/classifier/2.png) |![](/results/hdim512/images/backprop/normalizedPCA/epoch99/0/classifier/2.png) |
|  512  |  TSNE  | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/backprop/normalizedTSNE/epoch60/0/classifier/2.png) |![](/results/hdim512/images/backprop/normalizedTSNE/epoch99/0/classifier/2.png) |
| 1000  |  PCA   | ![](/results/hdim1000/images/backprop/normalizedPCA/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/backprop/normalizedPCA/epoch60/0/classifier/2.png) |![](/results/hdim1000/images/backprop/normalizedPCA/epoch99/0/classifier/2.png) |
| 1000  |  TSNE  | ![](/results/hdim1000/images/backprop/TSNE/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/backprop/TSNE/epoch60/0/classifier/2.png) |![](/results/hdim1000/images/backprop/TSNE/epoch99/0/classifier/2.png) |


### **Standard**

#### layer 0
| hdim  | PCA or TSNE | epoch0 | epoch60 | epoch99 |
|:-----:|:-----------:|:------:|:-------:|:-------:|
|  256  |  PCA   | ![](/results/hdim256/images/backprop/PCA/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/backprop/PCA/epoch60/0/classifier/0.png) |![](/results/hdim256/images/backprop/PCA/epoch99/0/classifier/0.png) |
|  256  |  TSNE  | ![](/results/hdim256/images/backprop/TSNE/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/backprop/TSNE/epoch60/0/classifier/0.png) |![](/results/hdim256/images/backprop/TSNE/epoch99/0/classifier/0.png) |
|  512  |  PCA   | ![](/results/hdim512/images/backprop/PCA/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/backprop/PCA/epoch60/0/classifier/0.png) |![](/results/hdim512/images/backprop/PCA/epoch99/0/classifier/0.png) |
|  512  |  TSNE  | ![](/results/hdim512/images/backprop/TSNE/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/backprop/TSNE/epoch60/0/classifier/0.png) |![](/results/hdim512/images/backprop/TSNE/epoch99/0/classifier/0.png) |
| 1000  |  PCA   | ![](/results/hdim1000/images/backprop/PCA/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/backprop/PCA/epoch60/0/classifier/0.png) |![](/results/hdim1000/images/backprop/PCA/epoch99/0/classifier/0.png) |
| 1000  |  TSNE  | ![](/results/hdim1000/images/backprop/TSNE/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/backprop/TSNE/epoch60/0/classifier/0.png) |![](/results/hdim1000/images/backprop/TSNE/epoch99/0/classifier/0.png) |


#### layer 1
| hdim  | PCA or TSNE | epoch0 | epoch60 | epoch99 |
|:-----:|:-----------:|:------:|:-------:|:-------:|
|  256  |  PCA   | ![](/results/hdim256/images/backprop/PCA/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/backprop/PCA/epoch60/0/classifier/1.png) |![](/results/hdim256/images/backprop/PCA/epoch99/0/classifier/1.png) |
|  256  |  TSNE  | ![](/results/hdim256/images/backprop/TSNE/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/backprop/TSNE/epoch60/0/classifier/1.png) |![](/results/hdim256/images/backprop/TSNE/epoch99/0/classifier/1.png) |
|  512  |  PCA   | ![](/results/hdim512/images/backprop/PCA/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/backprop/PCA/epoch60/0/classifier/1.png) |![](/results/hdim512/images/backprop/PCA/epoch99/0/classifier/1.png) |
|  512  |  TSNE  | ![](/results/hdim512/images/backprop/TSNE/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/backprop/TSNE/epoch60/0/classifier/1.png) |![](/results/hdim512/images/backprop/TSNE/epoch99/0/classifier/1.png) |
| 1000  |  PCA   | ![](/results/hdim1000/images/backprop/PCA/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/backprop/PCA/epoch60/0/classifier/1.png) |![](/results/hdim1000/images/backprop/PCA/epoch99/0/classifier/1.png) |
| 1000  |  TSNE  | ![](/results/hdim1000/images/backprop/TSNE/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/backprop/TSNE/epoch60/0/classifier/1.png) |![](/results/hdim1000/images/backprop/TSNE/epoch99/0/classifier/1.png) |


#### layer 2
| hdim  | PCA or TSNE | epoch0 | epoch60 | epoch99 |
|:-----:|:-----------:|:------:|:-------:|:-------:|
|  256  |  PCA   | ![](/results/hdim256/images/backprop/PCA/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/backprop/PCA/epoch60/0/classifier/2.png) |![](/results/hdim256/images/backprop/PCA/epoch99/0/classifier/2.png) |
|  256  |  TSNE  | ![](/results/hdim256/images/backprop/TSNE/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/backprop/TSNE/epoch60/0/classifier/2.png) |![](/results/hdim256/images/backprop/TSNE/epoch99/0/classifier/2.png) |
|  512  |  PCA   | ![](/results/hdim512/images/backprop/PCA/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/backprop/PCA/epoch60/0/classifier/2.png) |![](/results/hdim512/images/backprop/PCA/epoch99/0/classifier/2.png) |
|  512  |  TSNE  | ![](/results/hdim512/images/backprop/TSNE/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/backprop/TSNE/epoch60/0/classifier/2.png) |![](/results/hdim512/images/backprop/TSNE/epoch99/0/classifier/2.png) |
| 1000  |  PCA   | ![](/results/hdim1000/images/backprop/PCA/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/backprop/PCA/epoch60/0/classifier/2.png) |![](/results/hdim1000/images/backprop/PCA/epoch99/0/classifier/2.png) |
| 1000  |  TSNE  | ![](/results/hdim1000/images/backprop/TSNE/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/backprop/TSNE/epoch60/0/classifier/2.png) |![](/results/hdim1000/images/backprop/TSNE/epoch99/0/classifier/2.png) |






----------------------------

# <center>**2 Forward-Forward results**</center>
In this chapter the results for the Forward-Forward approach are displayed.

## <center>**1.1 compare layer with itself in different epochs**</center>
This allows us to see the evolution of the layer itself over time.

`batch of reference:0 `
### <center>**1.1.1 Normalized TSNE**</center>
Here the layer has been normalized before plotting using TSNE.

#### **Hidden layer dimension 256**

| layer | epoch0 | epoch60  | epoch99 |
|:-----:|:------: |:-------:|:-------:|
| 0     |![](/results/hdim256/images/FF/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/FF/normalizedTSNE/epoch60/0/classifier/0.png) | ![](/results/hdim256/images/FF/normalizedTSNE/epoch99/0/classifier/0.png) |
1       | ![](/results/hdim256/images/FF/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/FF/normalizedTSNE/epoch60/0/classifier/1.png) | ![](/results/hdim256/images/FF/normalizedTSNE/epoch99/0/classifier/1.png) |
2       | ![](/results/hdim256/images/FF/normalizedTSNE/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/FF/normalizedTSNE/epoch60/0/classifier/2.png) | ![](/results/hdim256/images/FF/normalizedTSNE/epoch99/0/classifier/2.png) |

#### **Hidden layer dimension 512**

| layer | epoch0 | epoch60  | epoch99 |
|:-----:|:------: |:-------:|:-------:|
| 0     |![](/results/hdim512/images/FF/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/FF/normalizedTSNE/epoch60/0/classifier/0.png) | ![](/results/hdim512/images/FF/normalizedTSNE/epoch99/0/classifier/0.png) |
1       | ![](/results/hdim512/images/FF/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/FF/normalizedTSNE/epoch60/0/classifier/1.png) | ![](/results/hdim512/images/FF/normalizedTSNE/epoch99/0/classifier/1.png) |
2       | ![](/results/hdim512/images/FF/normalizedTSNE/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/FF/normalizedTSNE/epoch60/0/classifier/2.png) | ![](/results/hdim512/images/FF/normalizedTSNE/epoch99/0/classifier/2.png) |

#### **Hidden layer dimension 1000**

| layer | epoch0 | epoch60  | epoch99 |
|:-----:|:------: |:-------:|:-------:|
| 0     |![](/results/hdim1000/images/FF/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch60/0/classifier/0.png) | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch99/0/classifier/0.png) |
1       | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch60/0/classifier/1.png) | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch99/0/classifier/1.png) |
2       | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch60/0/classifier/2.png) | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch99/0/classifier/2.png) |

-----------------------------

### <center>**1.1.2 standard TSNE**</center>
Here the layer is clean and untouched for plotting using TSNE.

#### **Hidden layer dimension 256**

| layer | epoch0 | epoch60  | epoch99 |
|:-----:|:------: |:-------:|:-------:|
| 0     |![](/results/hdim256/images/FF/TSNE/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/FF/TSNE/epoch60/0/classifier/0.png) | ![](/results/hdim256/images/FF/TSNE/epoch99/0/classifier/0.png) |
1       | ![](/results/hdim256/images/FF/TSNE/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/FF/TSNE/epoch60/0/classifier/1.png) | ![](/results/hdim256/images/FF/TSNE/epoch99/0/classifier/1.png) |
2       | ![](/results/hdim256/images/FF/TSNE/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/FF/TSNE/epoch60/0/classifier/2.png) | ![](/results/hdim256/images/FF/TSNE/epoch99/0/classifier/2.png) |

#### **Hidden layer dimension 512**

| layer | epoch0 | epoch60  | epoch99 |
|:-----:|:------: |:-------:|:-------:|
| 0     |![](/results/hdim512/images/FF/TSNE/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/FF/TSNE/epoch60/0/classifier/0.png) | ![](/results/hdim512/images/FF/TSNE/epoch99/0/classifier/0.png) |
1       | ![](/results/hdim512/images/FF/TSNE/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/FF/TSNE/epoch60/0/classifier/1.png) | ![](/results/hdim512/images/FF/TSNE/epoch99/0/classifier/1.png) |
2       | ![](/results/hdim512/images/FF/TSNE/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/FF/TSNE/epoch60/0/classifier/2.png) | ![](/results/hdim512/images/FF/TSNE/epoch99/0/classifier/2.png) |

#### **Hidden layer dimension 1000**

| layer | epoch0 | epoch60  | epoch99 |
|:-----:|:------: |:-------:|:-------:|
| 0     |![](/results/hdim1000/images/FF/TSNE/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/FF/TSNE/epoch60/0/classifier/0.png) | ![](/results/hdim1000/images/FF/TSNE/epoch99/0/classifier/0.png) |
1       | ![](/results/hdim1000/images/FF/TSNE/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/FF/TSNE/epoch60/0/classifier/1.png) | ![](/results/hdim1000/images/FF/TSNE/epoch99/0/classifier/1.png) |
2       | ![](/results/hdim1000/images/FF/TSNE/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/FF/TSNE/epoch60/0/classifier/2.png) | ![](/results/hdim1000/images/FF/TSNE/epoch99/0/classifier/2.png) |

-----------------------------

### <center>**1.1.3 Normalized PCA**</center>
Here the layer has been normalized before plotting using PCA.

#### **Hidden layer dimension 256**

| layer | epoch0 | epoch60  | epoch99 |
|:-----:|:------: |:-------:|:-------:|
| 0     |![](/results/hdim256/images/FF/normalizedPCA/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/FF/normalizedPCA/epoch60/0/classifier/0.png) | ![](/results/hdim256/images/FF/normalizedPCA/epoch99/0/classifier/0.png) |
1       | ![](/results/hdim256/images/FF/normalizedPCA/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/FF/normalizedPCA/epoch60/0/classifier/1.png) | ![](/results/hdim256/images/FF/normalizedPCA/epoch99/0/classifier/1.png) |
2       | ![](/results/hdim256/images/FF/normalizedPCA/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/FF/normalizedPCA/epoch60/0/classifier/2.png) | ![](/results/hdim256/images/FF/normalizedPCA/epoch99/0/classifier/2.png) |

#### **Hidden layer dimension 512**

| layer | epoch0 | epoch60  | epoch99 |
|:-----:|:------: |:-------:|:-------:|
| 0     |![](/results/hdim512/images/FF/normalizedPCA/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/FF/normalizedPCA/epoch60/0/classifier/0.png) | ![](/results/hdim512/images/FF/normalizedPCA/epoch99/0/classifier/0.png) |
1       | ![](/results/hdim512/images/FF/normalizedPCA/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/FF/normalizedPCA/epoch60/0/classifier/1.png) | ![](/results/hdim512/images/FF/normalizedPCA/epoch99/0/classifier/1.png) |
2       | ![](/results/hdim512/images/FF/normalizedPCA/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/FF/normalizedPCA/epoch60/0/classifier/2.png) | ![](/results/hdim512/images/FF/normalizedPCA/epoch99/0/classifier/2.png) |

#### **Hidden layer dimension 1000**

| layer | epoch0 | epoch60  | epoch99 |
|:-----:|:------: |:-------:|:-------:|
| 0     |![](/results/hdim1000/images/FF/normalizedPCA/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/FF/normalizedPCA/epoch60/0/classifier/0.png) | ![](/results/hdim1000/images/FF/normalizedPCA/epoch99/0/classifier/0.png) |
1       | ![](/results/hdim1000/images/FF/normalizedPCA/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/FF/normalizedPCA/epoch60/0/classifier/1.png) | ![](/results/hdim1000/images/FF/normalizedPCA/epoch99/0/classifier/1.png) |
2       | ![](/results/hdim1000/images/FF/normalizedPCA/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/FF/normalizedPCA/epoch60/0/classifier/2.png) | ![](/results/hdim1000/images/FF/normalizedPCA/epoch99/0/classifier/2.png) |

-----------------------------

### <center>**1.1.4 standard PCA**</center>
Here the layer is clean and untouched for plotting using PCA.

#### **Hidden layer dimension 256**

| layer | epoch0 | epoch60  | epoch99 |
|:-----:|:------: |:-------:|:-------:|
| 0     |![](/results/hdim256/images/FF/PCA/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/FF/PCA/epoch60/0/classifier/0.png) | ![](/results/hdim256/images/FF/PCA/epoch99/0/classifier/0.png) |
1       | ![](/results/hdim256/images/FF/PCA/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/FF/PCA/epoch60/0/classifier/1.png) | ![](/results/hdim256/images/FF/PCA/epoch99/0/classifier/1.png) |
2       | ![](/results/hdim256/images/FF/PCA/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/FF/PCA/epoch60/0/classifier/2.png) | ![](/results/hdim256/images/FF/PCA/epoch99/0/classifier/2.png) |

#### **Hidden layer dimension 512**

| layer | epoch0 | epoch60  | epoch99 |
|:-----:|:------: |:-------:|:-------:|
| 0     |![](/results/hdim512/images/FF/PCA/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/FF/PCA/epoch60/0/classifier/0.png) | ![](/results/hdim512/images/FF/PCA/epoch99/0/classifier/0.png) |
1       | ![](/results/hdim512/images/FF/PCA/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/FF/PCA/epoch60/0/classifier/1.png) | ![](/results/hdim512/images/FF/PCA/epoch99/0/classifier/1.png) |
2       | ![](/results/hdim512/images/FF/PCA/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/FF/PCA/epoch60/0/classifier/2.png) | ![](/results/hdim512/images/FF/PCA/epoch99/0/classifier/2.png) |

#### **Hidden layer dimension 1000**

| layer | epoch0 | epoch60  | epoch99 |
|:-----:|:------: |:-------:|:-------:|
| 0     |![](/results/hdim1000/images/FF/PCA/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/FF/PCA/epoch60/0/classifier/0.png) | ![](/results/hdim1000/images/FF/PCA/epoch99/0/classifier/0.png) |
1       | ![](/results/hdim1000/images/FF/PCA/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/FF/PCA/epoch60/0/classifier/1.png) | ![](/results/hdim1000/images/FF/PCA/epoch99/0/classifier/1.png) |
2       | ![](/results/hdim1000/images/FF/PCA/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/FF/PCA/epoch60/0/classifier/2.png) | ![](/results/hdim1000/images/FF/PCA/epoch99/0/classifier/2.png) |

-----------------------------


## <center>**1.2 Comparison of Normalization vs Non-normalization of the layer with itself in different epochs**</center>
This is used to compare if better results are obtained with or without normalization of the layer.

`batch of reference:0 `

### <center>**1.2.1 TSNE plotting**</center>
Here the plotting is done using TSNE

#### **Hidden layer dim 256**
| layer | normalized | epoch0 | epoch60 | epoch99 |
|:-----:|:----------:|:------:|:-------:|:-------:|
| 0     | yes | ![](/results/hdim256/images/FF/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/FF/normalizedTSNE/epoch60/0/classifier/0.png) | ![](/results/hdim256/images/FF/normalizedTSNE/epoch99/0/classifier/0.png) |
| 0     | no  | ![](/results/hdim256/images/FF/TSNE/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/FF/TSNE/epoch60/0/classifier/0.png) | ![](/results/hdim256/images/FF/TSNE/epoch99/0/classifier/0.png) |
| 1     | yes | ![](/results/hdim256/images/FF/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/FF/normalizedTSNE/epoch60/0/classifier/1.png) | ![](/results/hdim256/images/FF/normalizedTSNE/epoch99/0/classifier/1.png) |
| 1     | no  | ![](/results/hdim256/images/FF/TSNE/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/FF/TSNE/epoch60/0/classifier/1.png) | ![](/results/hdim256/images/FF/TSNE/epoch99/0/classifier/1.png) |
| 2     | yes | ![](/results/hdim256/images/FF/normalizedTSNE/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/FF/normalizedTSNE/epoch60/0/classifier/2.png) | ![](/results/hdim256/images/FF/normalizedTSNE/epoch99/0/classifier/2.png) |
| 2     | no  | ![](/results/hdim256/images/FF/TSNE/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/FF/TSNE/epoch60/0/classifier/2.png) | ![](/results/hdim256/images/FF/TSNE/epoch99/0/classifier/2.png) |


#### **Hidden layer dim 512**
| layer | normalized | epoch0 | epoch60 | epoch99 |
|:-----:|:----------:|:------:|:-------:|:-------:|
| 0     | yes | ![](/results/hdim512/images/FF/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/FF/normalizedTSNE/epoch60/0/classifier/0.png) | ![](/results/hdim512/images/FF/normalizedTSNE/epoch99/0/classifier/0.png) |
| 0     | no  | ![](/results/hdim512/images/FF/TSNE/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/FF/TSNE/epoch60/0/classifier/0.png) | ![](/results/hdim512/images/FF/TSNE/epoch99/0/classifier/0.png) |
| 1     | yes | ![](/results/hdim512/images/FF/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/FF/normalizedTSNE/epoch60/0/classifier/1.png) | ![](/results/hdim512/images/FF/normalizedTSNE/epoch99/0/classifier/1.png) |
| 1     | no  | ![](/results/hdim512/images/FF/TSNE/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/FF/TSNE/epoch60/0/classifier/1.png) | ![](/results/hdim512/images/FF/TSNE/epoch99/0/classifier/1.png) |
| 2     | yes | ![](/results/hdim512/images/FF/normalizedTSNE/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/FF/normalizedTSNE/epoch60/0/classifier/2.png) | ![](/results/hdim512/images/FF/normalizedTSNE/epoch99/0/classifier/2.png) |
| 2     | no  | ![](/results/hdim512/images/FF/TSNE/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/FF/TSNE/epoch60/0/classifier/2.png) | ![](/results/hdim512/images/FF/TSNE/epoch99/0/classifier/2.png) |


#### **Hidden layer dim 1000**
| layer | normalized | epoch0 | epoch60 | epoch99 |
|:-----:|:----------:|:------:|:-------:|:-------:|
| 0     | yes | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch60/0/classifier/0.png) | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch99/0/classifier/0.png) |
| 0     | no  | ![](/results/hdim1000/images/FF/TSNE/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/FF/TSNE/epoch60/0/classifier/0.png) | ![](/results/hdim1000/images/FF/TSNE/epoch99/0/classifier/0.png) |
| 1     | yes | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch60/0/classifier/1.png) | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch99/0/classifier/1.png) |
| 1     | no  | ![](/results/hdim1000/images/FF/TSNE/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/FF/TSNE/epoch60/0/classifier/1.png) | ![](/results/hdim1000/images/FF/TSNE/epoch99/0/classifier/1.png) |
| 2     | yes | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch60/0/classifier/2.png) | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch99/0/classifier/2.png) |
| 2     | no  | ![](/results/hdim1000/images/FF/TSNE/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/FF/TSNE/epoch60/0/classifier/2.png) | ![](/results/hdim1000/images/FF/TSNE/epoch99/0/classifier/2.png) |

-----------------------------

### <center>**1.2.2 PCA plotting**</center>
Here the plotting is done using PCA

#### **Hidden layer dim 256**
| layer | normalized | epoch0 | epoch60 | epoch99 |
|:-----:|:----------:|:------:|:-------:|:-------:|
| 0     | yes | ![](/results/hdim256/images/FF/normalizedPCA/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/FF/normalizedPCA/epoch60/0/classifier/0.png) | ![](/results/hdim256/images/FF/normalizedPCA/epoch99/0/classifier/0.png) |
| 0     | no  | ![](/results/hdim256/images/FF/PCA/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/FF/PCA/epoch60/0/classifier/0.png) | ![](/results/hdim256/images/FF/PCA/epoch99/0/classifier/0.png) |
| 1     | yes | ![](/results/hdim256/images/FF/normalizedPCA/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/FF/normalizedPCA/epoch60/0/classifier/1.png) | ![](/results/hdim256/images/FF/normalizedPCA/epoch99/0/classifier/1.png) |
| 1     | no  | ![](/results/hdim256/images/FF/PCA/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/FF/PCA/epoch60/0/classifier/1.png) | ![](/results/hdim256/images/FF/PCA/epoch99/0/classifier/1.png) |
| 2     | yes | ![](/results/hdim256/images/FF/normalizedPCA/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/FF/normalizedPCA/epoch60/0/classifier/2.png) | ![](/results/hdim256/images/FF/normalizedPCA/epoch99/0/classifier/2.png) |
| 2     | no  | ![](/results/hdim256/images/FF/PCA/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/FF/PCA/epoch60/0/classifier/2.png) | ![](/results/hdim256/images/FF/PCA/epoch99/0/classifier/2.png) |


#### **Hidden layer dim 512**
| layer | normalized | epoch0 | epoch60 | epoch99 |
|:-----:|:----------:|:------:|:-------:|:-------:|
| 0     | yes | ![](/results/hdim512/images/FF/normalizedPCA/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/FF/normalizedPCA/epoch60/0/classifier/0.png) | ![](/results/hdim512/images/FF/normalizedPCA/epoch99/0/classifier/0.png) |
| 0     | no  | ![](/results/hdim512/images/FF/PCA/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/FF/PCA/epoch60/0/classifier/0.png) | ![](/results/hdim512/images/FF/PCA/epoch99/0/classifier/0.png) |
| 1     | yes | ![](/results/hdim512/images/FF/normalizedPCA/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/FF/normalizedPCA/epoch60/0/classifier/1.png) | ![](/results/hdim512/images/FF/normalizedPCA/epoch99/0/classifier/1.png) |
| 1     | no  | ![](/results/hdim512/images/FF/PCA/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/FF/PCA/epoch60/0/classifier/1.png) | ![](/results/hdim512/images/FF/PCA/epoch99/0/classifier/1.png) |
| 2     | yes | ![](/results/hdim512/images/FF/normalizedPCA/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/FF/normalizedPCA/epoch60/0/classifier/2.png) | ![](/results/hdim512/images/FF/normalizedPCA/epoch99/0/classifier/2.png) |
| 2     | no  | ![](/results/hdim512/images/FF/PCA/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/FF/PCA/epoch60/0/classifier/2.png) | ![](/results/hdim512/images/FF/PCA/epoch99/0/classifier/2.png) |


#### **Hidden layer dim 1000**
| layer | normalized | epoch0 | epoch60 | epoch99 |
|:-----:|:----------:|:------:|:-------:|:-------:|
| 0     | yes | ![](/results/hdim1000/images/FF/normalizedPCA/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/FF/normalizedPCA/epoch60/0/classifier/0.png) | ![](/results/hdim1000/images/FF/normalizedPCA/epoch99/0/classifier/0.png) |
| 0     | no  | ![](/results/hdim1000/images/FF/PCA/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/FF/PCA/epoch60/0/classifier/0.png) | ![](/results/hdim1000/images/FF/PCA/epoch99/0/classifier/0.png) |
| 1     | yes | ![](/results/hdim1000/images/FF/normalizedPCA/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/FF/normalizedPCA/epoch60/0/classifier/1.png) | ![](/results/hdim1000/images/FF/normalizedPCA/epoch99/0/classifier/1.png) |
| 1     | no  | ![](/results/hdim1000/images/FF/PCA/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/FF/PCA/epoch60/0/classifier/1.png) | ![](/results/hdim1000/images/FF/PCA/epoch99/0/classifier/1.png) |
| 2     | yes | ![](/results/hdim1000/images/FF/normalizedPCA/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/FF/normalizedPCA/epoch60/0/classifier/2.png) | ![](/results/hdim1000/images/FF/normalizedPCA/epoch99/0/classifier/2.png) |
| 2     | no  | ![](/results/hdim1000/images/FF/PCA/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/FF/PCA/epoch60/0/classifier/2.png) | ![](/results/hdim1000/images/FF/PCA/epoch99/0/classifier/2.png) |

-----------------------------


## <center>**1.3 Compare layer with itself in different epochs and layer dimension**</center>
This is used to compare how different layer dimensions act on the features.

`batch of reference:0 `

### <center>**1.3.1 TSNE plotting**</center>
Here the plotting is done using TSNE.

#### **Normalized TSNE**
Here the layer has been normalized before plotting using TSNE.

##### **layer 0**
| hdim | epoch0 | epoch60  | epoch99 |
|:----:|:------: |:-------:|:-------:|
| 256  | ![](/results/hdim256/images/FF/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/FF/normalizedTSNE/epoch60/0/classifier/0.png) |![](/results/hdim256/images/FF/normalizedTSNE/epoch99/0/classifier/0.png) |
| 512  | ![](/results/hdim512/images/FF/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/FF/normalizedTSNE/epoch60/0/classifier/0.png) | ![](/results/hdim512/images/FF/normalizedTSNE/epoch99/0/classifier/0.png) |
| 1000 | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch60/0/classifier/0.png) | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch99/0/classifier/0.png) |

##### **layer 1**
| hdim | epoch0 | epoch60  | epoch99 |
|:----:|:------: |:-------:|:-------:|
| 256  | ![](/results/hdim256/images/FF/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/FF/normalizedTSNE/epoch60/0/classifier/1.png) |![](/results/hdim256/images/FF/normalizedTSNE/epoch99/0/classifier/1.png) |
| 512  | ![](/results/hdim512/images/FF/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/FF/normalizedTSNE/epoch60/0/classifier/1.png) | ![](/results/hdim512/images/FF/normalizedTSNE/epoch99/0/classifier/1.png) |
| 1000 | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch60/0/classifier/1.png) | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch99/0/classifier/1.png) |

##### **layer 2**
| hdim | epoch0 | epoch60  | epoch99 |
|:----:|:------: |:-------:|:-------:|
| 256  | ![](/results/hdim256/images/FF/normalizedTSNE/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/FF/normalizedTSNE/epoch60/0/classifier/2.png) |![](/results/hdim256/images/FF/normalizedTSNE/epoch99/0/classifier/2.png) |
| 512  | ![](/results/hdim512/images/FF/normalizedTSNE/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/FF/normalizedTSNE/epoch60/0/classifier/2.png) | ![](/results/hdim512/images/FF/normalizedTSNE/epoch99/0/classifier/2.png) |
| 1000 | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch60/0/classifier/2.png) | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch99/0/classifier/2.png) |

-----------------------------

#### **Standard TSNE**
Here the layer is clean and untouched for plotting using TSNE.

##### **layer 0**
| hdim | epoch0 | epoch60  | epoch99 |
|:----:|:------: |:-------:|:-------:|
| 256  | ![](/results/hdim256/images/FF/TSNE/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/FF/TSNE/epoch60/0/classifier/0.png) |![](/results/hdim256/images/FF/TSNE/epoch99/0/classifier/0.png) |
| 512  | ![](/results/hdim512/images/FF/TSNE/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/FF/TSNE/epoch60/0/classifier/0.png) | ![](/results/hdim512/images/FF/TSNE/epoch99/0/classifier/0.png) |
| 1000 | ![](/results/hdim1000/images/FF/TSNE/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/FF/TSNE/epoch60/0/classifier/0.png) | ![](/results/hdim1000/images/FF/TSNE/epoch99/0/classifier/0.png) |

##### **layer 1**
| hdim | epoch0 | epoch60  | epoch99 |
|:----:|:------: |:-------:|:-------:|
| 256  | ![](/results/hdim256/images/FF/TSNE/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/FF/TSNE/epoch60/0/classifier/1.png) |![](/results/hdim256/images/FF/TSNE/epoch99/0/classifier/1.png) |
| 512  | ![](/results/hdim512/images/FF/TSNE/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/FF/TSNE/epoch60/0/classifier/1.png) | ![](/results/hdim512/images/FF/TSNE/epoch99/0/classifier/1.png) |
| 1000 | ![](/results/hdim1000/images/FF/TSNE/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/FF/TSNE/epoch60/0/classifier/1.png) | ![](/results/hdim1000/images/FF/TSNE/epoch99/0/classifier/1.png) |

##### **layer 2**
| hdim | epoch0 | epoch60  | epoch99 |
|:----:|:------: |:-------:|:-------:|
| 256  | ![](/results/hdim256/images/FF/TSNE/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/FF/TSNE/epoch60/0/classifier/2.png) |![](/results/hdim256/images/FF/TSNE/epoch99/0/classifier/2.png) |
| 512  | ![](/results/hdim512/images/FF/TSNE/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/FF/TSNE/epoch60/0/classifier/2.png) | ![](/results/hdim512/images/FF/TSNE/epoch99/0/classifier/2.png) |
| 1000 | ![](/results/hdim1000/images/FF/TSNE/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/FF/TSNE/epoch60/0/classifier/2.png) | ![](/results/hdim1000/images/FF/TSNE/epoch99/0/classifier/2.png) |

-----------------------------

### <center>**1.3.2 PCA plotting**</center>
Here the plotting is done using PCA.

#### **Normalized PCA**
Here the layer has been normalized before plotting using PCA.

##### **layer 0**
| hdim | epoch0 | epoch60  | epoch99 |
|:----:|:------: |:-------:|:-------:|
| 256  | ![](/results/hdim256/images/FF/normalizedPCA/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/FF/normalizedPCA/epoch60/0/classifier/0.png) |![](/results/hdim256/images/FF/normalizedPCA/epoch99/0/classifier/0.png) |
| 512  | ![](/results/hdim512/images/FF/normalizedPCA/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/FF/normalizedPCA/epoch60/0/classifier/0.png) | ![](/results/hdim512/images/FF/normalizedPCA/epoch99/0/classifier/0.png) |
| 1000 | ![](/results/hdim1000/images/FF/normalizedPCA/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/FF/normalizedPCA/epoch60/0/classifier/0.png) | ![](/results/hdim1000/images/FF/normalizedPCA/epoch99/0/classifier/0.png) |

##### **layer 1**
| hdim | epoch0 | epoch60  | epoch99 |
|:----:|:------: |:-------:|:-------:|
| 256  | ![](/results/hdim256/images/FF/normalizedPCA/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/FF/normalizedPCA/epoch60/0/classifier/1.png) |![](/results/hdim256/images/FF/normalizedPCA/epoch99/0/classifier/1.png) |
| 512  | ![](/results/hdim512/images/FF/normalizedPCA/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/FF/normalizedPCA/epoch60/0/classifier/1.png) | ![](/results/hdim512/images/FF/normalizedPCA/epoch99/0/classifier/1.png) |
| 1000 | ![](/results/hdim1000/images/FF/normalizedPCA/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/FF/normalizedPCA/epoch60/0/classifier/1.png) | ![](/results/hdim1000/images/FF/normalizedPCA/epoch99/0/classifier/1.png) |

##### **layer 2**
| hdim | epoch0 | epoch60  | epoch99 |
|:----:|:------: |:-------:|:-------:|
| 256  | ![](/results/hdim256/images/FF/normalizedPCA/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/FF/normalizedPCA/epoch60/0/classifier/2.png) |![](/results/hdim256/images/FF/normalizedPCA/epoch99/0/classifier/2.png) |
| 512  | ![](/results/hdim512/images/FF/normalizedPCA/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/FF/normalizedPCA/epoch60/0/classifier/2.png) | ![](/results/hdim512/images/FF/normalizedPCA/epoch99/0/classifier/2.png) |
| 1000 | ![](/results/hdim1000/images/FF/normalizedPCA/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/FF/normalizedPCA/epoch60/0/classifier/2.png) | ![](/results/hdim1000/images/FF/normalizedPCA/epoch99/0/classifier/2.png) |

-----------------------------

#### **Standard PCA**
Here the layer is clean and untouched for plotting using PCA.

##### **layer 0**
| hdim | epoch0 | epoch60  | epoch99 |
|:----:|:------: |:-------:|:-------:|
| 256  | ![](/results/hdim256/images/FF/PCA/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/FF/PCA/epoch60/0/classifier/0.png) |![](/results/hdim256/images/FF/PCA/epoch99/0/classifier/0.png) |
| 512  | ![](/results/hdim512/images/FF/PCA/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/FF/PCA/epoch60/0/classifier/0.png) | ![](/results/hdim512/images/FF/PCA/epoch99/0/classifier/0.png) |
| 1000 | ![](/results/hdim1000/images/FF/PCA/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/FF/PCA/epoch60/0/classifier/0.png) | ![](/results/hdim1000/images/FF/PCA/epoch99/0/classifier/0.png) |

##### **layer 1**
| hdim | epoch0 | epoch60  | epoch99 |
|:----:|:------: |:-------:|:-------:|
| 256  | ![](/results/hdim256/images/FF/PCA/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/FF/PCA/epoch60/0/classifier/1.png) |![](/results/hdim256/images/FF/PCA/epoch99/0/classifier/1.png) |
| 512  | ![](/results/hdim512/images/FF/PCA/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/FF/PCA/epoch60/0/classifier/1.png) | ![](/results/hdim512/images/FF/PCA/epoch99/0/classifier/1.png) |
| 1000 | ![](/results/hdim1000/images/FF/PCA/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/FF/PCA/epoch60/0/classifier/1.png) | ![](/results/hdim1000/images/FF/PCA/epoch99/0/classifier/1.png) |

##### **layer 2**
| hdim | epoch0 | epoch60  | epoch99 |
|:----:|:------: |:-------:|:-------:|
| 256  | ![](/results/hdim256/images/FF/PCA/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/FF/PCA/epoch60/0/classifier/2.png) |![](/results/hdim256/images/FF/PCA/epoch99/0/classifier/2.png) |
| 512  | ![](/results/hdim512/images/FF/PCA/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/FF/PCA/epoch60/0/classifier/2.png) | ![](/results/hdim512/images/FF/PCA/epoch99/0/classifier/2.png) |
| 1000 | ![](/results/hdim1000/images/FF/PCA/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/FF/PCA/epoch60/0/classifier/2.png) | ![](/results/hdim1000/images/FF/PCA/epoch99/0/classifier/2.png) |




## <center>**1.4 PCA vs TSNE**</center>

### <center>**1.4.1 compare layer with itself in different epochs with PCA and TSNE**</center>
This is to compare how a layer evolves in comparison between PCA and TSNE

`batch of reference:0 `


### **Normalized**

#### layer 0
| hdim  | PCA or TSNE | epoch0 | epoch60 | epoch99 |
|:-----:|:-----------:|:------:|:-------:|:-------:|
|  256  |  PCA   | ![](/results/hdim256/images/FF/normalizedPCA/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/FF/normalizedPCA/epoch60/0/classifier/0.png) |![](/results/hdim256/images/FF/normalizedPCA/epoch99/0/classifier/0.png) |
|  256  |  TSNE  | ![](/results/hdim256/images/FF/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/FF/normalizedTSNE/epoch60/0/classifier/0.png) |![](/results/hdim256/images/FF/normalizedTSNE/epoch99/0/classifier/0.png) |
|  512  |  PCA   | ![](/results/hdim512/images/FF/normalizedPCA/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/FF/normalizedPCA/epoch60/0/classifier/0.png) |![](/results/hdim512/images/FF/normalizedPCA/epoch99/0/classifier/0.png) |
|  512  |  TSNE  | ![](/results/hdim512/images/FF/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/FF/normalizedTSNE/epoch60/0/classifier/0.png) |![](/results/hdim512/images/FF/normalizedTSNE/epoch99/0/classifier/0.png) |
| 1000  |  PCA   | ![](/results/hdim1000/images/FF/normalizedPCA/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/FF/normalizedPCA/epoch60/0/classifier/0.png) |![](/results/hdim1000/images/FF/normalizedPCA/epoch99/0/classifier/0.png) |
| 1000  |  TSNE  | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch60/0/classifier/0.png) |![](/results/hdim1000/images/FF/normalizedTSNE/epoch99/0/classifier/0.png) |


#### layer 1
| hdim  | PCA or TSNE | epoch0 | epoch60 | epoch99 |
|:-----:|:-----------:|:------:|:-------:|:-------:|
|  256  |  PCA   | ![](/results/hdim256/images/FF/normalizedPCA/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/FF/normalizedPCA/epoch60/0/classifier/1.png) |![](/results/hdim256/images/FF/normalizedPCA/epoch99/0/classifier/1.png) |
|  256  |  TSNE  | ![](/results/hdim256/images/FF/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/FF/normalizedTSNE/epoch60/0/classifier/1.png) |![](/results/hdim256/images/FF/normalizedTSNE/epoch99/0/classifier/1.png) |
|  512  |  PCA   | ![](/results/hdim512/images/FF/normalizedPCA/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/FF/normalizedPCA/epoch60/0/classifier/1.png) |![](/results/hdim512/images/FF/normalizedPCA/epoch99/0/classifier/1.png) |
|  512  |  TSNE  | ![](/results/hdim512/images/FF/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/FF/normalizedTSNE/epoch60/0/classifier/1.png) |![](/results/hdim512/images/FF/normalizedTSNE/epoch99/0/classifier/1.png) |
| 1000  |  PCA   | ![](/results/hdim1000/images/FF/normalizedPCA/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/FF/normalizedPCA/epoch60/0/classifier/1.png) |![](/results/hdim1000/images/FF/normalizedPCA/epoch99/0/classifier/1.png) |
| 1000  |  TSNE  | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/FF/normalizedTSNE/epoch60/0/classifier/1.png) |![](/results/hdim1000/images/FF/normalizedTSNE/epoch99/0/classifier/1.png) |


#### layer 2
| hdim  | PCA or TSNE | epoch0 | epoch60 | epoch99 |
|:-----:|:-----------:|:------:|:-------:|:-------:|
|  256  |  PCA   | ![](/results/hdim256/images/FF/normalizedPCA/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/FF/normalizedPCA/epoch60/0/classifier/2.png) |![](/results/hdim256/images/FF/normalizedPCA/epoch99/0/classifier/2.png) |
|  256  |  TSNE  | ![](/results/hdim256/images/FF/normalizedTSNE/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/FF/normalizedTSNE/epoch60/0/classifier/2.png) |![](/results/hdim256/images/FF/normalizedTSNE/epoch99/0/classifier/2.png) |
|  512  |  PCA   | ![](/results/hdim512/images/FF/normalizedPCA/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/FF/normalizedPCA/epoch60/0/classifier/2.png) |![](/results/hdim512/images/FF/normalizedPCA/epoch99/0/classifier/2.png) |
|  512  |  TSNE  | ![](/results/hdim512/images/FF/normalizedTSNE/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/FF/normalizedTSNE/epoch60/0/classifier/2.png) |![](/results/hdim512/images/FF/normalizedTSNE/epoch99/0/classifier/2.png) |
| 1000  |  PCA   | ![](/results/hdim1000/images/FF/normalizedPCA/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/FF/normalizedPCA/epoch60/0/classifier/2.png) |![](/results/hdim1000/images/FF/normalizedPCA/epoch99/0/classifier/2.png) |
| 1000  |  TSNE  | ![](/results/hdim1000/images/FF/TSNE/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/FF/TSNE/epoch60/0/classifier/2.png) |![](/results/hdim1000/images/FF/TSNE/epoch99/0/classifier/2.png) |


### **Standard**

#### layer 0
| hdim  | PCA or TSNE | epoch0 | epoch60 | epoch99 |
|:-----:|:-----------:|:------:|:-------:|:-------:|
|  256  |  PCA   | ![](/results/hdim256/images/FF/PCA/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/FF/PCA/epoch60/0/classifier/0.png) |![](/results/hdim256/images/FF/PCA/epoch99/0/classifier/0.png) |
|  256  |  TSNE  | ![](/results/hdim256/images/FF/TSNE/epoch0/0/classifier/0.png) | ![](/results/hdim256/images/FF/TSNE/epoch60/0/classifier/0.png) |![](/results/hdim256/images/FF/TSNE/epoch99/0/classifier/0.png) |
|  512  |  PCA   | ![](/results/hdim512/images/FF/PCA/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/FF/PCA/epoch60/0/classifier/0.png) |![](/results/hdim512/images/FF/PCA/epoch99/0/classifier/0.png) |
|  512  |  TSNE  | ![](/results/hdim512/images/FF/TSNE/epoch0/0/classifier/0.png) | ![](/results/hdim512/images/FF/TSNE/epoch60/0/classifier/0.png) |![](/results/hdim512/images/FF/TSNE/epoch99/0/classifier/0.png) |
| 1000  |  PCA   | ![](/results/hdim1000/images/FF/PCA/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/FF/PCA/epoch60/0/classifier/0.png) |![](/results/hdim1000/images/FF/PCA/epoch99/0/classifier/0.png) |
| 1000  |  TSNE  | ![](/results/hdim1000/images/FF/TSNE/epoch0/0/classifier/0.png) | ![](/results/hdim1000/images/FF/TSNE/epoch60/0/classifier/0.png) |![](/results/hdim1000/images/FF/TSNE/epoch99/0/classifier/0.png) |


#### layer 1
| hdim  | PCA or TSNE | epoch0 | epoch60 | epoch99 |
|:-----:|:-----------:|:------:|:-------:|:-------:|
|  256  |  PCA   | ![](/results/hdim256/images/FF/PCA/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/FF/PCA/epoch60/0/classifier/1.png) |![](/results/hdim256/images/FF/PCA/epoch99/0/classifier/1.png) |
|  256  |  TSNE  | ![](/results/hdim256/images/FF/TSNE/epoch0/0/classifier/1.png) | ![](/results/hdim256/images/FF/TSNE/epoch60/0/classifier/1.png) |![](/results/hdim256/images/FF/TSNE/epoch99/0/classifier/1.png) |
|  512  |  PCA   | ![](/results/hdim512/images/FF/PCA/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/FF/PCA/epoch60/0/classifier/1.png) |![](/results/hdim512/images/FF/PCA/epoch99/0/classifier/1.png) |
|  512  |  TSNE  | ![](/results/hdim512/images/FF/TSNE/epoch0/0/classifier/1.png) | ![](/results/hdim512/images/FF/TSNE/epoch60/0/classifier/1.png) |![](/results/hdim512/images/FF/TSNE/epoch99/0/classifier/1.png) |
| 1000  |  PCA   | ![](/results/hdim1000/images/FF/PCA/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/FF/PCA/epoch60/0/classifier/1.png) |![](/results/hdim1000/images/FF/PCA/epoch99/0/classifier/1.png) |
| 1000  |  TSNE  | ![](/results/hdim1000/images/FF/TSNE/epoch0/0/classifier/1.png) | ![](/results/hdim1000/images/FF/TSNE/epoch60/0/classifier/1.png) |![](/results/hdim1000/images/FF/TSNE/epoch99/0/classifier/1.png) |


#### layer 2
| hdim  | PCA or TSNE | epoch0 | epoch60 | epoch99 |
|:-----:|:-----------:|:------:|:-------:|:-------:|
|  256  |  PCA   | ![](/results/hdim256/images/FF/PCA/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/FF/PCA/epoch60/0/classifier/2.png) |![](/results/hdim256/images/FF/PCA/epoch99/0/classifier/2.png) |
|  256  |  TSNE  | ![](/results/hdim256/images/FF/TSNE/epoch0/0/classifier/2.png) | ![](/results/hdim256/images/FF/TSNE/epoch60/0/classifier/2.png) |![](/results/hdim256/images/FF/TSNE/epoch99/0/classifier/2.png) |
|  512  |  PCA   | ![](/results/hdim512/images/FF/PCA/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/FF/PCA/epoch60/0/classifier/2.png) |![](/results/hdim512/images/FF/PCA/epoch99/0/classifier/2.png) |
|  512  |  TSNE  | ![](/results/hdim512/images/FF/TSNE/epoch0/0/classifier/2.png) | ![](/results/hdim512/images/FF/TSNE/epoch60/0/classifier/2.png) |![](/results/hdim512/images/FF/TSNE/epoch99/0/classifier/2.png) |
| 1000  |  PCA   | ![](/results/hdim1000/images/FF/PCA/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/FF/PCA/epoch60/0/classifier/2.png) |![](/results/hdim1000/images/FF/PCA/epoch99/0/classifier/2.png) |
| 1000  |  TSNE  | ![](/results/hdim1000/images/FF/TSNE/epoch0/0/classifier/2.png) | ![](/results/hdim1000/images/FF/TSNE/epoch60/0/classifier/2.png) |![](/results/hdim1000/images/FF/TSNE/epoch99/0/classifier/2.png) |

----------------------------

# <center>**FF vs Backpropahation</center>