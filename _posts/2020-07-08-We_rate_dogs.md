---
layout: post
title: We rate dogs Udacity project
date:   2020-07-08 18:35:04 +0200
categories: twitter, education, udacity
ref: udacity-dogs
lang: en
---

As part of a [Udacity](https://www.udacity.com) Data Analyst Nanodegree I analyzed a Twitter account:
[We Rate Dogs!](https://twitter.com/dog_rates).

We rate dogs is a popular Twitter account posting funny pictures and ratings about dogs. I
want to analyze the coverage of that account.

The dataset used spans from End of 2015 to Summer 2017, and I learned how to use
the twitter api to download the data:

![Tweets from We rate Dogs](/assets/images/dogs/timestamp_histogram.png){: .centered }

The figure above shows the amount of tweets from that account in the considered time frame and
it can be seen, that the were more active in late 2015.

The dog jury of *We rate Dogs* has their own vocabulary in naming different types of dogs, like
'doggo' or 'pupper'.

In the dataset given, they used it in around a quarter of occasions:

![Dog pie of Dogtionary](/assets/images/dogs/dogpie.png){: .centered }

Most of the dogs remained untyped, but around a sixth was classified as a 'Pupper' and the least
amount of dogs were 'Floofers'.

Here are two examples for 'Puppers', source Twitter, just click the images to
link to the tweets:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Meet Benji. He just turned 1. Has already given up on a traditional pupper physique. Just inhaled that thing. 9/10 <a href="https://t.co/sLUC4th3Zj">pic.twitter.com/sLUC4th3Zj</a></p>&mdash; WeRateDogs® (@dog_rates) <a href="https://twitter.com/dog_rates/status/739606147276148736?ref_src=twsrc%5Etfw">June 5, 2016</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

[![A pupper](/assets/images/dogs/CkOb3FXW0AAUL_U.jpg){: .half-image }](https://twitter.com/dog_rates/status/739606147276148736?s=20)
[![another pupper](/assets/images/dogs/ChpuRyvVAAARMoq.jpg){: .half-image }](https://twitter.com/dog_rates/status/728015554473250816?s=20)

And here one example for a fluffer:

[![a Fluffer](/assets/images/dogs/DEJT3FeXoAAtwUy.jpg){: .half-centered }](https://twitter.com/dog_rates/status/883360690899218434?s=20)

## Coverage

In total the account generated over 10.000.000 retweets and favs, with a higher momentum in the
earlier time span:

![Cumulated Retweets of We Rate Dogs](/assets/images/dogs/cumulated_retweets.png){: .half-image }
![Cumulated Favorites of We Rate Dogs](/assets/images/dogs/cumulated_favs.png){: .half-image }

Another interesting fact within the twitter account of we rate dots, are their (name giving)
Dog Rates. They mostly rate dogs within a "... out of ten scale", so for example 8/10, or 4/10.
But sometimes a dog receives only a top note, and on other times the nominator may be higher
than 10, so for example 14/10.

Therefore I normalized all values to be within (0, 1) and also aded a denominator of 10,
wherever it was missing:

![Normalized grades of we rate dogs](/assets/images/dogs/normalized_grades.png){: .half-image }
![Normalized grades without outliers of we rate dogs](/assets/images/dogs/normalized_grades_without_outliers.png){: .half-image }

So now it is clear, that there are only a few outliers, namely those four guys. If you are a
dog person, brace for a cuteness impact:

<!-- markdownlint-disable no-inline-html -->
<ul class="image-gallery4">
<li>
  <a href="https://twitter.com/dog_rates/status/892177421306343426?s=20">
    <img src="/assets/images/dogs/DGGmoV4XsAAUL6n_thumb.jpg" alt="OMG!" title="OMG!" />
    <span>OMG!</span>
  </a>
</li>

<li>
  <a href="https://twitter.com/dog_rates/status/891815181378084864?s=20">
    <img src="/assets/images/dogs/DGBdLU1WsAANxJ9_thumb.jpg" alt="In the bush :D" title="In the bush :D" />
    <span>In the bush :D</span>
  </a>
</li>

<li>
  <a href="https://twitter.com/dog_rates/status/891689557279858688?s=20">
    <img src="/assets/images/dogs/DF_q7IAWsAEuuN8_thumb.jpg" alt="Full of food" title="Full of food" />
    <span>Full of food</span>
  </a>
</li>

<li>
  <a href="https://twitter.com/dog_rates/status/891327558926688256?s=20">
    <img src="/assets/images/dogs/DF6hr6BUMAAzZgT_thumb.jpg" alt="And again so cute!" title="And again so cute!" />
    <span>And again so cute!</span>
  </a>
</li>
</ul>
<!-- markdownlint-enable no-inline-html -->

Maybe as a last annotation it is worth noting, that the cuteness of the dogs increases slightly
over time:

![Cuteness Inflation](/assets/images/dogs/cutness_inflation.png){: .centered }

so it might be interesting to stay tuned and follow that twitter
[account](https://twitter.com/dog_rates), if you are a dog person!
