---
layout: post
title: Covid-19 Update
date:   2020-09-02 08:59:20 +0200
mathjax: true
categories: Corona, Covid-19, update
images:
  - path: /assets/images/200902_germany.png
    title: Deutschland
  - path: /assets/images/200902_bw.png
    title: Baden-Württemberg
  - path: /assets/images/200902_oak.png
    title: Ostalbkreis
ref: Covid-19_update
lang: en
---

## Status of {{ page.date | date: "%s" | date_to_string: "ordinal" }}

So in the following plots is just show data of Germany, Baden-Württemberg and
the Ostalbkreis, which are regions I'm interested in. For more scientific data
rely on the pro's:

* [Robert Koch Institut](https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/nCoV.html)
* [Johns Hopkins University](https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6)
* [Worldometer.info](https://www.worldometers.info/coronavirus/country/germany/)
* or, if you want to create your own simulation: [CovidSim](http://covidsim.eu).

{% include image-gallery3.html %}

{: .right}
[(csv)](https://opendata.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0.csv)

The data is from the daily [RKI
Report](https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html).

{% include image-lightbox.html %}
