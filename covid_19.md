---
layout: page
title: Covid-19
logistic_curve: ./200404_corona.png
---

## Prediction of Cases in Germany

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
started by fitting a logistic curve, like described in this
[3Blue1Brown](https://www.youtube.com/watch?v=Kas0tIxDvrg&t=473s) youtube video, but now I
just use a exponential function (e^{kx}), because it doesn't matter if you are only
interested in the next day.

So, the following plot is just a curve fit with two parameters, for more scientific data
rely on the pro's:

* [Robert Koch Institut](https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/nCoV.html)
* [Johns Hopkins University](https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6)
* [Worldometer.info](https://www.worldometers.info/coronavirus/country/germany/)
* or, if you want to create your own simulation: [CovidSim](http://covidsim.eu).

![Logistic curve of corona virus progression]({{ page.logistic_curve }})

> *Remember:* All models are wrong. [George Box](https://en.wikipedia.org/wiki/All_models_are_wrong)