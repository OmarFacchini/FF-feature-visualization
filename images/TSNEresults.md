# **results obtained**

here are shown the images obtained from the TSNE for both forward-forward and standard backpropagation approach.

<!--
## **Forward-froward results**

there will be 3 sets of results:
1. layer-layer comparison for classifier in standard and normalized TSNE
2. layer-layer comparison for each layer
3. layer compared with itself in different epochs



### **layer-layer comparison for classifier in standard and normalized TSNE**
`epoch of reference: 0`
| layer-batch | normalized TSNE            |  standard TSNE |
:------:|:-------------------------:|:-------------------------:
0 - 0 |  ![](/images/FF/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/images/FF/TSNE/epoch0/0/classifier/0.png) | 
1 - 0 |  ![](/images/FF/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/images/FF/TSNE/epoch0/0/classifier/1.png) |
2 - 0 |  ![](/images/FF/normalizedTSNE/epoch0/0/classifier/2.png) | ![](/images/FF/TSNE/epoch0/0/classifier/2.png) |
0 - 200 |  ![](/images/FF/normalizedTSNE/epoch0/200/classifier/0.png) | ![](/images/FF/TSNE/epoch0/200/classifier/0.png) | 
1 - 200 |  ![](/images/FF/normalizedTSNE/epoch0/200/classifier/1.png) | ![](/images/FF/TSNE/epoch0/200/classifier/1.png) |
2 - 200 |  ![](/images/FF/normalizedTSNE/epoch0/200/classifier/2.png) | ![](/images/FF/TSNE/epoch0/200/classifier/2.png) |
0 - 400 |  ![](/images/FF/normalizedTSNE/epoch0/400/classifier/0.png) | ![](/images/FF/TSNE/epoch0/400/classifier/0.png) | 
1 - 400 |  ![](/images/FF/normalizedTSNE/epoch0/400/classifier/1.png) | ![](/images/FF/TSNE/epoch0/400/classifier/1.png) |
2 - 400 |  ![](/images/FF/normalizedTSNE/epoch0/400/classifier/2.png) | ![](/images/FF/TSNE/epoch0/400/classifier/2.png) |

`epoch of reference: 60`
| layer-batch | normalized TSNE            |  standard TSNE |
:------:|:-------------------------:|:-------------------------:
0 - 0 |  ![](/images/FF/normalizedTSNE/epoch60/0/classifier/0.png) | ![](/images/FF/TSNE/epoch60/0/classifier/0.png) | 
1 - 0 |  ![](/images/FF/normalizedTSNE/epoch60/0/classifier/1.png) | ![](/images/FF/TSNE/epoch60/0/classifier/1.png) |
2 - 0 |  ![](/images/FF/normalizedTSNE/epoch60/0/classifier/2.png) | ![](/images/FF/TSNE/epoch60/0/classifier/2.png) |
0 - 200 |  ![](/images/FF/normalizedTSNE/epoch60/200/classifier/0.png) | ![](/images/FF/TSNE/epoch60/200/classifier/0.png) | 
1 - 200 |  ![](/images/FF/normalizedTSNE/epoch60/200/classifier/1.png) | ![](/images/FF/TSNE/epoch60/200/classifier/1.png) |
2 - 200 |  ![](/images/FF/normalizedTSNE/epoch60/200/classifier/2.png) | ![](/images/FF/TSNE/epoch60/200/classifier/2.png) |
0 - 400 |  ![](/images/FF/normalizedTSNE/epoch60/400/classifier/0.png) | ![](/images/FF/TSNE/epoch60/400/classifier/0.png) | 
1 - 400 |  ![](/images/FF/normalizedTSNE/epoch60/400/classifier/1.png) | ![](/images/FF/TSNE/epoch60/400/classifier/1.png) |
2 - 400 |  ![](/images/FF/normalizedTSNE/epoch60/400/classifier/2.png) | ![](/images/FF/TSNE/epoch60/400/classifier/2.png) |

