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

**`AR(p)`**

- It's just linear regression. We use the past data points in the series to predict the next point
- $AR(p) = $ auto-regressive model of order $p$.

$$\large \hat{y_t} = b + \phi_1y_{t-1} + \phi_2y_{t-2} + ... + \phi_py_{t-p}$$

- equivalent expression

$$\large y_t = b + \phi_1y_{t-1} + \phi_2y_{t-2} + ... + \phi_py_{t-p} + \varepsilon_t$$

$$\large\varepsilon_t \backsim \aleph(0, \sigma^2)$$

$$\large\hat{y_t} = E(y_t)$$

**Why stick to Linear regression when you have good algorithms in the market?**

- Linear models aren't that powerful (only lines and hyper-planes).
- But we know that linear models help to understand the feature importance.
- ARIMA also helps us understand the modeling and statistical properties of your data.


**Blogs**
- https://machinelearningmastery.com/autoregression-models-time-series-forecasting-python
- https://otexts.com/fpp2/AR.html


## Moving Average Model | `MA(q)`

- Not the same as "simple moving average" and "exponentially weighted moving average" (EWMA).
- Moving average of order q
- It depends on past errors, not on past data in the time series.

$$\large y_t = c + \varepsilon_t + \theta_1\varepsilon_{t-1} + \theta_2\varepsilon_{t-2} + ... + \theta_q\varepsilon_{t-q}$$

$$\large Expected \ Value \ E(y_t) = E(c + \varepsilon_t + \theta_1\varepsilon_{t-1} + \theta_2\varepsilon_{t-2} + ... + \theta_q\varepsilon_{t-q})$$

$$\large Expected \ Value \ E(y_t) = c \ (if \ other \ \varepsilon \ become \ zero)$$

### Simulation

$\large Initialize: \varepsilon_1, \varepsilon_2 \backsim \aleph(0, \sigma^2)$

$\large Sample: \varepsilon_3 \backsim \aleph(0, \sigma^2)$

$\large Calculate: y_3 = c + \varepsilon_3 + \theta_1\varepsilon_2 + \theta_2\varepsilon_1$

$\large Sample: \varepsilon_4 \backsim \aleph(0, \sigma^2)$

$\large Calculate: y_4 = c + \varepsilon_4 + \theta_1\varepsilon_3 + \theta_2\varepsilon_2$

and so on...



## ARIMA

### `ARMA(p, q)`

- Auroregressive moving average.
- $\large ARMA(p, q) = AR(p) + MA(q)$

$$\large y_t = b + AR(p) + MA(q) + \varepsilon_t$$

$$\large y_t = b + (\phi_1y_{t-1} + ... + \phi_py_{t-p}) + (\theta_1\varepsilon_{t-1} + ... + \theta_q\varepsilon_{t-q}) + \varepsilon_t$$

### `ARIMA`

- ARIMA = autoregressive integrated moving average
- The *integrated* part works differently than the others!

**Differencing:**

Given: $\large\{y_t\} = \{y_1, y_2, ..., y_r\}$ (some time series).

Differenced Series: $\large \Delta{y_t} = y_t - y_{t-1}$

- Where have we seen this?
    - *Log returns* - the difference of log prices: $r_t = p_t - p_{t-1}$
    - *Holt's Linear Trend Model:* $b_t = \beta(l_t - l_{t-1}) + (1 - \beta)b_{t-1}$

**Why difference?**

- When fitting an ARMA model, we want the data to be close to stationary.
- Stationary = Does not change over time
- Stationary is nice: mean, variance, autocorrelation, ... will be constant over time
    - Recall: linear models fit well when there is strong correlation between inputs/output
- Each "window" of the time series is like a "training point" for fitting the model.

**Differencing and Stationary**

- Differencing will often make the time series stationary!
- We have already seen this (log returns)
- Not exact of course (volatility clustering)
- SOmetimes, need to difference twice (but usually not more).

**I(d) and ARIMA(p, d, q)**

- An $I(d)$ process is a process that is stationary after differencing $d$ times.
- We say it's integrated to order $d$.
- $ARIMA(p, d, q)$ is just a model where we've differenced $d$ times before applying $ARMA(p, q)$

**Special Cases**

- $ARIMA(p, 0, 0) = AR(p = ARMA(p, 0))$
- $ARIMA(0, 0, q) = ARMA(0, q) = MA(q)$
- $ARIMA(0, d, 0) = I(d)$

**Random Walk**

- $ARIMA(0, 1, 0)$ is $I(1)$ and this is a random walk.

$$\large \Delta y_t = \varepsilon_t$$

$$\large y_t - y_{t-1} = \varepsilon_t$$

