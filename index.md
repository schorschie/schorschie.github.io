---
layout: home
title: Covid-19 Cases in Germany
logistic_curve: ./200403_corona.png
---

## Prediction

I'm trying to predict the amount of hospital treatment needed to deal with the corona crisis in
Germany, so that people understand, why this drastic measures are necessary. I hope we will se a decrease of the
curve in the near future.

I do not do this to stress you, but to *increase the understanding* for the drastic measures taken now
by the German goverment.

## Disclaimer

The numbers are from the daily [RKI Report](https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html).

In the first step I fit a logistic curve to the current progression of infected cases and a
maximum value of 70% of the population in Germany. The idea to use a logistic curve came from this
[3Blue1Brown youtube video](https://www.youtube.com/watch?v=Kas0tIxDvrg&t=473s).
Second step I estimate, that 1 % of the people need intensive care for 3 days and sum up
these cases.

So as you may have guessed until now, the following plot isn't scientific from any point of view.
It is just a curve fit with two parameters, and I'm even hiding the R<sup>2</sup> value.

For more scientific data rely on the pro's:

* [Robert Koch Institut](https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/nCoV.html)
* [Johns Hopkins University](https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6)
* [Worldometer.info](https://www.worldometers.info/coronavirus/country/germany/)

They are better in every aspect, except they don't predict the epidemic curve in public.

## Contribute

* Feel free to comment or contribute. I would like to access the data from some online source and
not from my offline csv file.
* Is there a source for the amount of people in intensive care? 1% and 3 days is just a guess.

![Logistic curve of corona virus progression]({{ page.logistic_curve }})

> *Remember:* All models are wrong. [George Box](https://en.wikipedia.org/wiki/All_models_are_wrong)