`epoch of reference: 99`
| layer-batch | normalized TSNE            |  standard TSNE |
:------:|:-------------------------:|:-------------------------:
0 - 0 |  ![](/images/FF/normalizedTSNE/epoch99/0/classifier/0.png) | ![](/images/FF/TSNE/epoch99/0/classifier/0.png) | 
1 - 0 |  ![](/images/FF/normalizedTSNE/epoch99/0/classifier/1.png) | ![](/images/FF/TSNE/epoch99/0/classifier/1.png) |
2 - 0 |  ![](/images/FF/normalizedTSNE/epoch99/0/classifier/2.png) | ![](/images/FF/TSNE/epoch99/0/classifier/2.png) |
0 - 200 |  ![](/images/FF/normalizedTSNE/epoch99/200/classifier/0.png) | ![](/images/FF/TSNE/epoch99/200/classifier/0.png) | 
1 - 200 |  ![](/images/FF/normalizedTSNE/epoch99/200/classifier/1.png) | ![](/images/FF/TSNE/epoch99/200/classifier/1.png) |
2 - 200 |  ![](/images/FF/normalizedTSNE/epoch99/200/classifier/2.png) | ![](/images/FF/TSNE/epoch99/200/classifier/2.png) |
0 - 400 |  ![](/images/FF/normalizedTSNE/epoch99/400/classifier/0.png) | ![](/images/FF/TSNE/epoch99/400/classifier/0.png) | 
1 - 400 |  ![](/images/FF/normalizedTSNE/epoch99/400/classifier/1.png) | ![](/images/FF/TSNE/epoch99/400/classifier/1.png) |
2 - 400 |  ![](/images/FF/normalizedTSNE/epoch99/400/classifier/2.png) | ![](/images/FF/TSNE/epoch99/400/classifier/2.png) |

## layer-layer comparison for each layer for classifier

`batch of reference:0 `

will keep the batch fixed for this comparison
### **Normalized TSNE**

`epoch of reference: 0`

| layer0 | layer1  | layer2 |
:------: |:--------:|:------:
![](/images/FF/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/images/FF/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/images/FF/normalizedTSNE/epoch0/0/classifier/2.png) |

`epoch of reference: 60`


| layer0 | layer1  | layer2 |
:------: |:--------:|:------:
![](/images/FF/normalizedTSNE/epoch60/0/classifier/0.png) | ![](/images/FF/normalizedTSNE/epoch60/0/classifier/1.png) | ![](/images/FF/normalizedTSNE/epoch60/0/classifier/2.png) |

`epoch of reference: 99`


| layer0 | layer1  | layer2 |
:------: |:--------:|:------:
![](/images/FF/normalizedTSNE/epoch99/0/classifier/0.png) | ![](/images/FF/normalizedTSNE/epoch99/0/classifier/1.png) | ![](/images/FF/normalizedTSNE/epoch99/0/classifier/2.png) |

### **standard TSNE**

`epoch of reference: 0`

| layer0 | layer1  | layer2 |
:------: |:--------:|:------:
![](/images/FF/TSNE/epoch0/0/classifier/0.png) | ![](/images/FF/TSNE/epoch0/0/classifier/1.png) | ![](/images/FF/TSNE/epoch0/0/classifier/2.png) |

`epoch of reference: 60`


| layer0 | layer1  | layer2 |
:------: |:--------:|:------:
![](/images/FF/TSNE/epoch60/0/classifier/0.png) | ![](/images/FF/TSNE/epoch60/0/classifier/1.png) | ![](/images/FF/TSNE/epoch60/0/classifier/2.png) |

`epoch of reference: 99`


| layer0 | layer1  | layer2 |
:------: |:--------:|:------:
![](/images/FF/TSNE/epoch99/0/classifier/0.png) | ![](/images/FF/TSNE/epoch99/0/classifier/1.png) | ![](/images/FF/TSNE/epoch99/0/classifier/2.png) |