$$\large y_t = y_{t-1} + \varepsilon_t \ (Exactly \ the \ random \ walk \ formula)$$

**Log Returns**

- If we fit an ARIMA and find it to be a random walk, this says that the return can't be predicted from previous values.

$$\large r_t = p_t - p_{t-1} = \varepsilon_t \backsim \aleph(\mu, \sigma^2)$$

## Stationarity for I(d) order selection

- Stationarity will help us choose the hyper-parameter, $d$.



**Practical explanation of stationarity**

- Loosely, the distribution of the random variables in the time series does not change over time.
- E.g., mean and variance will always be the same.
- If you see a time series looking upwards or downwards then you know that mean is changing. Therefore, existence of any trends means that the time series is not stationary.
- When the variance changes over time, that is also not stationary.
- Stock returns exhibit volatility clustering, but don't be surprised if we assume they are stationary!



### `ADF Test`

- We use the **Augmented Dickey-Fuller Test** (ADF Test).
- Think of it like an API:
    - Given: null hypothesis, alternative hypothesis
    - Input: time series, Output: p-value
    - Action: accept or reject the null hypothesis
- For ADF test:
    - Null: time series is non-stationary
    - Alternative: time series is stationary



**How to use the ADF Test to select d?**

- Idea: keep differencing until the result is stationary (check using ADF)

![How to use ADF test](../00%20-%20Images/image-1.png)



**Strong vs. Weak Stationarity**

- More formally, there are 2 kinds of stationary:
    - Strong-sense stationarity (SSS)
    - Weak-sense stationarity (WSS)
- Strong: The entire distribution does not change over time (over any selection of RVs)

![Strong Stationarity](../00%20-%20Images/image-2.png)

- Weak-Sense Stationarity
    - First-order statistics (mean), second-order statistics (auto-covariance)
    - The mean does not change over time

    $\large \mu_{Y}(t) = \mu_{Y}(t + \tau) \ for \ all \ \tau$

    - The auto-covariance does not change over time

    $\large K_{YY}(t_1, t_2) = K_{YY}(t_1 - t_2, 0) \ for \ all \ t_1,t_2$



**What is auto-covariance?**

- Auto = Self (e.g. auto-regressive = y(t) depends on its own past values!)
- Auto-covariance = just the covariance of 2 RVs from the same time series.
- Recall: covariance = unscaled correlation
    - Not related $\longrightarrow$ covariance = 0
    - Move in same direction $\longrightarrow$ covariance > 0
    - Move in opposite direction $\longrightarrow$ covariance < 0

$$\large\large K_{YY}(t_1, t_2) = E\{(Y_{t_1} - \mu_{Y}(t_1))(Y_{t_2} - \mu_{Y}(t_2))\}$$



**Why time difference?**

$$\large K_{YY}(t_1, t_2) = K_{YY}(t_1 - t_2, 0) \ for \ all \ t_1, t_2$$

- $t_1 - t_2$ is the distance between 2 time points.
- That's mean if I pick any 2 time points in a series, as long as the time difference is same, the covariance between these 2 random variables is the same. E.g. (the distance between all of these are 2),

$$cov(Y_1, Y_3) == cov(Y_3, Y_5) == cov(Y_{10}, Y_{12})$$

- The relationship between points in the time series remains constant no matter where I look, as long as they're same distance apart.
- Makes sense if we want to fit an auto-regressive model, e.g., $y(t) = 0.5y(t-1)$
- The equation doesn't work if it's only true for $t=2$ but not $t=3$!



**Variance is constant over time**

- The auto-covariance requirement also implies variance is constant.
- Why? If it is true that the auto-covariance depends only on the time difference then it doesn't matter what time we pick. $K(1, 1) = K(0, 0), K(2, 2) = K(0, 0)$ etc.
- That's why if we that the variance is changing over time as we do with volatility clustering, then we take as evidence that the time series is not stationary.

$$\large K_{YY}(t_1, t_2) = K_{YY}(t_1 - t_2, 0) \ for \ all \ t_1, t_2$$

$$\large\large K_{YY}(t_1, t_2) = E\{(Y_{t_1} - \mu_{Y}(t_1))(Y_{t_2} - \mu_{Y}(t_2))\}$$


**How is stationarity useful?**

- If a time series is non-stationarity, then you might need different models at different points in time!
- For non-stationarity time series, you can't treat data points at different times like "samples" (e.g. computing the mean, variance)



## Auto-correlation Function (ACF) for MA(q) order selection

- Also known as correlogram
- Autocorrelation is to autocovariance as correlation is to covariance
- Auto = Self (both RVs come from the same time series)
- Correlation = scaled covariance (always between -1 and +1)

