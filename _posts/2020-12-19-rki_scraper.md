---
layout: post
title: Machine Learning Nano Degree
date:   2020-12-19 10:10:04 +0200
mathjax: false
categories: Corona, code, udacity
ref: rki_scraper
lang: en
---

This week I started another "Nano-Degree" at Udacity: "Machine Learning
Engineer".

The Nano Degree consist out of five courses, the first course is software
engineering and as a part of it one is encouraged to upload ones own Python
class to [PyPi](https://www.pypi.org) to build up a own portfolio.

So I took the script from [RKI Data Scraper]({% post_url 2020-09-09-scraper_de
%}), refined it to a class and uploaded it to PyPi as
[rki_scraper](https://pypi.org/project/rki-scraper/0.1.7/). It downloads the
current version of the RKI csv file and parses it into a pandas dataframe. Thats
about it, but I haven't found anything similar on the web last summer.

To download it, do the following:

```bash
~$ pip install rki_scraper
~$ python
```

```python
>>> from rki_scraper import RKI
>>> r = RKI()  # wait a while to download and parse a >>100 MB csv file
>>> r.df.head()
```

If you need help, or find a bug just drop a mail!
