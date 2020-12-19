---
layout: post
title: Machine Learning Nano Degree
date:   2020-12-19 10:10:04 +0200
mathjax: false
categories: Corona, code, udacity
ref: rki_scraper
lang: de
---

Diese Woche habe ich einen weiteren "Nano-Degree" bei Udacity gestartet,
"Machine Learning Engineer".

Bestandteil des ersten Kurses ist die Aufforderung doch ein eigenes Python
Package auf (PyPi)[https://www.pypi.org] hochzuladen, als Bestandteil des
eigenen Portfolios.

Nun, hier ist es: (RKI Scraper][]. Ich habe den RKI Scraper aus meinem letzten
post () ein bisschen aufgehübscht und ihn auf PyPi hochgeladen. Er lädt die
aktuelle Version der RKI Daten aus dem Netz herunter und parst diese in ein
Pandas DataFrame.

Nun kann man sich die RKI Daten folgendermaßen bereitstellen:

```bash
~$ pip install rki_scraper
~$ python
```

```python
>>> from rki_scraper import RKI
>>> r = RKI()  # dauert, über 100 MB !
>>> r.df.head()
```