$$\large Autocovariance: cov(Y_{t_1}, Y_{t_2}) = E\{(X - \mu_X)(Y - \mu_Y)\}$$

$$\large Autocorrelation: \frac{cov(Y_{t_1}, Y_{t_2})}{\sigma_Y(t_1)\sigma_Y(t_2)}$$

**Autocorrelation to ACF**

- The ACF is defined as if the time series were stationary (that is, the autocorrelation depends only on the time difference $\tau$)
- We can calculate the sample mean, covariance, correlation, ... over time.

$$\large Stationary: \varrho(Y(t_1), Y(t_2)) = \varrho(t_1 - t_2) = \varrho(\tau)$$

$$\large \hat{\varrho}(\tau) = \frac{1}{(T-\tau)\hat{\sigma}^2}\sum_{t=1}^{T-\tau}(y_t - \hat{\mu})(y_{t+\tau} - \hat{\mu})$$

- $\large \frac{1}{T-\tau} = $ because that's many samples we are adding up.
- $\large \frac{1}{\sigma^2} =$  Without this, the formula will become to auto-covariance formula. The autocorrelation is the autocovariance divided by the sigmas of the two random variables. Because of we are assuming the time series is stationarity, the both sigma is same and that why there is the squared term.
- $\large y_t - \hat{\mu})(y_{t+\tau} - \hat{\mu}) = $ which is exactly which goes inside the expected value for the autocorrelation.
- $\large \hat{\varrho}(\tau) =$ It's just the sample correlation in time.

**Plotting the ACF**

So, what is the consequence having autocorrelation function which is only a function of a lag $\tau$. We are calling it lag because we are comparing to of the same time-series except that one of the time-series is lagging behind by the duration $\tau$.

- Plot ACF value vs. the lag ($\tau$)
- In R, the acf() function is built right in
- In Python, see Scipy or statsmodels

![ACF Plot](../00%20-%20Images/image-3.png)

*Note: at lag=0, we just get variance / variance = 1*

**Confidence Intervals in ACF plot**

- The interesting thing with ACF plot is that, it also plots the confidence intervals. This confidence interval can be thought off that kind of threshold.
- If we see any lagged autocorrelations outside the confidence threshold, we will *reject* that they are equal to 0.
- Any point we find in ACF plot that goes outside of the confidence interval we can consider to be non-zero.
- Note! Frequentist interpretation: for a 95% confidence interval, this means 5% of the time values will go outside by chance.

**How to determine `q` in MA(q)**

- A moving average process of order q can be shown to have non-zero autocorrelation up to lag q. That is if we look at the ACF plot, and can see that at lag 2 the ACF goes outside of the confidence interval but after that it doesn't then we would choose q = 2.
- Assign q to be the maximum non-zero lag
- E.g. in below chart, q = 2
- Usually, the ACF for lags < q are also non-zero

**Why does it work?**

- This can be derived mathematically! (we won't do it right now)
- For MA(1):

$$\large y_t = c + \theta_1\varepsilon_{t-1} + \varepsilon_t, \ where \ \varepsilon_t \backsim \aleph(0, \sigma^2)$$

$$\large Q(1) = \frac{\theta_1}{1 + \theta_1^2}, \ \varrho(\tau) = 0 \ for \ \tau > 1$$

- For MA(2):

$$\large \varrho(1) = \frac{\theta_1 + \theta_1\theta_2}{1+\theta_1^2+\theta_2^2}, \ \varrho(2) = \frac{\theta_2}{1+\theta_1^2+\theta_2^2}, \ \varrho(\tau) = 0 \ for \ \tau > 2$$

## PACF for AR(p) order selection

- PACF = Partial Autocorrelation Function
- A bit more difficult to understand than ACF but its application to choosing p is the same

![PACF Plot](../00%20-%20Images/image-4.png)

**Practical Application of PACF**

The vertical axis is the value of the function and the horizontal axis still represents the lag $\tau$. And to read the graph is exactly save as the ACF plot.  If we see any statistically significant non-zero lags up to some lag $p$, this would indicate we have autoregressive component of order $p$.

- Set p = maximum non-zero (outside confidence interval) lag
- p = 5 from the graph.

**What is the PACF?**

- 2 methods:
    - Its definition
    - How it is calculated

![Definition of PACF](../00%20-%20Images/image-5.png)

- You can think about it as conditional autocorrelation where the regular autocorrelation is unconditional.

![How to calculate PACF Part-1](../00%20-%20Images/image-6.png)

![How to calculate PACF Part-2](../00%20-%20Images/image-7.png)

![How to calculate PACF Part-3](../00%20-%20Images/image-8.png)
