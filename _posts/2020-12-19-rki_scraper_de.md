---
layout: post
title: Machine Learning Nano Degree
date:   2020-12-19 10:10:04 +0200
mathjax: false
categories: Corona, code, udacity
ref: rki_scraper
lang: de
---

Diese Woche habe ich einen weiteren "Nano-Degree" bei Udacity gestartet:
"Machine Learning Engineer".

Bestandteil des ersten Kurses ist die Aufforderung doch ein eigenes Python
Package auf [PyPi](https://www.pypi.org) hochzuladen, als Fundament für ein
eigenes Portfolio.

Nun, hier ist es: [rki_scraper](https://pypi.org/project/rki-scraper/0.1.7/) Ich
habe den RKI Scraper aus meinem letzten Post [RKI Scraper]({% post_url
2020-09-09-scraper_de %}) ein bisschen aufgehübscht und ihn auf PyPi
hochgeladen. Er lädt die aktuelle Version der RKI Daten aus dem Netz herunter
und parst diese in ein Pandas DataFrame.

Nun kann man sich die RKI Daten folgendermaßen bereitstellen:

```bash
~$ pip install rki_scraper
~$ python
```

```python
>>> from rki_scraper import RKI
>>> r = RKI()  # dauert, über 100 MB csv Datei runterladen und parsen!
>>> r.df.head()
```

Falls jemand Hilfe brauch, oder ein Fehler findet gerne schreiben!