## **layer compared with itself in different epochs**

`batch of reference:0 `

will keep the batch fixed for this comparison
### layer 0 
| epoch | normalized TSNE            |  standard TSNE |
:------:|:-------------------------:|:-------------------------:
0       | ![](/images/FF/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/images/FF/TSNE/epoch0/0/classifier/0.png) |
60       | ![](/images/FF/normalizedTSNE/epoch60/0/classifier/0.png) | ![](/images/FF/TSNE/epoch60/0/classifier/0.png) |
99       | ![](/images/FF/normalizedTSNE/epoch99/0/classifier/0.png) | ![](/images/FF/TSNE/epoch99/0/classifier/0.png) |

### layer 1
| epoch | normalized TSNE            |  standard TSNE |
:------:|:-------------------------:|:-------------------------:
0       | ![](/images/FF/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/images/FF/TSNE/epoch0/0/classifier/1.png) |
60       | ![](/images/FF/normalizedTSNE/epoch60/0/classifier/1.png) | ![](/images/FF/TSNE/epoch60/0/classifier/1.png) |
99       | ![](/images/FF/normalizedTSNE/epoch99/0/classifier/1.png) | ![](/images/FF/TSNE/epoch99/0/classifier/1.png) |


### layer 2
| epoch | normalized TSNE            |  standard TSNE |
:------:|:-------------------------:|:-------------------------:
0       | ![](/images/FF/normalizedTSNE/epoch0/0/classifier/2.png) | ![](/images/FF/TSNE/epoch0/0/classifier/2.png) |
60       | ![](/images/FF/normalizedTSNE/epoch60/0/classifier/2.png) | ![](/images/FF/TSNE/epoch60/0/classifier/2.png) |
99       | ![](/images/FF/normalizedTSNE/epoch99/0/classifier/2.png) | ![](/images/FF/TSNE/epoch99/0/classifier/2.png) |


-->
-----------------------------------------------------------------------

## **backpropagation results**
same as just seen for the forward-forward

### **layer-layer comparison for classifier in standard and normalized TSNE**
`epoch of reference: 0`
| layer-batch | normalized TSNE            |  standard TSNE |
:------:|:-------------------------:|:-------------------------:
0 - 0 |  ![](/images/backprop/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/images/backprop/TSNE/epoch0/0/classifier/0.png) |
1 - 0 |  ![](/images/backprop/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/images/backprop/TSNE/epoch0/0/classifier/1.png) |
2 - 0 |  ![](/images/backprop/normalizedTSNE/epoch0/0/classifier/2.png) | ![](/images/backprop/TSNE/epoch0/0/classifier/2.png) |
0 - 200 |  ![](/images/backprop/normalizedTSNE/epoch0/200/classifier/0.png) | ![](/images/backprop/TSNE/epoch0/200/classifier/0.png) | 
1 - 200 |  ![](/images/backprop/normalizedTSNE/epoch0/200/classifier/1.png) | ![](/images/backprop/TSNE/epoch0/200/classifier/1.png) |
2 - 200 |  ![](/images/backprop/normalizedTSNE/epoch0/200/classifier/2.png) | ![](/images/backprop/TSNE/epoch0/200/classifier/2.png) |
0 - 400 |  ![](/images/backprop/normalizedTSNE/epoch0/400/classifier/0.png) | ![](/images/backprop/TSNE/epoch0/400/classifier/0.png) | 
1 - 400 |  ![](/images/backprop/normalizedTSNE/epoch0/400/classifier/1.png) | ![](/images/backprop/TSNE/epoch0/400/classifier/1.png) |
2 - 400 |  ![](/images/backprop/normalizedTSNE/epoch0/400/classifier/2.png) | ![](/images/backprop/TSNE/epoch0/400/classifier/2.png) |

