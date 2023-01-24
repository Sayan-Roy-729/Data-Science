# Different ETS Models

## ETS for Beginners

![EMA & SMA](https://www.fidelity.com/bin-public/060_www_fidelity_com/images/LC/EMA_602x345.png)

## [**Simple Moving Average (SMA)**](https://www.investopedia.com/terms/s/sma.asp)

- SMA computing by taking the average of a rolling-window - just one line of Pandas code.
    - We might want to estimate the mean/variance of a stock's returns
    - Recall: volatility clustering (generally, things change over time)
    - 2 options:
        - Use all values to calculate mean/variance
        - Use only recent values
    - Recent average might be better than overall average
- The SMA is equally weighted, since for a window of size N, each point has a weight $1/N$

```python
# returns a rolling object
rolling_window = df["GooG"].rolling(window_size)

# returns a series/dataframe of rolling means
# can also calculate min, max, sum, var, etc
rolling_window.mean()

# multi-dimensional
covariance = df[["GOOG", "AAPL"]].rolling(50).cov()
```

$$\large SMA = \frac{A_1 + A_2 + A_3 + ... + A_N}{N} $$





## [**Exponentially Weighted Moving Average (EWMA)**](https://corporatefinanceinstitute.com/resources/equities/exponentially-weighted-moving-average-ewma)

- The **EWMA** gives each point a weight that decays exponentially.
- Also known as exponential smoothing/and a kind of low-pass filter
- Very applicable in machine learning statistics, finance, signal processing.

$$\large Arithmetic \ mean: \bar{x} = \frac{1}{T}\sum_{t=1}^{T}X_t$$

$$\large EWMA: \bar{x_t} = \alpha{x_t} + (1-\alpha)\bar{x_{t-1}}, \ where \ 0 \leq \alpha \leq 1  $$

```python
# code to calculate EWMA
xhat = df["GOOG"].ewm(alpha).mean()  # also var, cov, etc.
```
- Choosing **$\large\alpha$**
    - Typically choose a small value between 0 and 1, e.g. 0.1, 0.2
    - Consider $\large\alpha = 1$: Just copy the original time series
    - Consider $\large\alpha = 0$: Just copy itself
    - Consider $\large\alpha$ almost 1:
        - Follow new samples more
        - More jagged
    - Consider $\large\alpha$ almost 0:
        - Follow existing average more

$\large \bar{X_t} = \frac{1}{t}(\sum_{\tau = 1}^{t-1}X_{\tau} + X_t)$

$\large \bar{X_{t-1}} = \frac{1}{t-1}\sum_{\tau=1}^{t-1}X_\tau$

$\large (t-1)\bar{X_{t-1}} = \sum_{\tau=1}^{t-1}X_\tau$

$\large \bar{X_t} = \frac{1}{t}((t-1)\bar{X_{t-1}} + X_t)$

$\large \bar{X_t} = \frac{t-1}{t}\bar{X_{t-1}} + \frac{1}{t}X_t$

$\large \bar{X_t} = (1 - \frac{1}{t})\bar{X_{t-1}} + \frac{1}{t}X_t$

$\large \bar{X_t} = \frac{1}{t}\sum_{\tau=1}^{t}X_\tau  \ and \ \bar{X_t} = (1-\alpha)\bar{X_{t-1}} + \alpha{X_t}$

$\large \bar{X_t} = \frac{1}{t}(X_1 + X_2 + ... + X_t)$

**Why is it exponentially weighted?**

$\large \bar{x_t} = (1-\alpha)\bar{x_{t-1}} + \alpha{x_t}$

$\large \bar{x_t} = (1-\alpha)[(1-\alpha)\bar{x_{t-2}} + \alpha{x_{t-1}}] + \alpha{x_t}$

$\large \bar{x_t} = (1-\alpha)^2\bar{x_{t-2}} + (1-\alpha)\alpha{x_{t-1}} + \alpha{x_t}$

$\large \bar{x_t} = (1-\alpha)^3\bar{x_{t-3}} + (1-\alpha)^2x_{t-2} + (1-\alpha)\alpha{x_{t-1}} + \alpha{x_t}$

$\large \bar{x_t} = (1-\alpha)^t\bar{x_0} + \alpha\sum_{k=0}^{t-1}(1-\alpha)^kx_{t-k}$



## [**Simple Exponential Smoothing (SES):**](https://otexts.com/fpp2/ses.html)

- The **SES** method turns the EWMA into a forecasting model.

$$\large Level(t+h) = EWMA(Time \ series \ from \ 1...t)$$

$$\large \hat{y_t} = \alpha{y_t} + (1-\alpha)\hat{y_{t-1}}$$

### The Forecasting Model

$$\large \hat{y_{t+1|t}} = \alpha{y_t} + (1-\alpha)\hat{y_{t|t-1}} $$

- Time indices have changed!
    - Now: next pred = alpha * current value + (1 - alpha) * current pred
    - Before: current pred = alpha * current value + (1 - alpha) * last pred
- We'll observe this in the code!

### Component Form

- **Forecast Equation:**

$$\large \hat{y_{t+h|t}} = l_t, \ h = 1, 2, 3, ...$$

- **Smoothing Equation:**
    - Just the EWMA
    - Notice: the original time indices are back!
    - $\large l_t$ is called the "level".

$$\large l_t = \alpha{y_t} + (1-\alpha)l_{t-1}$$

```python
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

# make the model - data is univariate
ses = SimpleExpSmoothing(data)

# 'fit' the model - returns a HoltWintersResults object
result = ses.fit(smoothing_level = alpha, optimized = False)

# in-sample prediction or out-of-sample forecast
result.predict(start = start_date, end = end_date)

# get all in-sample predictions
result.fittedvalues

# forecast n steps ahead
result.forecast(n)
```






## [**Holt's Linear Trend Model:**](https://towardsdatascience.com/forecasting-with-holts-linear-trend-exponential-smoothing-af2aa4590c18)

- With simple exponential smoothing, our forecast was always a straight, horizontal line.
- Holt's Linear Trend Model allows for trends (lines at any angle)

$$\large y = mx + b$$

$$\large y_t = slope * t + y_0$$

- Best way to understand it is to study the equations in component form
    - $\large Forecast \ Equation: \hat{y_{t+h|t}} = l_t + hb_t$
        - It's a line equation.
    - $\large Level \ Equation: l_t = \alpha{y_t} + (1-\alpha)(l_{t-1} + b_{t-1})$
        - $\large (l_{t-1} + b_{t-1}) ⬅$ one step increase due to trend $\large = l_{t-1} + 1 * b_{t-1}$
    - $\large Trend \ Equation: b_t = \beta(l_t - l_{t-1}) + (1-\beta)b_{t-1}$
        - $\large(l_t - l_{t-1}) ⬅$ slope in one step $\large = \frac{l_t - l_{t-1}}{1}$

**How to treat alpha ($\large\alpha$)**
- Alpha is often a hyperparameter, depending on what you're doing
- Ex. imagine you're an audio engineer, applying effects to a sound file
- You have to "tune" these knobs to your tastes
- In Holt's Linear Trend Model, can treat it more like "machine learning"
$$\large Error = \sum_{t=1}^{T}(y_t - \hat{y_{t|t-1}})^2$$

$$\large \alpha,\beta = arg \ min \ Error(\alpha, \beta)$$

```python
from statsmodels.tsa.holtwinters import Holt

# make the model - data is univariate
model = Holt(data)

# 'fit' the model - returns a HoltWintersResults object
result = model.fit()

# in-sample prediction or out-of-sample forecast
result.fittedvalues
result.forecast(n)
```


## [**Holt-Winters Model**](https://towardsdatascience.com/time-series-forecasting-with-holt-winters-b78ffc322f24)

- **So far:**
    - Simple Moving Average
    - Exponentially-Weighted Moving Average
    - Simple Exponential Smoothing as a forecasting model
    - Holt's Linear Trend Model
- Holt-Winters adds a seasonal component
    - Applicable everywhere: the weather, air conditioner sales, back-to-school, Black Friday, ...
- In time-series, there are 3 components
    - (Linear) trend
    - Seasonal (cycles)
    - Level (average)
- **Additive Method vs. Multiplicative Method**
    - Additive: y = level + trend + seasonal
    - Multiplicative: y = (level + trend) * seasonal

### Hold-Winters Additive Model
- Is still in the form of EWMA
- y = level + trend + seasonal, so seasonal = y - level - trend

$\large Forecast: \hat{y_{t+h|t}} = l_t + hb_t + s_{t+h-mk}$

$\large Level: l_t = \alpha(y_t - s_{t-m}) + (1-\alpha)(l_{t-1} + b_{t-1})$

$\large Trend: b_t = \beta(l_t - l_{t-1}) + (1-\beta)b_{t-1}$

$\large Seasonality: s_t = \gamma(y_t - l_{t-1} - b_{t-1}) + (1-\gamma)s_{t-m}$

- *Note: $m$ = the period of the cycle*
- $\large k = floor(\frac{h-1}{m}) + 1$
    - The intuition: finds the latest matching seasonal component (e.g. for March forecast, find the last-known March)
    - Mar 2020 (last known) ➡ Dec 2020 (end of data) ➡ Mar 2021 (forecast date)

### Holt-Winters Multiplicative Model

$\large Forecast: \hat{y}_{t+h|t} = (l_t + bh_t)s_{t+h-mk} $

$\large Level: l_t = \alpha\frac{y_t}{s_{t-m}} + (1 - \alpha)(l_{t-1} + b_{t-1})$

$\large Trend: b_t = \beta(l_t - l_{t-1}) + (1-\beta)b_{t-1}$

$\large Seasonal: s_t = \gamma\frac{y_t}{l_{t-1}+b_{t-1}} + (1-\gamma)s_{t-m}$

```python
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# make the model - data is univariate
# trend/seasonal args can be 'add' or 'mul'
model = ExponentialSmoothing(
    data,
    trend = 'add',
    seasonal = 'add',
    seasonal_periods = 12
)

# 'fit' the model - returns a HoltWintersResults object
result = model.fit()

# in-sample prediction or out-of-sample forecast
result.fittedvalues
result.forecast(n)
```


## [**Walk-Forward Validation:**](https://sarit-maitra.medium.com/take-time-series-a-level-up-with-walk-forward-validation-217c33114f68)

- In general machine learning architecture, you use K-Fold Cross Validation to evaluate your model. But in time-series, you can't use because in the time-series data, there are time dependent factors among the data points.
- Since the data is split randomly, you'll mix past and future data.
- In the real-world, your model cannot be trained on future data!
- We can only use past data to predict future data.
- For this, Walk Forward Validation can be a key-point for the time-series data.
- Start with some minimum data to train on.
- ... and validation forecast horizon $h \geq 1$
- Walk forward one step (train set becomes +1 bigger).
- Validate on the next $h$ data points, etc etc. until you reach the end.

![Walk Forward Validation](https://alphascientist.com/images/walkforward.png)

- You can also set the training set constant size.
- When you add more training data to the end, you delete the same amount from the beginning.

![With constant training set](https://www.researchgate.net/publication/348249035/figure/fig4/AS:983761357393920@1611558393131/Walk-forward-validation-with-five-folds.jpg)

- You can also walk forward by $h$ steps instead of just 1 step.
- Or any other step size you like.

### TimeSeriesSplit (Scikit-Learn)

- Might save you from a bit of work, under the right circumstances.
- To use with cross validation functions, your model must conform to scikit-learn interface (e.e. not statsmodels)
- Another limitation: not flexible - must use non-overlapping blocks
- All blocks are equal size - first train set is teeny tiny
- Do these reflect real-world operation?
