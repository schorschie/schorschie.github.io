---
layout: post
title: Passed Machine Learning Nano Degree
date:   2021-02-25 15:41:04 +0200
mathjax: false
categories: AI, machine, learning, udacity
ref: machine_learning
lang: en
---

This week I [graduated](https://confirm.udacity.com/CGALRCZP) the Udacity
Machine Learning Nanodegree.

## Overview

The Nano-Degree can be roughly divided into three parts. The first part was
general software development in which I was encouraged to create some random
[pip](https://pypi.org) library, which I did already describe in the previous
[post]({% post_url 2020-12-19-rki_scraper %}).

The second part mostly consisted out of preparing, training and implementing
models on the [AWS](https://aws.amazon.com).

The final part is the capstone project in which the student is encouraged to
develop a own machine learning model. Here I choose the Udacity supported "dog
breed identification".

## Capstone Project Dog Breed Identification

Here is the abstract of the [project
report](https://github.com/schorschie/udacity_dog_breed/blob/main/project_report.pdf),
which is hosted alongside the project on github.

In this project the knowledge and usage of Convolutional Neural Networks (CNN)
[[1]](https://en.wikipedia.org/wiki/Convolutional_neural_network) is
demonstrated for the Udacity reviewer team. Within this project a CNN with the
ability to detect dog breeds with an accuracy of more than 10% is created from
scratch. Afterwards a pre-trained VGG16
[[2]](https://pytorch.org/vision/0.8/models.html),
[[3]](https://arxiv.org/abs/1409.1556) is adapted to perform the same
task with an accuracy of >60%.

Besides a neural net for dog breed detection, also an existing OpenCV
[[4]](https://opencv.org/) neural net for face recognition is adapted. The
algorithm provides a bounding box for each face it found within a picture.

Both algorithms, the OpenCV face recognition and the VGG16 dog breed detection
are combined into an demo app, that can take an arbitrary picture and return a
statement of a most likely dog breed. If a picture of a human is provided, the
app should identify a human, but still provide a statement of a most similar
looking dog breed.

**[1]** [Convolutional Neural Network (CNN)](https://en.wikipedia.org/wiki/Convolutional_neural_network)  
**[2]** [PyTorch Models](https://pytorch.org/vision/0.8/models.html)  
**[3]** [Very Deep Convolutional Networks for Large-Scale Image
Recognition](https://arxiv.org/abs/1409.1556)  
**[4]** [Open Computer Vision](https://opencv.org/})  