`epoch of reference: 60`
| layer-batch | normalized TSNE            |  standard TSNE |
:------:|:-------------------------:|:-------------------------:
0 - 0 |  ![](/images/backprop/normalizedTSNE/epoch60/0/classifier/0.png) | ![](/images/backprop/TSNE/epoch60/0/classifier/0.png) | 
1 - 0 |  ![](/images/backprop/normalizedTSNE/epoch60/0/classifier/1.png) | ![](/images/backprop/TSNE/epoch60/0/classifier/1.png) |
2 - 0 |  ![](/images/backprop/normalizedTSNE/epoch60/0/classifier/2.png) | ![](/images/backprop/TSNE/epoch60/0/classifier/2.png) |
0 - 200 |  ![](/images/backprop/normalizedTSNE/epoch60/200/classifier/0.png) | ![](/images/backprop/TSNE/epoch60/200/classifier/0.png) | 
1 - 200 |  ![](/images/backprop/normalizedTSNE/epoch60/200/classifier/1.png) | ![](/images/backprop/TSNE/epoch60/200/classifier/1.png) |
2 - 200 |  ![](/images/backprop/normalizedTSNE/epoch60/200/classifier/2.png) | ![](/images/backprop/TSNE/epoch60/200/classifier/2.png) |
0 - 400 |  ![](/images/backprop/normalizedTSNE/epoch60/400/classifier/0.png) | ![](/images/backprop/TSNE/epoch60/400/classifier/0.png) | 
1 - 400 |  ![](/images/backprop/normalizedTSNE/epoch60/400/classifier/1.png) | ![](/images/backprop/TSNE/epoch60/400/classifier/1.png) |
2 - 400 |  ![](/images/backprop/normalizedTSNE/epoch60/400/classifier/2.png) | ![](/images/backprop/TSNE/epoch60/400/classifier/2.png) |

`epoch of reference: 99`
| layer-batch | normalized TSNE            |  standard TSNE |
:------:|:-------------------------:|:-------------------------:
0 - 0 |  ![](/images/backprop/normalizedTSNE/epoch99/0/classifier/0.png) | ![](/images/backprop/TSNE/epoch99/0/classifier/0.png) | 
1 - 0 |  ![](/images/backprop/normalizedTSNE/epoch99/0/classifier/1.png) | ![](/images/backprop/TSNE/epoch99/0/classifier/1.png) |
2 - 0 |  ![](/images/backprop/normalizedTSNE/epoch99/0/classifier/2.png) | ![](/images/backprop/TSNE/epoch99/0/classifier/2.png) |
0 - 200 |  ![](/images/backprop/normalizedTSNE/epoch99/200/classifier/0.png) | ![](/images/backprop/TSNE/epoch99/200/classifier/0.png) | 
1 - 200 |  ![](/images/backprop/normalizedTSNE/epoch99/200/classifier/1.png) | ![](/images/backprop/TSNE/epoch99/200/classifier/1.png) |
2 - 200 |  ![](/images/backprop/normalizedTSNE/epoch99/200/classifier/2.png) | ![](/images/backprop/TSNE/epoch99/200/classifier/2.png) |
0 - 400 |  ![](/images/backprop/normalizedTSNE/epoch99/400/classifier/0.png) | ![](/images/backprop/TSNE/epoch99/400/classifier/0.png) | 
1 - 400 |  ![](/images/backprop/normalizedTSNE/epoch99/400/classifier/1.png) | ![](/images/backprop/TSNE/epoch99/400/classifier/1.png) |
2 - 400 |  ![](/images/backprop/normalizedTSNE/epoch99/400/classifier/2.png) | ![](/images/backprop/TSNE/epoch99/400/classifier/2.png) |

## layer-layer comparison for each layer for classifier
`batch of reference:0 `

will keep the batch fixed for this comparison
### **Normalized TSNE**

`epoch of reference: 0`

| layer0 | layer1  | layer2 |
:------: |:--------:|:------:
![](/images/backprop/normalizedTSNE/epoch0/0/classifier/0.png) | ![](/images/backprop/normalizedTSNE/epoch0/0/classifier/1.png) | ![](/images/backprop/normalizedTSNE/epoch0/0/classifier/2.png) |

