---
layout: post
title: Covid-19 Update
date:   2020-07-06 19:53:40 +0200
mathjax: true
categories: Corona, Covid-19, update
images:
  - path: /assets/images/200706_germany.png
    title: Deutschland
  - path: /assets/images/200706_bw.png
    title: Baden-Württemberg
  - path: /assets/images/200706_oak.png
    title: Ostalbkreis
ref: Covid-19_update
lang: en
---

## Prediction for {{ page.date | date: "%s" | plus: 86400 | date_to_string: "ordinal" }}

{% include image-gallery3.html %}

{: .right}
[(csv)](/covid-19_germany.csv)

> *Remember:* All models are wrong. [George Box](https://en.wikipedia.org/wiki/All_models_are_wrong)

## Background

I'm trying to predict the amount of infected people in Germany for the next day. I had
difficulties with the crazy increasing numbers in Italy and later in Germany. I know it is
in the nature of many people like me, having problems imagining exponential growth. (I
believe older generations, who used a slide ruler instead of a calculated may be in benefit
here.)

So for me it was a relief to see, that the numbers aren't behaving crazy, but just as
expected.

## Disclaimer

The data is from the daily [RKI
Report](https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html). I
fit a exponential function \\(e^{k(x-x_0)}\\) for the last week of the time span.

So, the following plot is just a curve fit with two parameters, for more scientific data
rely on the pro's:

* [Robert Koch Institut](https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/nCoV.html)
* [Johns Hopkins University](https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6)
* [Worldometer.info](https://www.worldometers.info/coronavirus/country/germany/)
* or, if you want to create your own simulation: [CovidSim](http://covidsim.eu).

{% include image-lightbox.html %}
