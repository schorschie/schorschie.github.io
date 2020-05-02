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
                'key': 'This Week',
                'plot': True,
                'predict': True,
                'style': {'linestyle': '--',
                          'color': 'black'}}]
PREDICTIONS.append({'until': 7,
                    'days':  7,
                    'key': 'Last Week',
                    'plot': False,
                    'predict': False,
                    'style': {'linestyle': '--',
                              'color': 'gray'}})
PREDICTIONS.append({'until': 14,
                    'days':  7,
                    'key': 'Second to Last Week',
                    'plot': False,
                    'predict': False,
                    'style': {'linestyle': ':',
                              'color': 'gray'}})
PREDICTIONS.append({'until': 21,
                    'days':  7,
                    'key': 'Three Weeks Before',
                    'plot': False,
                    'predict': False,
                    'style': {'linestyle': ':',
                              'color': 'lightgray'}})

AXVLINES = [{'date': datetime(2020, 3, 14),
             'plot': True,
             'style': {'color': 'green',
                       'label': 'Schools in Germany closed'}}]
AXVLINES.append({'date': datetime(2020, 3, 21),
                 'plot': True,
                 'style': {'color': 'orange',
                           'label': 'Shops in Germany closed'}})
AXVLINES.append({'date': datetime(2020, 4, 20),
                 'plot': True,
                 'style': {'color': 'blue',
                           'label': 'Shops (≤800m²) in Germany opened'}})

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
    doubling_rate = pd.DataFrame()
    for prediction in PREDICTIONS:
        start_date = last_date - timedelta(days=prediction['until'])
        end_date = start_date - timedelta(days=prediction['days']-1)
        slice_x = xx[len(xx)-(prediction['until']+prediction['days']) : len(xx)-prediction['until'] ]
        d = op.curve_fit(_exponential_function, slice_x,
                         data.loc[end_date : start_date, 'Infected'].values,
                         p0=[0.1, -70])[0]
        predicted_infected = _exponential_function(XX, d[0], d[1])
        doubling_rate.loc[prediction['key'], 'Doubling Rate [d]'] =\
            1/(np.log2(np.exp(1)) * d[0])
        pred[prediction['key']] = predicted_infected
        if prediction['predict']:
            PREDICTION.loc[predict_date, prediction['key'] + "'s prediction"] = \
                np.ceil(pred.loc[predict_date, prediction['key']])

    return pred, PREDICTION, doubling_rate


def get_plot(predict_date, safepath):
    data = _get_data()
    pred, PREDICTION, doubling_rate = _get_predictions(data=data, predict_date=predict_date)
    print(doubling_rate)

    day_before_prediction = (datetime.strptime(predict_date, '%Y-%m-%d') - timedelta(days=1)).strftime('%Y-%m-%d')
    _, ax = plt.subplots(figsize=(13,7))
    data['Infected'].plot(ax=ax, marker='x', linestyle='', label='Infected [RKI]', color='red')
    for prediction in PREDICTIONS:
        if prediction['plot']:
            prediction_key = prediction['key']
            pred[prediction_key].plot(label=prediction_key, **prediction['style'])

        if prediction['predict']:
            PREDICTION.plot(ax=ax, marker='x', markeredgewidth=2, linestyle='')
            ax.annotate('%d' %(PREDICTION[prediction['key'] + "'s prediction"][0]),
                        (PREDICTION.index[0], PREDICTION[prediction['key'] + "'s prediction"][0]),
                        textcoords="offset points", rotation=45,
                        xytext=(1, 10))

    for axline in AXVLINES:
        if axline['plot']:
            ax.axvline(axline['date'], **axline['style'])
    ax.annotate('%d' %(data.loc[day_before_prediction, 'Infected']), (pd.to_datetime(day_before_prediction), 
                                                                      data.loc[day_before_prediction, 'Infected']),
                textcoords="offset points", rotation=-45,
                xytext=(-30, 8))
    plt.yscale('log')
    ax.grid(True)
    ax.legend(loc='best')
    plt.title('Covid-19 Cases in Germany, prediction for ' + predict_date,
              fontsize=14)
    plt.xticks(rotation=30)
    plt.yticks(10**np.array(range(9)))
    plt.ylim((1, 100e6))
    plt.xlim((plt.xlim()[0], plt.xlim()[0]+80))
    plt.ylabel('Infected [-]')
    plt.savefig(safepath)

#   _, ax = plt.subplots(figsize=(13,7))
#   doubling_rate.plot(ax=ax, kind='bar')
#   plt.savefig('bar_' + safepath)

    return ax, doubling_rate


def write_indexmd(picpath, doubling_rate, safepath='covid_19.md'):
    string =u"""---
layout: page
title: Covid-19
logistic_curve: ./%s
mathjax: true
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
fit a exponential function \\\\(e^{k(x-x_0)}\\\\) for the last week of the time span.

So, the following plot is just a curve fit with two parameters, for more scientific data
rely on the pro's:

* [Robert Koch Institut](https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/nCoV.html)
* [Johns Hopkins University](https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6)
* [Worldometer.info](https://www.worldometers.info/coronavirus/country/germany/)
* or, if you want to create your own simulation: [CovidSim](http://covidsim.eu).

![Logistic curve of corona virus progression]({{ page.logistic_curve }})

> *Remember:* All models are wrong. [George Box](https://en.wikipedia.org/wiki/All_models_are_wrong)

## Doubling Rates

The following table shows the doubling rates in days (how much days does it take for the infected people to double their amount),
based on the data points of a whole week. 

%s
""" % (picpath, doubling_rate.to_html(float_format=lambda x: '%10.2f' % (x)))
    f = open(safepath, 'w', encoding="utf-8")
    f.write(string)
    f.close()
    return string


date = datetime(2020, 5, 3)
predict_date = date.strftime('%Y-%m-%d')
safe_path = date.strftime('assets/images/%y%m%d_corona.png')
_, doubling_rate = get_plot(predict_date=predict_date, safepath=safe_path)
write_indexmd(picpath=safe_path,
              doubling_rate=doubling_rate)
