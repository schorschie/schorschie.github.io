---
layout: post
title: Covid-19 Update
date:   2020-06-03 18:26:30 +0200
mathjax: true
categories: Corona, Covid-19, update
---

## Prediction for {{ page.date | date: "%s" | plus: 86400 | date_to_string: "ordinal" }}

Despite the prolonged opening of the social live the curve still looks good.
Here is an interesting article from [Süddeutsche](http://www.sueddeutsche.de)
regarding this topic: [Warten auf die zweite
Welle](https://www.sueddeutsche.de/gesundheit/coronavirus-zweite-welle-neuinfektionen-1.4924892).


![Logistic curve of corona virus progression](/assets/images/200602_corona.png)

{: .right}
[(csv)](/covid-19_germany.csv)

> *Remember:* All models are wrong. [George Box](https://en.wikipedia.org/wiki/All_models_are_wrong)

## Doubling Rates

The following table shows the doubling rates in days (how much days does it take for the infected people to double their amount),
based on the data points of a whole week.

<!-- markdownlint-disable no-inline-html -->
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Doubling Rate [d]</th>
      <th>Prediction [02.06.20]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Fit based on this weeks data</th>
      <td>437</td>
      <td>186926</td>
    </tr>
    <tr>
      <th>Last Week</th>
      <td>311</td>
      <td>188855</td>
    </tr>
    <tr>
      <th>Second to Last Week</th>
      <td>218</td>
      <td>193562</td>
    </tr>
    <tr>
      <th>Three Weeks Before</th>
      <td>160</td>
      <td>201165</td>
    </tr>
  </tbody>
</table>
<!-- markdownlint-enable no-inline-html -->

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
