## Atlas Human Protein Classification
This project is an attempt to solve a kaggle challenge named the same. The original dataset is present [here](https://www.kaggle.com/c/human-protein-atlas-image-classification/data)


### Motivation

This project is aimed at the use of CNNs in Bio-Medical images for object detection purposes.
Proteins are “the doers” in the human cell, executing many functions that together enable life. Historically, classification of proteins has been limited to single patterns in one or a few cell types, but in order to fully understand the complexity of the human cell, models must classify mixed patterns across a range of different human cells.
Images visualizing proteins in cells are commonly used for biomedical research, and these cells could hold the key for the next breakthrough in medicine. However, thanks to advances in high-throughput microscopy, these images are generated at a far greater pace than what can be manually evaluated. Therefore, the need is greater than ever for automating biomedical image analysis to accelerate the understanding of human cells and disease.


## Framework used
 - Keras
 - Numpy
 - skImage
 - cv2


## What am I looking at?

You are looking at a repository aimed at classification of cell bodies present in images. First, there is an analysis of the dataset. Then I have used transfer learning on pretrained networks to build a classifier. This repository contains such experiments and discusses the results/output analysing the differences in performance from one change to another.

This is my first attempt at both transfer learning and bio-medical image analysis. I am trying to provide a code base that is not too complex and would also provide jupyter notebook for better visualization. I would welcome any correction and criticism as this is the main aim of this activity.

## Credits
Credit goes to kaggle for providing computational resources and the organisers of [Human Protein Classification Challenge](https://www.kaggle.com/c/human-protein-atlas-image-classification/data) for providing an amazing dataset. Credit is also due to individual kagglers for providing guidance and further resources.
