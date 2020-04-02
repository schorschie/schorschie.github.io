#!/usr/bin/env python

 # -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from datetime import timedelta, datetime
from matplotlib.dates import MO
from scipy import optimize as op


PREDICTIONS = [{'until': 0,
                'days': 7,
                'key': 'Last week',
                'plot': True,
                'predict': True,
                'style': {'linestyle': '--',
                          'color': 'black'}}]
PREDICTIONS.append({'until': 7,
                    'days':  7,
                    'key': 'Second to last week',
                    'plot': True,
                    'predict': False,
                    'style': {'linestyle': '--',
                              'color': 'gray'}})
PREDICTIONS.append({'until': 14,
                    'days':  7,
                    'key': 'Three weeks before',
                    'plot': True,
                    'predict': False,
                    'style': {'linestyle': ':',
                              'color': 'gray'}})

def _exponential_function(x, k, x_0):
    y = np.exp(k * (x - x_0))
    return y


def _get_data():
    data = pd.read_csv('covid-19_germany.csv', index_col=0, parse_dates=True)
    data['Delta Infected'] = data['Infected'].diff()
    data.loc[data.index[0], 'Delta Infected'] = data['Infected'][0]
    data['Deceased'] = data['Total Deceased'].diff()
    data.loc[data.index[0], 'Deceased'] = data['Total Deceased'][0]
    print(data)
    return data


def _get_predictions(data, predict_date='2020-03-20'):
    N = (0, len(data)+7)
    xx =  data.index.factorize()[0]
    XX = np.array(range(N[0], N[1]))
    last_date = data.index[-1]

    pred = pd.DataFrame(index=pd.date_range(start=data.index[0], periods=N[1]-N[0], freq='d'))
    PREDICTION = pd.DataFrame(index=[pd.to_datetime(predict_date)])
    for prediction in PREDICTIONS:
        start_date = last_date - timedelta(days=prediction['until'])
        end_date = start_date - timedelta(days=prediction['days']-1)
        slice_x = xx[len(xx)-(prediction['until']+prediction['days']) : len(xx)-prediction['until'] ]
        d = op.curve_fit(_exponential_function, slice_x,
                         data.loc[end_date : start_date, 'Infected'].values,
                         p0=[0.1, -70])[0]
        predicted_infected = _exponential_function(XX, d[0], d[1])
        pred[prediction['key']] = predicted_infected
        if prediction['predict']:
            PREDICTION.loc[predict_date, prediction['key'] + "'s prediction"] = \
                np.ceil(pred.loc[predict_date, prediction['key']])

    return pred, PREDICTION


def get_plot(predict_date, safepath):
    data = _get_data()
    pred, PREDICTION = _get_predictions(data=data, predict_date=predict_date)

    day_before_prediction = (datetime.strptime(predict_date, '%Y-%m-%d') - timedelta(days=1)).strftime('%Y-%m-%d')
    _, ax = plt.subplots(figsize=(13,7))
    data['Infected'].plot(ax=ax, marker='x', linestyle='', label='Infected [RKI]', color='red')
    for prediction in PREDICTIONS:
        if prediction['plot']:
            prediction_key = prediction['key']
            pred[prediction_key].plot(label=prediction_key, **prediction['style'])

    if PREDICTION.size > 0:
        PREDICTION.plot(ax=ax, marker='v', markersize=12)
        ax.annotate('%d' %(PREDICTION.iloc[0,0]), (PREDICTION.index[0], PREDICTION.iloc[0,0]),
                    textcoords="offset points", rotation=45,
                    xytext=(1, 10))
    ax.annotate('%d' %(data.loc[day_before_prediction, 'Infected']), (pd.to_datetime(day_before_prediction), 
                                                                      data.loc[day_before_prediction, 'Infected']),
                textcoords="offset points", rotation=-45,
                xytext=(-30, 8))
    plt.yscale('log')
    ax.grid(True)
    ax.legend(loc='best')
    plt.title('Covid-19 Cases in Germany')
    plt.xticks(rotation=30)
    plt.yticks(10**np.array(range(9)))
    plt.ylim((1, 100e6))
    plt.xlim((plt.xlim()[0], plt.xlim()[0]+80))
    plt.savefig(safepath)
    return ax


def write_indexmd(picpath, safepath='index.md'):
    string =u"""---
layout: home
logistic_curve: ./%s
---

# Covid-19 Cases in Germany

## Prediction

I'm trying to predict the amount of hospital treatment needed to deal with the corona crisis in
Germany, so that people understand, why this drastic measures are necessary. I hope we will se a decrease of the
curve in the near future.

I do not do this to stress you, but to *increase the understanding* for the drastic measures taken now
by the German goverment.

## Disclaimer

The numbers are from the daily [RKI Report](https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html).

In the first step I fit a logistic curve to the current progression of infected cases and a
maximum value of 70%% of the population in Germany. The idea to use a logistic curve came from this
[3Blue1Brown youtube video](https://www.youtube.com/watch?v=Kas0tIxDvrg&t=473s).
Second step I estimate, that 1 %% of the people need intensive care for 3 days and sum up
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
* Is there a source for the amount of people in intensive care? 1%% and 3 days is just a guess.

![Logistic curve of corona virus progression]({{ page.logistic_curve }})

> *Remember:* All models are wrong. [George Box](https://en.wikipedia.org/wiki/All_models_are_wrong)
""" % (picpath)
    f = open(safepath, 'w', encoding="utf-8")
    f.write(string)
    f.close()
    return string


date = datetime(2020, 4, 2)
predict_date = date.strftime('%Y-%m-%d')
safe_path = date.strftime('%y%m%d_corona.png')
get_plot(predict_date=predict_date, safepath=safe_path)
write_indexmd(picpath=safe_path)
