># **Common Matrixes Used in Time Series Analysis:**

## **Sum of Squared Errors (SSE)**

$$\large E = \sum_{i=1}^{N}(y_i - \hat{y_i})^2$$

## **Mean Squared Error (MSE)**

$$E = \frac{1}{N}\sum_{i=1}^{N}(y_i - \hat{y_i})^2 \approx E((y_i - \hat{y})^2)$$

## **Root Mean Squared Error (RMSE)**

$$E = \sqrt{\frac{1}{N}\sum_{i=1}^{N}(y_i - \hat{y_i})^2} $$

## **Mean Absolute Error (MAE)**

$$\large E = \frac{1}{N}\sum_{i=1}^{N}|y_i - \hat{y_i}| $$

## **$R^2$**

$$\large E = 1 - \frac{SSE}{SST} = 1 - \frac{MSE}{V \ ar(Y)}  $$

where

$\large SST = \sum_{i=1}^{N}(y_i - \bar{y})^2$

$\large V \ ar(Y) = \frac{1}{N}SST$

## **Mean Absolute Percentage Error (MAPE)**

$$\large E=\frac{1}{N}\sum_{i=1}^{N}|\frac{y_i - \hat{y_i}}{y_i}| $$

## **Symmetric MAPE (sMAPE)**

$$\large E = \frac{1}{N}\sum_{i=1}^{N}(\frac{|y_i - \hat{y_i}|}{\frac{|y_i| + |\hat{y_i}|}{2}})$$

> # **Financial Time Series Primer:**

- Stock price time series data is quite different with other time series data and that's why need to treat this in a different way.

$$\large LSTMs + Stock \ Price \ Prediction \neq profit$$

- Continuous-values, discrete-time (e.g. Yahoo Finance daily/hourly data)
- Advanced: continuous data

## Stock Return

- Percentage change tells us how much we've gained or lost.

$$\large return = \frac{p_{final} - p_{initial}}{p_{initial}}$$

## Indexing the return by time

$$\large R_t = \frac{P_t - P_{t-1}}{P_{t-1}} = \frac{P_t}{P_{t-1}} - 1$$

## Contemporary example of importance of returns

- Many people now considering investing in cryptocurrencies.
- Then think "Bitcoin is expensive" (~$50_000)
- But some random cryptocurrency is just a few cents, so it's cheap.
- This is irrelevant.
- If you have $1000 to spend, you'll buy 1/50 BTC.
- Or you'll buy 10_000 random coins at $0.10 per coin.
- Neither gives you anymore value.
- If random coin drops to $0.05, your value is $500.
- If BTC goes up to $100_000, your value is $2000
- Al Albert Einstein said: everything is relative.

## Log Price

$$\large p_t = \log{P_t}$$

## Gross Return

- There is no symbol for it, we just write $(1 + R_t)$
- Convenient way to see how much our wealth has multiplied
- E.g., $100 -> $120, gross return = 1.2
- E.g., $100 -> $80 (lost $20), gross return = 0.8 (whereas net return = -20%)

$$\large 1 + R_t = \frac{P_t}{P_{t-1}}$$

## Log Return
- Recall: net return can be negative (e.g., -20%)
- Corresponds to the log(1+x) transformation
- Is also just the difference in log prices
- In computers, +/- are more stable and efficient than multiplication and division.

$$\large r_t = \log{(1+R_t)} = \log{\frac{P_t}{P_{t-1}}} = (p_t - p_{t-1})$$

## Adjusted Close

- Adjusted close is the close price adjusted for stock splits and dividends ($D_t$).
- Dividends are paid as cash into your brokerage account.

$$1 + R_t = \frac{P_t + D_t}{P_{t_1}}$$

### Stock Split

- Just for information only - the API / data sources we use have all prices already adjusted for stock splits.
- Motivation: a $100,000 share might be too large for everyone to afford (can't buy fractional shares)
- We "split" the stock, e.g., "2-for-1 split", "3-for-1 split"
- But you will then own 2 or 3 times more shares (the value of what you own does not change).

> # **Random Walks & Random Walks Hypothesis** 

- Brief summary: a more theoretical view on the "price simulation" practical.
- Random walk is a special case of ARIMA.
- Random walk hypothesis: stock prices follow a random walk.
- Consequence: stock price are unpredictable

## What is a random walk?

$$\large p_0 = some \ initial \ value$$

$$\large p_1 = p_0 + e_1, \ where \ e_1 \in \{-1, +1\}$$

$$\large p_2 = p_1 + e_2$$

- Imagine yourself walking - you take one step **left** or **right** based on a coin flip - that's this random walk!
- Can't predict the future (50% chance of being correct).

## Gaussian Random Walk

$$\large p_0 = some \ initial \ value$$

$$\large p_1 = p_0 + e_1, \ where \ e_i \sim \mathcal{N}(0, \sigma^2) $$

$$\large p_2 = p_1 + e_2$$

$$p_1 - p_0 = e_1 \sim \mathcal{N}(0, \sigma^2) \approx Gaussian \ Noise$$

## Log Prices

- Consider a random walk with drift

$$\large p_t = p_{t-1} + \mu + e_t, \ e_t \sim \mathcal{N}(0, \sigma^2) $$

- Take p(t-1) to the LHS - this is now the log return

$$\large r_t = p_t - p_{t-1} = \mu + e_t $$

- The log return is therefore distributed as follows

$$\large r_t \sim \mathcal{N}(\mu, \sigma^2)$$

- This model is the basis for the `Black-Scholes formula`, which earned the Nobel Prize in Economics.

## Is the Random Walk Hypothesis correct?
- **Assumption:** the log returns are iid (independent and identically distributed)
- But we have observed **volatility clustering**.
- Automatically means that the log returns are not identically distributed.
- If volatility at one moment is related to nearby volatilities, then it's also not independent.
- It is a convenient model.
    - Used to derive Black-Scholes
    - When fitting ARIMA, sometimes the best model is a random walk.
    - It's possible to use statistical tests to determine whether or not a time series is a random walk.