`epoch of reference: 60`

| layer0 | layer1  | layer2 |
:------: |:--------:|:------:
![](/images/backprop/normalizedTSNE/epoch60/0/classifier/0.png) | ![](/images/backprop/normalizedTSNE/epoch60/0/classifier/1.png) | ![](/images/backprop/normalizedTSNE/epoch60/0/classifier/2.png) |

`epoch of reference: 99`

| layer0 | layer1  | layer2 |
:------: |:--------:|:------:
![](/images/backprop/normalizedTSNE/epoch99/0/classifier/0.png) | ![](/images/backprop/normalizedTSNE/epoch99/0/classifier/1.png) | ![](/images/backprop/normalizedTSNE/epoch99/0/classifier/2.png) |

### **standard TSNE**
`epoch of reference: 0`

| layer0 | layer1  | layer2 |
:------: |:--------:|:------:
![](/images/backprop/TSNE/epoch0/0/classifier/0.png) | ![](/images/backprop/TSNE/epoch0/0/classifier/1.png) | ![](/images/backprop/TSNE/epoch0/0/classifier/2.png) |

`epoch of reference: 60`

| layer0 | layer1  | layer2 |
:------: |:--------:|:------:
![](/images/backprop/TSNE/epoch60/0/classifier/0.png) | ![](/images/backprop/TSNE/epoch60/0/classifier/1.png) | ![](/images/backprop/TSNE/epoch60/0/classifier/2.png) |

`epoch of reference: 99`

| layer0 | layer1  | layer2 |
:------: |:--------:|:------:
![](/images/backprop/TSNE/epoch99/0/classifier/0.png) | ![](/images/backprop/TSNE/epoch99/0/classifier/1.png) | ![](/images/backprop/TSNE/epoch99/0/classifier/2.png) |

## **layer compared with itself in different epochs**
`batch of reference:0 `

will keep the batch fixed for this comparison

### layer 0 
| epoch | normalized TSNE            |  standard TSNE |
:------:|:-------------------------:|:-------------------------:
0       | ![](/images/backprop/normalizedTSNE/epoch0/0/classifier/0.png)  | ![](/images/backprop/TSNE/epoch0/0/classifier/0.png)  |
60      | ![](/images/backprop/normalizedTSNE/epoch60/0/classifier/0.png) | ![](/images/backprop/TSNE/epoch60/0/classifier/0.png) |
99      | ![](/images/backprop/normalizedTSNE/epoch99/0/classifier/0.png) | ![](/images/backprop/TSNE/epoch99/0/classifier/0.png) |

### layer 1 
| epoch | normalized TSNE            |  standard TSNE |
:------:|:-------------------------:|:-------------------------:
0       | ![](/images/backprop/normalizedTSNE/epoch0/0/classifier/1.png)  | ![](/images/backprop/TSNE/epoch0/0/classifier/1.png)  |
60      | ![](/images/backprop/normalizedTSNE/epoch60/0/classifier/1.png) | ![](/images/backprop/TSNE/epoch60/0/classifier/1.png) |
99      | ![](/images/backprop/normalizedTSNE/epoch99/0/classifier/1.png) | ![](/images/backprop/TSNE/epoch99/0/classifier/1.png) |

### layer 2 
| epoch | normalized TSNE            |  standard TSNE |
:------:|:-------------------------:|:-------------------------:
0       | ![](/images/backprop/normalizedTSNE/epoch0/0/classifier/2.png)  | ![](/images/backprop/TSNE/epoch0/0/classifier/2.png)  |
60      | ![](/images/backprop/normalizedTSNE/epoch60/0/classifier/2.png) | ![](/images/backprop/TSNE/epoch60/0/classifier/2.png) |
99      | ![](/images/backprop/normalizedTSNE/epoch99/0/classifier/2.png) | ![](/images/backprop/TSNE/epoch99/0/classifier/2.png) |



