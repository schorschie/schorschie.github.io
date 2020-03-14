
Covid-19 Cases in Germany
=========================

I'm trying to predict the amount of hospital treatment needed to deal with the corona crisis in
germany.

The numbers in the csv file are from a wikipedia article [COVID-19 Fälle in
Deutschland](https://de.wikipedia.org/wiki/COVID-19-Fälle_in_Deutschland).

In the first step I fit a logistic curve to the current progression of infected cases and a
maximum value of 70% of germany.

The idea to use a logistic curve came from this 3Blue1Brown [video](https://www.youtube.com/watch?v=Kas0tIxDvrg&t=473s)

Second step I estimate, that 1 % of the people need intensive care for 4 days and sum up
these cases.






Contribute
==========

* Feel free to comment or contribute. I would like to access the data from some online source and
  not from my offline csv file.
* Is there a source for the amount of people in intensive care? 1% and 3 days is just a guess.
