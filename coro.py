#!/usr/bin/env python

import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import MO
import statsmodels.api as sm
from scipy import optimize as op


PREDICTIONS = [{'days': 3,
                'percentage': 1,
                'key': 'If 1 % need 3 days of care',
                'plot': True}]
PREDICTIONS.append({'days': 15,
                    'percentage': 10,
                    'key': 'If 10 % need 15 days of care',
                    'plot': False})


def logistic_function(x, k, x_0):
    # L maximum
    # k Steepness, d/dx(x=x_0) = k * L
    # x_0 point of 0.5L
    L = 0.5 * 0.7 * 82e6 # The amount of people which will be roundabout at the half infection point.
    y = L / (1 + np.exp(-k * (x - x_0)))
    return y

def get_data():
    data = pd.read_csv('covid-19_germany.csv', index_col=0, parse_dates=True)
    data['Delta Infected'] = data['Infected'].diff()
    data.loc[data.index[0], 'Delta Infected'] = data['Infected'][0]
    data['Total Deceased'] = data['Deceased'].cumsum()
    return data

def get_prediction(data, N=70):
    d = op.curve_fit(logistic_function, data.index.factorize()[0], data['Infected'], p0=[0.5, 30])[0]
    N = (0, N)
    XX = np.array(range(N[0], N[1]))
    
    f = logistic_function(XX, d[0], d[1])
    pred = pd.DataFrame(data={'Prediction': f},
                        index=pd.date_range(start=data.index[0], periods=N[1]-N[0], freq='d'))
    new_infected_prediction = np.hstack([pred['Prediction'][0], np.diff(pred['Prediction'])])
    for prediction in PREDICTIONS:
        prediction_key = prediction['key']
        pred[prediction_key] = np.ceil(new_infected_prediction * prediction['percentage']/100)
        pred[prediction_key] = pred[prediction_key].rolling('%dd' % (prediction['days'])).sum()


    return pred

def get_plot(data, pred, safepath):
    today = time.strftime('%Y-%m-%d')
    PREDICTION = np.ceil(pred.loc[today]['Prediction'])
    _, ax = plt.subplots(figsize=(13,7))
    data['Infected'].plot(ax=ax, marker='x', linestyle='', label='Infected [wikipedia]', color='red')
    pred['Prediction'].plot(ax=ax, label='Prediction', color='red')
    for prediction in PREDICTIONS:
        if prediction['plot']:
            prediction_key = prediction['key']
            pred[prediction_key].plot(label=prediction_key, linestyle=':')

    prediction_dummy = pd.DataFrame(data=PREDICTION, columns=['Prediction for %s' % (today)],
                                    index=[pd.to_datetime(today)])
    prediction_dummy.plot(ax=ax, marker='v', color='green', markersize=12)
    ax.annotate('%d' %(PREDICTION), (pd.to_datetime(today), PREDICTION),
                textcoords="offset points", rotation=45,
                xytext=(1, 10))
    plt.yscale('log')
    ax.grid(True)
    ax.legend(loc='best')
    plt.title('Covid-19 Cases in Germany')
    plt.xticks(rotation=30)
    plt.savefig(safepath)
    return ax

def write_index(safepath='index.html'):
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

<h2>Disclaimer</h2>

<p>The numbers are from a wikipedia article <a href="https://de.wikipedia.org/wiki/COVID-19-Fälle_in_Deutschland">
COVID-19 F&auml;lle in Deutschland</a>.

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
""" % (time.strftime('%y%m%d_corona.png'))
    f = open(safepath, 'w')
    f.write(string)
    f.close()
    return string

data = get_data()
pred = get_prediction(data=data, N=80)
get_plot(data=data, pred=pred, safepath=time.strftime('%y%m%d_corona.png'))
write_index()
# plt.show()
