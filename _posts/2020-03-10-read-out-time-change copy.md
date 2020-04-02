---
layout: post
title:  "Logistic curve does not apply anymore"
date:   2020-04-01 08:24:20 +0200
categories: model, logistic, curve, exponential, function
---

The logistics function does not apply anymore, because:

* there could be a vaccine before we reach 70%% of infected.
* the shutdown could lead to a confinement of the decease.

Therefore I changed the fit to a simple exponential function $e^{x-x_0}$. Also the prediction
now is limited to seven days, and there are three fittings: Extrapolation of the last weeks
growth, the second to last week and from three weeks behind.

Now it is possible to see the effect of the school closing and contact limitations.
