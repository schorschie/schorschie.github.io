#!/usr/bin/env python

 # -*- coding: utf-8 -*-

import to_pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from datetime import timedelta, datetime
from matplotlib.dates import MO
from scipy import optimize as op


AXVLINES = [{'date': datetime(2020, 3, 14),
             'plot': True,
             'style': {'color': 'green',
                       'label': 'Schools in Germany closed'}}]
AXVLINES.append({'date': datetime(2020, 3, 21),
                 'plot': True,
                 'style': {'color': 'orange',
                           'label': 'Shops in Germany closed'}})
AXVLINES.append({'date': datetime(2020, 4, 12),
                 'plot': True,
                 'style': {'color': 'yellow',
                           'label': 'Eastern'}})
AXVLINES.append({'date': datetime(2020, 4, 20),
                 'plot': True,
                 'style': {'color': 'blue',
                           'label': 'Shops (≤800m²) in Germany opened'}})
AXVLINES.append({'date': datetime(2020, 5, 4),
                 'plot': True,
                 'style': {'color': 'magenta',
                           'label': 'All Shops in Germany opened'}})
AXVLINES.append({'date': datetime(2020, 5, 18),
                 'plot': True,
                 'style': {'color': 'seagreen',
                           'label': 'Most Restaurants in Germany opened'}})

def _get_data(region):
    assert isinstance(region, str)
    data = pd.read_csv('covid-19_' + region + '.csv', index_col=0, parse_dates=True)
    data['Infected'] = data['AnzahlFall']
    data['Total Deceased'] = data['AnzahlTodesfall']
    data['Delta Infected'] = data['Infected'].diff()
    data.loc[data.index[0], 'Delta Infected'] = data['Infected'][0]
    data['Deceased'] = data['Total Deceased'].diff()
    data.loc[data.index[0], 'Deceased'] = data['Total Deceased'][0]
    print(data)
    return data


def get_plot(plots):
    for a_plot in plots:
        data = _get_data(a_plot['code'])

        _, ax = plt.subplots(figsize=(13,7))
        data['Infected'].plot(ax=ax, marker='x', linestyle='', label='Infected [RKI]', color='red')

        for axline in AXVLINES:
            if axline['plot']:
                ax.axvline(axline['date'], **axline['style'])

        plt.yscale('log')
        ax.grid(True)
        ax.legend(loc='best')
        plt.title('Covid-19 Cases in ' + a_plot['region'],
                fontsize=14)
        plt.xticks(rotation=30)
        plt.yticks(10**np.array(range(9)))
        plt.ylim((1, 100e6))
        plt.xlim((plt.xlim()[0]+6, plt.xlim()[0]+160))
        plt.ylabel('Infected [-]')
        plt.savefig(a_plot['safe_path'], bbox_inches = 'tight')

        plt.gcf().set_size_inches(2,2)
        ax.get_legend().remove()
        for ticklabel in (ax.get_xticklabels()):
            ticklabel.set_fontsize(5)
        for ticklabel in (ax.get_yticklabels()):
            ticklabel.set_fontsize(5)
        ax.xaxis.get_label().set_fontsize(6)
        ax.yaxis.get_label().set_fontsize(6)
        ax.title.set_fontsize(7)
        plt.savefig(a_plot['thumb_path'], bbox_inches = 'tight')

        plt.close()


def write_indexmd(picpath, safepath='covid_19.md'):
    string =u"""---
layout: post
title: Covid-19 Update
date:   %s
mathjax: true
categories: Corona, Covid-19, update
images:""" % (datetime.now().strftime('%Y-%m-%d %H:%M:%S +0200'))

    for pic in picpath:
        string = string + "\n  - path: /" + pic['safe_path'] + "\n    title: " + pic['region']

    string = string + """
---

## Prediction for {{ page.date | date: "%%s" | plus: 86400 | date_to_string: "ordinal" }}

{%% include image-gallery3.html %%}

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
fit a exponential function \\\\(e^{k(x-x_0)}\\\\) for the last week of the time span.

So, the following plot is just a curve fit with two parameters, for more scientific data
rely on the pro's:

* [Robert Koch Institut](https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/nCoV.html)
* [Johns Hopkins University](https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6)
* [Worldometer.info](https://www.worldometers.info/coronavirus/country/germany/)
* or, if you want to create your own simulation: [CovidSim](http://covidsim.eu).

{%% include image-lightbox.html %%}
""" % (picpath)

    f = open(safepath, 'w', encoding="utf-8")
    f.write(string)
    f.close()
    return string


# to_pandas.write_csv() # downloade csv from rki

date = datetime(2020, 7, 3)
post_path = datetime.now().strftime('_posts/%Y-%m-%d-corona_update.md')

plots = [{'code' : 'germany',
          'region' : 'Deutschland',
         'safe_path' : date.strftime('assets/images/%y%m%d_germany.png'),
         'thumb_path' : date.strftime('assets/images/%y%m%d_germany_thumb.png')}]
plots.append({'code' : 'bw',
              'region' : 'Baden-Württemberg',
              'safe_path' : date.strftime('assets/images/%y%m%d_bw.png'),
              'thumb_path' : date.strftime('assets/images/%y%m%d_bw_thumb.png')})
plots.append({'code' : 'oak',
              'region' : 'Ostalbkreis',
              'safe_path' : date.strftime('assets/images/%y%m%d_oak.png'),
              'thumb_path' : date.strftime('assets/images/%y%m%d_oak_thumb.png')})

get_plot(plots=plots)
write_indexmd(picpath=plots,
              safepath=post_path)
