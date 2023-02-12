# Vector Auto-regressive & Moving Average Models

- Previously, we looked at only single time series' in isolation.
- Assumption: the time series is predictable using only its past values.
- In real-world, could one time series affect another?
- Ex. Num visitors to website --> Num webservers required to serve traffic
- Ex. Minimum wage --> Unemployment rate / num jobs

## VARMA

Equation for ARMA

$$\large y_t = b + \phi_1y_{t-1} + ... + \phi_py_{t-p} + \theta_1\varepsilon_{t-1} + ... + \theta_q\varepsilon_{t-q} + \varepsilon_t$$

- Equation for VARMA
    - $\vec{y}_t$, $\vec{y}_{t-1}$ was scalars, now these are vectors.
    - $\Phi_1$, $\Theta_1$ was scalars, now these are matrices. Also, these are in upper case.
    - Multiplication of matrices with the vectors give the result as vectors.
    - The matrices are squared matrices of size $D \times D$
    - The modified equation is still a linear model and the as same with ARMA, the first part is for auto-regressive model (VAR(p)) and the second part is for moving average model (VMA(q)).
    - p for VAR(p) stands for the past values of the time-series and q for VMA(q) stands for the past errors.

$$\large \vec{y_t} = \vec{b} + \Phi_1\vec{y}_{t-1} + ... + \Phi_p\vec{y}_{t-p} + \Theta_1 \vec{\varepsilon}_{t-1} + ... + \Theta_q\vec{\varepsilon}_{t-q} + \varepsilon_t$$

- Consider $VAR(p)$ in 2 dimensions (let p = 1 for simplicity)

$$\large \begin{vmatrix}y_t^{(1)} \\\ y_t^{(2)}\end{vmatrix} = \begin{vmatrix}b^{(1)}\\\b^{(2)}\end{vmatrix} + \begin{vmatrix}\phi_{11} & \phi_{12}\\\phi_{21} & \phi_{22}\end{vmatrix}\begin{vmatrix}y_{t-1}^{(1)}\\\y_{t-2}^{(2)}\end{vmatrix} + \begin{vmatrix}\varepsilon_t^{(1)}\\\ \varepsilon_t^{(2)}\end{vmatrix}$$

- Multiply it out and express both components in scalar form

$$\large y_{t}^{(1)} = b^{(1)} + \phi_{11}y_{t-1}^{(1)} + \phi_{12}y_{t-1}^{(2)} + \varepsilon_{t}^{(1)}$$

$$\large y_{t}^{(2)} = b^{(2)} + \phi_{21}y_{t-1}^{(1)} + \phi_{22}y_{t-1}^{(2)} + \varepsilon_{t}^{(2)}$$

- $VAR(1)$

$$\large y_{t}^{(1)} = b^{(1)} + \phi_{11}y_{t-1}^{(1)} + \phi_{12}y_{t-1}^{(2)} + \varepsilon_t^{(1)}$$

$$\large y_{t}^{(2)} = b^{(2)} + \phi_{21}y_{t-1}^{(1)} + \phi_{22}y_{t-1}^{(2)} + \varepsilon_t^{(2)}$$

- 2 separate $AR(1)$'s

$$\large y_t^{(1)} = b^{(1)} + \phi_{11}y_{t-1}^{(1)} + \varepsilon_t^{(1)}$$

$$\large y_t^{(2)} = b^{(2)} + \phi_{22}y_{t-1}^{(2)} + \varepsilon_t^{(2)}$$

-- more have to add

```python
## Code for VARMA(p, q)

# train is a matrix of TxD
model = VARMAX(train, order=(p, q))
res = model.fit(maxiter=100)

fcast = res.get_forecast(Ntest)

train_pred = fcast.predicted_mean # df with 'col1', ..., 'colD'

ci = fcast.conf_int()  # df with 'lower col1', 'upper col1', ...
```

```python
# code for VAR(p)
model = VAR(train)
lag_order_results = model.select_order(maxlags=15)
# returns LagOrderResults object
lag_order_results.selected_orders
# returns {'aic': 12, 'bic': 6, 'fpe': 12, 'hqic': 11}
results = model.fit(maxlags=15, ic="aic")
# returns VARResults object
lag_order = results.k_ar
prior = train.iloc[-lag_order:].to_numpy()
fcast = results.forecast(prior, Ntest) # numpy array
```
### Summary:
- VARMA(p, q) is just an extension of ARMA(p, q) to vectors
- Still linear; each component depends on lags of every other component
- VARMA is not identifiable
- VARMA takes longer to train
- Number of parameters grows quadratically with number of components
- This may lead to overfitting (too many parameters)
- VAR and VARMAX have a different API in statsmodels
- VAR has automatic order selection. 

## [Granger Causality](https://towardsdatascience.com/a-quick-introduction-on-granger-causality-testing-for-time-series-analysis-7113dc9420d2)

- The Granger causality test is used to determine whether one time series is useful in forecasting another.
- Note: not "true" causality.
- Granger causality is just mechanical: find a predictive relationship, not a causal relationship.
- Let's say given 2 stationary time series: { x(t) }, { y(t) }
- AR Model 1:

$$\large y(t) = b + \phi_1y(t-1) + ... \phi_py(t-p) + \varepsilon(t)$$

- Now we build again an AR model 2 but instead of only using the past values of $y(t)$ you also use arbitrary lags of $x(t)$.

$$\large y(t) = b + \phi_1y(t-1) + ... \phi_py(t-p) + \alpha_3x(t-3) + \alpha_7x(t-7) + \varepsilon(t)$$

- If any of the cross-coefficients ($\alpha_3$, $\alpha_7$) are statistically significant, then we say x(t) "Granger causes" y(t) - Note: you can pick any lags, these are just examples.
- Recall: in regression analysis, we determine whether or not a coefficient is statistically significant by testing if it's "big enough" (in magnitude).

![Example Granger Causality](../00%20-%20Images/image-9.png)

```python
df = dataframe containing 2 columns as time series
result = grangercausalitytests(df, maxlag=p)
```
