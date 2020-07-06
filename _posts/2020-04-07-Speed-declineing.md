---
layout: post
title:  "Speed of Corona declining"
date:   2020-04-07 10:47:20 +0200
categories: personal, homepage, website, corona
mathjax: true
ref: speed_declining
lang: en
---

As you can see from the data of the
[RKI](https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html)
data (overviews from
[Wikipedia](https://de.wikipedia.org/wiki/COVID-19-Pandemie_in_Deutschland#Infektionsf%C3%A4lle)),
the speed of the newly infected in Germany ist declining.

| Date       | Infected | Delta |
|-----------:|---------:|------:|
| 2020-04-01 | 67366    |  5453 |
| 2020-04-02 | 73522    |  6156 |
| 2020-04-03 | 79696    |  6174 |
| 2020-04-04 | 85778    |  6082 |
| 2020-04-05 | 91714    |  5936 |
| 2020-04-06 | 95391    |  3677 |
| 2020-04-07 | 99225    |  3834 |

So as can be seen in the third column, the values of the daily increases are
declining. Thats a good sign and I hope we can find a way to slowly open up the
restrictions and get do a constant daily increase and a therefore to a linear
growth.

For example if we have \\(n\\)-thousand intensive care beds and 2% of the
patients need them for two weeks, than a daily rate of \\(d_r=14 \cdot
\frac{n}{50}\\) would be handable.

I also hope that we can do this without the so called Hammer and Dance"
Strategy. I don't know enough about epidemics to claim, whether a linear
growth is possible. We would need to first increase the value of daily new
infected to d and then lower the \\(R_0\\) coefficient to \\(1\\).
