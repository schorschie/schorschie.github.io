---
layout: post
title: Abschluss Machine Learning Nano Degree
date:   2021-02-25 15:41:04 +0200
mathjax: false
categories: AI, machine, learning, udacity
ref: machine_learning
lang: de
---

Diese Woche habe ich den Udacity Nano-Degree "Machine Learning Engineer"
[bestanden](https://confirm.udacity.com/CGALRCZP).

## Zusammenfassung

Der Nano-Degree besteht grob aus drei Teilen.

Der erste Teil war ein Überblick über Prozesse in der Software-Entwicklung und
zum Abschluss wurde man ermuntert eine eigene Python Bibliothek zu schreiben und
auf [pip](https://pypi.org) zu veröffentlichen. Diesen Teil habe ich bereits in
Blog [beschrieben]({% post_url 2020-12-19-rki_scraper_de %}).

Der zweite Teil schult den Umgang mit [AWS](https://aws.amazon.com). Es werden
KI Modelle vorbereitet, trainiert und auf AWS implementiert.

Der dritte und letzte Teil besteht aus dem Abschlussprojekt, in welchem der
Student ermutigt wird sein eigenes "Maschine Learning" Modell aufzusetzen und in
einer Demo App zu implementieren. Ich habe mich für den von Udacity
unterstützten Weg zur automatischen Hunderassen-Erkennung entschieden.

## Abschlussprojekt Hunderassen-Erkennung

Hier ist ein Auszug aus dem
[Abschlussbericht](https://github.com/schorschie/udacity_dog_breed/blob/main/project_report.pdf)
zum Abschlussprojekt, dieser sowie das gesamte Projekt ist auf github
zugänglich.

In diesem Projekt wird das Wissen und die Verwendung von Convolutional Neural
Networks (CNN) [[1]](https://de.wikipedia.org/wiki/Convolutional_Neural_Network)
für das Udacity "Reviewer-Team" aufgezeigt. Im Rahmen dieses Projekts wird ein
CNN mit der Fähigkeit, Hunderassen mit einer Genauigkeit von mehr als 10% zu
erkennen, von Grund auf neu erstellt. Anschließend wird ein vorab trainiertes
VGG16 [[2]](https://pytorch.org/vision/0.8/models.html),
[[3]](https://arxiv.org/abs/1409.1556) angepasst, um dieselbe Aufgabe mit einer
Genauigkeit von mehr als 60% auszuführen.

Neben einem neuronalen Netz zur Erkennung von Hunderassen wird auch ein
vorhandenes neuronales OpenCV-Netz [[4]](https://opencv.org/) zur
Gesichtserkennung wiederverwertet. Der Algorithmus erzeugt einen
Begrenzungsrahmen für jedes Gesicht, das in einem Bild gefunden wird.

Beide Algorithmen, die OpenCV-Gesichtserkennung und die
VGG16-Hunderassenerkennung, werden zu einer Demo-App kombiniert, die in einem
beliebigen Bild eine Aussage über die am wahrscheinlichsten abgebildete
Hunderasse trifft.

Wenn der Demo-App ein Bild eines Menschen bereitgestellt wird,
soll die App einen Menschen identifizieren, aber dennoch eine Aussage über
eine am ähnlichsten aussehende Hunderasse treffen.

**[1]** [Convolutional Neural Network (CNN)](https://de.wikipedia.org/wiki/Convolutional_Neural_Network)  
**[2]** [PyTorch Models](https://pytorch.org/vision/0.8/models.html)  
**[3]** [Very Deep Convolutional Networks for Large-Scale Image
Recognition](https://arxiv.org/abs/1409.1556)  
**[4]** [Open Computer Vision](https://opencv.org/})  
