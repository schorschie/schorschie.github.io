#!/usr/bin/env conda run -n gis python

import pandas as pd
import requests


def scrape(rki_csv_path='covid_19.csv'):
    url = 'https://opendata.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0.csv'
    r = requests.get(url, allow_redirects=True)
    open(rki_csv_path, 'wb').write(r.content)

def get_rki(rki_csv_path='covid_19.csv'):
    def dateparser(x):
        try:
            return pd.datetime.strptime(x, "%d.%m.%Y, %H:%M Uhr")
        except ValueError:
            return pd.datetime.strptime(x, "%Y/%m/%d %H:%M:%S")

    rki = pd.read_csv(rki_csv_path,
                      index_col=0,
                      parse_dates=[8, 10, 13],
                      date_parser=dateparser)
    return rki

def write_csv():
    rki = get_rki()

    deutschland = rki[['AnzahlFall', 'AnzahlTodesfall', 'Meldedatum']].groupby('Meldedatum').sum().cumsum()
    deutschland.to_csv('covid-19_germany.csv')

    bw = rki.query("Bundesland == 'Baden-Württemberg'")[['AnzahlFall', 'AnzahlTodesfall', 'Meldedatum']].groupby('Meldedatum').sum().cumsum()
    bw.to_csv('covid-19_bw.csv')

    oak = rki.query("Landkreis == 'LK Ostalbkreis'")[['AnzahlFall', 'AnzahlTodesfall', 'Meldedatum']].groupby('Meldedatum').sum().cumsum()
    oak.to_csv('covid-19_oak.csv')


if __name__ == "__main__":

    DOWNLOAD_DATA = True
    if DOWNLOAD_DATA:
        scrape()

    write_csv()
