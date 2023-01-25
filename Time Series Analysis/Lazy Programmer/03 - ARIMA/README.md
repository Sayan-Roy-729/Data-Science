# ARIMA Models

## AutoRegressive Model (AR)

**ARIMA vs. Exponential Smoothing**

- Exponential smoothing is very specific (linear trends, seasonality)
- ARIMA imposes no such structure. It is more "machine learning" -like.

**What is an auto-regressive model?**

- Let's first recall linear regression.
- Example: x = years of experience, y = salary, $\large \hat{y} = mx + b$

![Linear Regression](https://production-media.paperswithcode.com/methods/2560px-Linear_regression.svg_wwqz1f3.png)

- If more than one input, like $x_1$ = years of experience, $x_2$ = age, y = salary, then $\hat{y} = w_1x_1 + w_2x_2 + b$
- $w_1$, $w_2$, $b$ are found by minimizing the error of the predictions.
- $b=$ salary when years of experience and age are zero
- $w_1 = $ amount salary increases when years of experience increases by 1
- Ex. if $w_1 = 5000$, then on average I should get a $5000 raise every additional year I work.
- Multiple vs. Simple Linear Regression

**AR(p)**

- It's just linear regression. We use the past data points in the series to predict the next point
- $AR(p) = $ auto-regressive model of order $p$.

$$\large \hat{y_t} = b + \phi_1y_{t-1} + \phi_2y_{t-2} + ... + \phi_py_{t-p}$$

- equivalent expression

$$\large y_t = b + \phi_1y_{t-1} + \phi_2y_{t-2} + ... + \phi_py_{t-p} + \varepsilon_t$$

$$\large\varepsilon_t \backsim \aleph(0, \sigma^2)$$

$$\large\hat{y_t} = E(y_t)$$


**Blogs**
- https://machinelearningmastery.com/autoregression-models-time-series-forecasting-python
- https://otexts.com/fpp2/AR.html
