#!/usr/bin/env python


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
                    'predict': True,
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


def _get_predictions(data, predict_date='2020-03-20', N=70):
    N = (0, N)
    xx =  data.index.factorize()[0]
    XX = np.array(range(N[0], N[1]))
    last_date = data.index[-1]

    pred = pd.DataFrame(index=pd.date_range(start=data.index[0], periods=N[1]-N[0], freq='d'))
    PREDICTION = pd.DataFrame(data=[], columns=['Date', 'Infections', 'Description'])
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
            PREDICTION.loc[len(PREDICTION)] = [pd.to_datetime(predict_date),
                                               np.ceil(pred.loc[predict_date, prediction['key']]),
                                               prediction['key']]

    return pred, PREDICTION


def get_plot(predict_date, safepath):
    data = _get_data()
    pred, PREDICTION = _get_predictions(data=data, predict_date=predict_date, N=80)

    day_before_prediction = (datetime.strptime(predict_date, '%Y-%m-%d') - timedelta(days=1)).strftime('%Y-%m-%d')
    _, ax = plt.subplots(figsize=(13,7))
    data['Infected'].plot(ax=ax, marker='x', linestyle='', label='Infected [wikipedia]', color='red')
    for prediction in PREDICTIONS:
        if prediction['plot']:
            prediction_key = prediction['key']
            pred[prediction_key].plot(label=prediction_key, **prediction['style'])

    for _, prediction in PREDICTION.iterrows():
        ax.plot(prediction['Date'], prediction['Infections'], marker='v', markersize=12)
        ax.annotate('%d' %(prediction['Infections']), (prediction['Date'], prediction['Infections']),
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
    plt.savefig(safepath)
    return ax

def write_index(picpath, safepath='index.html'):
    string =u"""
<!DOCTYPE html>
<html>
<head>
<title>Covid-19 cases in Germany</title>
<link rel="stylesheet", href="coro.css">
</head>
<body>
<div id="centerContainer">
<h1>Covid-19 Cases in Germany</h1>

<h2>Prediction</h2>

<p>I'm trying to predict the amount of hospital treatment needed to deal with the corona crisis in
Germany, so that people understand, why this drastic measures are necessary. I hope we will se a decrease of the 
curve in the near future.</p>
I do not do this to stress you, but to <em>increase the understanding</em> for the drastic measures taken now 
by the German goverment.

<h3>Update 30<sup>th</sup> of March 2020</h3>

<p>The measures taken by the government where fruitful and the exponential growth is slowing. Therefore I changed the
fitting in that manner, that I don't use the 70%% of sick people as a maximum value anymore.</p>
<h2>Disclaimer</h2>

<p>The numbers are from a wikipedia article <a href="https://de.wikipedia.org/wiki/COVID-19-Pandemie_in_Deutschland">
COVID-19 Pandemie in Deutschland</a>.

<p>In the first step I fit a logistic curve to the current progression of infected cases and a
maximum value of 70%% of the population in Germany. The idea to use a logistic curve came from this
<a href="https://www.youtube.com/watch?v=Kas0tIxDvrg&t=473s">3Blue1Brown video</a>.
Second step I estimate, that 1 %% of the people need intensive care for 3 days and sum up
these cases.</p>

<p>So as you may have guessed until now, the following plot isn't scientific from any point of view.
It is just a curve fit with two parameters, and I'm even hiding the R<sup>2</sup> value.</p>

<p>For more scientific data rely on the pro's:</p>
<ul>
<li><a href="https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/nCoV.html">Robert Koch Institut</a></li>
<li><a href="https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6">Johns Hopkins University</a></li>
<li><a href="https://www.worldometers.info/coronavirus/country/germany/">Worldometer.info</a></li>
</ul>
<p>They are better in every aspect, except they don't predict the epidemic curve in public.</p>

<h2>Contribute</h2>
<ul>
<li>Feel free to comment or contribute. I would like to access the data from some online source and 
not from my offline csv file.</li>
<li>Is there a source for the amount of people in intensive care? 1%% and 3 days is just a guess.</li>
</ul>

<img width=90%% height=auto src="%s" alt="Logistic curve of corona virus progression">

<blockquote>
<p><em>Remember:</em> All models are wrong.
(<a href="https://en.wikipedia.org/wiki/All_models_are_wrong">George Box</a>)</p>
</blockquote>
<p><em>Note:</em> On 10<sup>th</sup> of March 2020 Wikipedia changed it's datasource from the reports to the digital
data of the RKI. I presume the time of day for the readout changed.</p>
<h2>Impressum</h2>
<p>Verantwortlich f&uuml;r den Inhalt dieser Seite:</p>
Grzegorz Lippe<br/>
Eugen-Hafner-Str. 10<br/>
73431 Aalen<br/>

<p>E-Mail: <a href="mailto:Grzegorz.Lippe@googlemail.com?subject=schorschie.github.io">Grzegorz.Lippe@googlemail.com</a></p>

<h3>Resources</h3>

<p>This site is hosted by github. I use python with pandas, numpy, matplotlib, statmodels and scipy for the computation
Output ist html and png.</p>
</div>
</body>
</html>
""" % (picpath)
    f = open(safepath, 'w')
    f.write(string)
    f.close()
    return string

date = datetime(2020, 4,  1)
predict_date = date.strftime('%Y-%m-%d')
safe_path = date.strftime('%y%m%d_corona.png')
get_plot(predict_date=predict_date, safepath=safe_path)
write_index(picpath=safe_path)
# plt.show()
