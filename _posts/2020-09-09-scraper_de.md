---
layout: post
title: RKI Daten Scraper
date:   2020-09-17 08:50:04 +0200
mathjax: false
categories: Corona, code
ref: scraper
lang: de
---

Zu Beginn der Pandemie wollte ich selber mit den [RKI](https://www.rki.de) Daten "rumspielen".
Es war gar nicht so einfach an eine maschinenlesbare Darstellung zu kommen. Sie ist ein
Nebenprodukt der [ArcGIS](https://www.esri.de/produkte/arcgis/das-bietet-arcgis)
Pandemie-[Karte](https://corona.rki.de).

Die Daten von ArcGIS kann man als
[CSV](https://opendata.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0.csv)
Datei herunterladen und in einen Pandas Dataframe parsen:

```python
import pandas as pd
import requests

def scrape(rki_csv_path='covid_19.csv'):
    """Download the RKI CSV and write it to given path."""

    url = 'https://opendata.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0.csv'
    r = requests.get(url, allow_redirects=True)
    open(rki_csv_path, 'wb').write(r.content)

def get_rki(rki_csv_path='covid_19.csv'):
    """Read the RKI CSV from path and return a Pandas dataframe."""

    def dateparser(x):
        """Parse RKI CSV date formats (there a two different ones)."""
        try:
            return pd.datetime.strptime(x, "%d.%m.%Y, %H:%M Uhr")
        except ValueError:
            return pd.datetime.strptime(x, "%Y/%m/%d %H:%M:%S")

    rki = pd.read_csv(rki_csv_path,
                      index_col=0,
                      parse_dates=[8, 10, 13],
                      date_parser=dateparser)
    return rki

# MAIN
scrape()
rki = get_rki()

# Data for Germany:
deutschland = rki[['AnzahlFall', 'AnzahlTodesfall', 'Meldedatum']].groupby('Meldedatum').sum().cumsum()
deutschland.to_csv('covid-19_germany.csv')

# Data for Baden-Württemberg:
bw = rki.query("Bundesland == 'Baden-Württemberg'")[['AnzahlFall', 'AnzahlTodesfall', 'Meldedatum']].groupby('Meldedatum').sum().cumsum()
bw.to_csv('covid-19_bw.csv')

# Data for the Ostalbkreis:
oak = rki.query("Landkreis == 'LK Ostalbkreis'")[['AnzahlFall', 'AnzahlTodesfall', 'Meldedatum']].groupby('Meldedatum').sum().cumsum()
oak.to_csv('covid-19_oak.csv')
```

Andere Quellen für COVID19 Datensätze und Analysen:

* [Johns Hopkins University](https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6)
* [Worldometer.info](https://www.worldometers.info/coronavirus/country/germany/)
* [Süddeutsche Zeitung](https://www.sueddeutsche.de/wissen/corona-zahlen-1.4844448)
* or, if you want to create your own simulation: [CovidSim](http://covidsim.eu)