----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# test to check if TSNE is actually doing clustering

## standard TSNE classifier

### layer 0

| epoch | TSNE applied            |  pre-TSNE |
:------:|:-------------------------:|:-------------------------:
0       | ![](/images/backprop/TSNE/epoch0/0/classifier/0.png)  | ![](/images/backpropTest/TSNE/epoch0/0/classifier/0.png)  |
60      | ![](/images/backprop/TSNE/epoch60/0/classifier/0.png) | ![](/images/backpropTest/TSNE/epoch60/0/classifier/0.png) |
99      | ![](/images/backprop/TSNE/epoch99/0/classifier/0.png) | ![](/images/backpropTest/TSNE/epoch99/0/classifier/0.png) |

### layer 1

| epoch | TSNE applied            |  pre-TSNE |
:------:|:-------------------------:|:-------------------------:
0       | ![](/images/backprop/TSNE/epoch0/0/classifier/1.png)  | ![](/images/backpropTest/TSNE/epoch0/0/classifier/1.png)  |
60      | ![](/images/backprop/TSNE/epoch60/0/classifier/1.png) | ![](/images/backpropTest/TSNE/epoch60/0/classifier/1.png) |
99      | ![](/images/backprop/TSNE/epoch99/0/classifier/1.png) | ![](/images/backpropTest/TSNE/epoch99/0/classifier/1.png) |

### layer 2

| epoch | TSNE applied            |  pre-TSNE |
:------:|:-------------------------:|:-------------------------:
0       | ![](/images/backprop/TSNE/epoch0/0/classifier/2.png)  | ![](/images/backpropTest/TSNE/epoch0/0/classifier/2.png)  |
60      | ![](/images/backprop/TSNE/epoch60/0/classifier/2.png) | ![](/images/backpropTest/TSNE/epoch60/0/classifier/2.png) |
99      | ![](/images/backprop/TSNE/epoch99/0/classifier/2.png) | ![](/images/backpropTest/TSNE/epoch99/0/classifier/2.png) |

## normalized TSNE classifier

### layer 0

| epoch | TSNE applied            |  pre-TSNE |
:------:|:-------------------------:|:-------------------------:
0       | ![](/images/backprop/normalizedTSNE/epoch0/0/classifier/0.png)  | ![](/images/backpropTest/normalizedTSNE/epoch0/0/classifier/0.png)  |
60      | ![](/images/backprop/normalizedTSNE/epoch60/0/classifier/0.png) | ![](/images/backpropTest/normalizedTSNE/epoch60/0/classifier/0.png) |
99      | ![](/images/backprop/normalizedTSNE/epoch99/0/classifier/0.png) | ![](/images/backpropTest/normalizedTSNE/epoch99/0/classifier/0.png) |

### layer 1

| epoch | TSNE applied            |  pre-TSNE |
:------:|:-------------------------:|:-------------------------:
0       | ![](/images/backprop/normalizedTSNE/epoch0/0/classifier/1.png)  | ![](/images/backpropTest/normalizedTSNE/epoch0/0/classifier/1.png)  |
60      | ![](/images/backprop/normalizedTSNE/epoch60/0/classifier/1.png) | ![](/images/backpropTest/normalizedTSNE/epoch60/0/classifier/1.png) |
99      | ![](/images/backprop/normalizedTSNE/epoch99/0/classifier/1.png) | ![](/images/backpropTest/normalizedTSNE/epoch99/0/classifier/1.png) |

### layer 2

| epoch | TSNE applied            |  pre-TSNE |
:------:|:-------------------------:|:-------------------------:
0       | ![](/images/backprop/normalizedTSNE/epoch0/0/classifier/2.png)  | ![](/images/backpropTest/normalizedTSNE/epoch0/0/classifier/2.png)  |
60      | ![](/images/backprop/normalizedTSNE/epoch60/0/classifier/2.png) | ![](/images/backpropTest/normalizedTSNE/epoch60/0/classifier/2.png) |
99      | ![](/images/backprop/normalizedTSNE/epoch99/0/classifier/2.png) | ![](/images/backpropTest/normalizedTSNE/epoch99/0/classifier/2.png) |



## standard TSNE normal 

### layer 0

| epoch | TSNE applied            |  pre-TSNE |
:------:|:-------------------------:|:-------------------------:
0       | ![](/images/backprop/TSNE/epoch0/0/0.png)  | ![](/images/backpropTest/TSNE/epoch0/0/0.png)  |
60      | ![](/images/backprop/TSNE/epoch60/0/0.png) | ![](/images/backpropTest/TSNE/epoch60/0/0.png) |
99      | ![](/images/backprop/TSNE/epoch99/0/0.png) | ![](/images/backpropTest/TSNE/epoch99/0/0.png) |

### layer 1

| epoch | TSNE applied            |  pre-TSNE |
:------:|:-------------------------:|:-------------------------:
0       | ![](/images/backprop/TSNE/epoch0/0/1.png)  | ![](/images/backpropTest/TSNE/epoch0/0/1.png)  |
60      | ![](/images/backprop/TSNE/epoch60/0/1.png) | ![](/images/backpropTest/TSNE/epoch60/0/1.png) |
99      | ![](/images/backprop/TSNE/epoch99/0/1.png) | ![](/images/backpropTest/TSNE/epoch99/0/1.png) |

### layer 2

| epoch | TSNE applied            |  pre-TSNE |
:------:|:-------------------------:|:-------------------------:
0       | ![](/images/backprop/TSNE/epoch0/0/2.png)  | ![](/images/backpropTest/TSNE/epoch0/0/2.png)  |
60      | ![](/images/backprop/TSNE/epoch60/0/2.png) | ![](/images/backpropTest/TSNE/epoch60/0/2.png) |
99      | ![](/images/backprop/TSNE/epoch99/0/2.png) | ![](/images/backpropTest/TSNE/epoch99/0/2.png) |



## normalized TSNE normal

### layer 0

| epoch | TSNE applied            |  pre-TSNE |
:------:|:-------------------------:|:-------------------------:
0       | ![](/images/backprop/normalizedTSNE/epoch0/0/0.png)  | ![](/images/backpropTest/normalizedTSNE/epoch0/0/0.png)  |
60      | ![](/images/backprop/normalizedTSNE/epoch60/0/0.png) | ![](/images/backpropTest/normalizedTSNE/epoch60/0/0.png) |
99      | ![](/images/backprop/normalizedTSNE/epoch99/0/0.png) | ![](/images/backpropTest/normalizedTSNE/epoch99/0/0.png) |

### layer 1

| epoch | TSNE applied            |  pre-TSNE |
:------:|:-------------------------:|:-------------------------:
0       | ![](/images/backprop/normalizedTSNE/epoch0/0/1.png)  | ![](/images/backpropTest/normalizedTSNE/epoch0/0/1.png)  |
60      | ![](/images/backprop/normalizedTSNE/epoch60/0/1.png) | ![](/images/backpropTest/normalizedTSNE/epoch60/0/1.png) |
99      | ![](/images/backprop/normalizedTSNE/epoch99/0/1.png) | ![](/images/backpropTest/normalizedTSNE/epoch99/0/1.png) |

### layer 2

| epoch | TSNE applied            |  pre-TSNE |
:------:|:-------------------------:|:-------------------------:
0       | ![](/images/backprop/normalizedTSNE/epoch0/0/2.png)  | ![](/images/backpropTest/normalizedTSNE/epoch0/0/2.png)  |
60      | ![](/images/backprop/normalizedTSNE/epoch60/0/2.png) | ![](/images/backpropTest/normalizedTSNE/epoch60/0/2.png) |
99      | ![](/images/backprop/normalizedTSNE/epoch99/0/2.png) | ![](/images/backpropTest/normalizedTSNE/epoch99/0/2.png) |