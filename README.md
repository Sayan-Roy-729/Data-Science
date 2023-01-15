# EDA Approach:

## <span id="index">**Index:**</span>
1. [Data Types in Statistics](https://github.com/Sayan-Roy-729/Data-Science#data-types-in-statistics-go-to-top)
2. [Measures of Central Tendency](https://github.com/Sayan-Roy-729/Data-Science#measures-of-central-tendencyestimates-of-location-go-to-top)
    1. [Mean](https://github.com/Sayan-Roy-729/Data-Science#mean-go-to-top)
    2. [Trimmed Mean](https://github.com/Sayan-Roy-729/Data-Science#trimmed-mean-go-to-top)
    3. [Weighted Mean](https://github.com/Sayan-Roy-729/Data-Science#weighted-mean-go-to-top)
    4. [Median](https://github.com/Sayan-Roy-729/Data-Science#median-go-to-top)
    5. [Mode](https://github.com/Sayan-Roy-729/Data-Science#mode-go-to-top)
    6. [Expected Value](https://github.com/Sayan-Roy-729/Data-Science#expected-value-go-to-top)
3. [Measures of Dispersion](https://github.com/Sayan-Roy-729/Data-Science#measures-of-dispersionvariability-go-to-top)
    1. [Mean Absolute Deviation (MAD)](https://github.com/Sayan-Roy-729/Data-Science#mean-absolute-deviation-mad-go-to-top)
    2. [Variance & Standard Deviation](https://github.com/Sayan-Roy-729/Data-Science#variance--standard-deviation-go-to-top)
    3. [Mean Absolute Variance](https://github.com/Sayan-Roy-729/Data-Science#median-absolute-variance-go-to-top)
    4. [Range](https://github.com/Sayan-Roy-729/Data-Science#range-go-to-top)
    5. [Percentile & IQR](https://github.com/Sayan-Roy-729/Data-Science#percentile--iqr-go-to-top)
4. [Visualization](https://github.com/Sayan-Roy-729/Data-Science#visualization-go-to-top)
    1. [Boxplot](https://github.com/Sayan-Roy-729/Data-Science#boxplot-go-to-top)
    2. [Histogram](https://github.com/Sayan-Roy-729/Data-Science#histogram-go-to-top)
    3. [Density/KDE Plot](https://github.com/Sayan-Roy-729/Data-Science#densitykde-plot-go-to-top)
    4. [Bar chart](https://github.com/Sayan-Roy-729/Data-Science#bar-chart-go-to-top)
    5. [Scatter plot](https://github.com/Sayan-Roy-729/Data-Science#scatter-plots-go-to-top)
    6. [Hexagonal Binning Plot](https://github.com/Sayan-Roy-729/Data-Science#hexagonal-binning-plot-go-to-top)
    7. [Contour Plot](https://github.com/Sayan-Roy-729/Data-Science#contour-plot-go-to-top)
    8. [Heat Maps](https://github.com/Sayan-Roy-729/Data-Science#heat-maps-go-to-top)
    9. [Violin Plot](https://github.com/Sayan-Roy-729/Data-Science#violin-plot-go-to-top)
5. [Correlation](https://github.com/Sayan-Roy-729/Data-Science#correlation-go-to-top)
6. [Pivot Table](https://github.com/Sayan-Roy-729/Data-Science#pivot-table-go-to-top)
7. [Some more Statistical Concepts](https://github.com/Sayan-Roy-729/Data-Science#some-more-statistical-concepts-go-to-top)

    1. [Random Sampling](https://github.com/Sayan-Roy-729/Data-Science#random-sampling-go-to-top)
    2. [Statistical Bias](https://github.com/Sayan-Roy-729/Data-Science#statistical-bias-go-to-top)
    3. [Selection Bias](https://github.com/Sayan-Roy-729/Data-Science#selection-bias-go-to-top)
    4. [Central Limit Theorem / Sampling Distribution](https://github.com/Sayan-Roy-729/Data-Science#central-limit-theorem--sampling-distribution-go-to-top)
    5. [Standard Error](https://github.com/Sayan-Roy-729/Data-Science#standard-error-go-to-top)
    6. [Bootstrapping](https://github.com/Sayan-Roy-729/Data-Science#bootstrapping-go-to-top)
    7. [Confidence Interval (CI)](https://github.com/Sayan-Roy-729/Data-Science#confidence-interval-ci-go-to-top)

---

## **Data Types in Statistics:** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

Generally 2 types of data types we can see in Data-Science.
- **`Numeric`**: Data that are expressed on a numeric scale.
    - **Continuous**: Data that can take on any value in an interval.
    - **Discrete:** Data that can take on only integer values, such as counts
- **`Categorical`**: Data that can take on only a specofic set of values representing a set of possible categories.
    - **Binary**: A special case of categorical data with just two categories of values e.g., 0/1, true/false.
    - **Ordinal**: Categorical data that has an explicit ordering.

---

## **Measures of Central Tendency/Estimates of Location:** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

### **Mean:** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

$$\large \bar{x} = \frac{\sum_{i=1}^{n}{x_i}}{n}$$

```python
DataFrame.mean()
```

### **Trimmed Mean:** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

A variation of the mean is a trimmed mean which you calculate by dropping a fixed number of sorted values at each end and then taking an average of the remaining values.

The formula to compute the trimmed mean with $p$ smallest and largest values omitted is:
$$\large \bar{x} = \frac{\sum_{i = p+1}^{n-p}{x_i}}{n - 2p}$$

```python
import scipy.stats as stats

# 0.1 means drop 10% from each end.
stats.trim_mean(column_name, 0.1)
```

### **Weighted Mean**: <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

$$\large \bar{x_w} = \frac{\sum_{i=1}^{n}{w_ix_i}}{\sum_{i=1}^{n}{w_i}}$$

```python
import numpy as np

np.average(DataFrame.column, weights=DataFrame.another_column)
```

### **Median:** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

Compared to mean, which uses all the observations, the median depends only on the values in the center of the sorted data. It is also possible to compute the *weighted median*.

```python
DataFrame.median()
```
For weighted median, you can use the specialized package `wquantiles`.
```python
wquantiles.median(DataFrame.column, weights=DataFrame.another_column)
```

### **Mode:** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

The mode is the value - or values in case of a tie - that appears most often in the data. The mode is a simple summary statistics for categorical data, and it is generally not used for numeric data.

### **Expected Value:** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

l data is data in which the categories represent or can be mapped to discrete values on the same scale. A marketer for a new cloud technology, for example, offers two levels of service, one priced at $300/month and another at $50/month. The marketer offers free webinars to generate leads, and the firm figures that 5% of the attendees will sign up for the $300 service, 15% will sign up for the $50 service and rest 80% will not sign up for anything. This data can be summed up, for financial purpose, in a single "*expected value*," which is a form of weighted mean, in which the weights are probabilities. So, expected values are:

$\large EV = 0.05 * 300 + 0.15 * 50 + 0.80 * 0 = 22.5$

In that cloud service example, the expected value of a webinar attendee is thus $22.50 per month.

## **Measures of Dispersion/Variability:** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

### **Mean Absolute Deviation (MAD):** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

$$\large MAD = \frac{\sum_{i=1}^{n}|x_i - \bar{x}|}{n}$$

### **Variance & Standard Deviation:** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

$$\large Variance \ (s^2) = \frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n-1}$$

$$\large STD \ (s) = \sqrt{s^2} = \sqrt{\frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n-1}}$$

```python
# STD calculation
DataFrame.std()
```

### **Median Absolute Variance:** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

$$\large Median \ Absolute \ Variance = Median(|x_1 - m|, |x_2 - m|, ..., |x_n - m|)$$

where $m$ is the median.

### **Range:** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

The difference between the largest and the smallest numbers. The minimum and maximum values themselves are useful to know and are helpful in identifying outliers. But the *range* is extremely sensitive to outliers and not very useful as a general measure of dispersion in the data.

### **Percentile | IQR:** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>
In a dataset, the $P$ th percentile is a value such that at least $P$ percent of the values take on this value or less and at least $(100-P)$ percent of the values take on this value or more.

The $median$ is the same thing as the 50th percentile. A common measurement of variability is the difference between the 25th percentile and the 75th percentile, called **Interquartile Range (IQR)**. For very large datasets, calculating exact percentiles can be computationally very expensive since it requires sorting all the data values.

```python
# calculate IQR
DataFrame[column_name].quantile(0.75) - DataFrame[column_name].quantile(0.25)
```

---

## **Visualization:** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

### **Boxplot:** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

```python
DataFrame[column_name].plot.box()
```

<img src="https://cdn1.byjus.com/wp-content/uploads/2020/10/Box-Plot-and-Whisker-Plot-2.png" alt="BoxPlot of Normal Distribution" width=500 heigh=auto/>

Boxplots are a simple way to visually compare the distributions of a numeric variable grouped accordingly to a categorical variable. The *pandas* boxplot method takes the `by` argument that splits the data set into groups and creates the individual boxplots:

```python
ax = DataFrame.boxplot(by=category_col_1, column=numeric_col_1)
ax.set_xlabel(category_col_1)
ax.set_ylabel(numeric_col_1)
```

<img src="https://www.itl.nist.gov/div898/handbook/eda/gif/boxplot0.gif" alt="Boxplot with categorical and numerical variables" width=500/>

### **Histogram:** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

```python
ax = DataFrame[column_name].plot.hist(figsize=(4,4))
ax.set_xlabel("Some label based on X-Axis)
```
<img src="https://statistics.laerd.com/statistical-guides/img/uh/laerd-statistics-example-histogram-frequencies-for-age.png" alt="Histogram" width=500 heigh=auto/>

### **Density/KDE Plot:** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

```python
ax = DataFrame[column_name].plot.hist(density=True)
DataFrame[column_name].plot.density(ax=ax)
ax.set_xlabel("Set some label of X-axis)
```

<img src="https://www.askpython.com/wp-content/uploads/2020/10/Density-plot-with-Histogram-1024x512.jpeg" width=500 alt="Density/KDE Plot"/>

### **Bar chart:** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

Note that a bar chart resembles a histogram; in a bar chart the x-axis represents different categories of a factor variable, while in a histogram the x-axis represents values of a single variable on a numeric scale. In a histogram, the bars are typically shown touching each other, with gaps indicating values that did not occur in the data. In a bar chart, the bars are shown separate from one another.

```python
ax = DataFrame[column_name].plot.bar(figsize = (4, 4), legend=False)
ax.set_xlable("Set some x-axis label")
ax.set_ylabel("Count")
```
<img src="https://www.tutorialspoint.com/matplotlib/images/matplotlib_bar_plot.jpg" width=500 alt="Bar chart"/>

### **Scatter plots:** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

The standard way to visualize the relationship between two measured data variables is with a scatter plot. The x-axis represents one variables and the y-axis represents another, each point on the graph is a record.

Scatter plots are fine when there is a relatively small number of data values. For data sets with hundred of thousands or millions of records, a scatter plot will be too dense to identify the details of the data. 

```python
ax = DataFrame.plot.scatter(x=column_name_1, y=column_name_2, figsize=(4, 4), marker='$\u25EF$')
ax.set_xlabel(column_name_1)
ax.set_ylabel(column_name_2)
ax.axhline(0, color="grey", lw=1)
ax.axvline(0, color="grey", lw=1)
```

<img src="https://www.tibco.com/sites/tibco/files/media_entity/2022-01/scatter-chart-example.svg" alt="Scatter Plot" width=500/>

### **Hexagonal Binning Plot:** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

This plot is the solution of the disadvantages of scatter plot. Rather than plotting points, which would appear as a monolithic dark cloud, we can group the records into hexagonal bins and then can plot that hexagons with a color indicating the number of records in that bin.

```python
ax = DataFrame.plot.hexbin(x=column_name_1, y=column_name_2, gridsize=30, sharex=False, figsize=(5, 4))
ax.set_xlabel(column_name_1)
ax.set_ylabel(column_name_2)
```

<img src="https://pandas.pydata.org/docs/_images/pandas-DataFrame-plot-hexbin-1.png" alt="Hexagonal Binning Plot" width=500/>

### **Contour Plot:** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

Another solution of the disadvantages of scatter plot. The contour plot overlaid onto a scatter plot to visualize the relationship between two numeric variables. The contours are essentially a topographical map to two variables; each contour band represents a specific density of points, increasing as one nears a "peak".

```python
import seaborn as sns

ax = sns.kdeplot(DataFrame[column_name_1], DataFrame[column_name_2], ax=ax)
ax.set_xlabel(column_name_1)
ax.set_ylabel(column_name_2)
```

<img src="https://www.wavemetrics.com/sites/www.wavemetrics.com/files/contourlabels2.png" alt="Contour Plot" width=500/>

### **Heat Maps:** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

Another solution of the disadvantages of the scatter plot.

<img src="https://www.displayr.com/wp-content/uploads/2018/09/rat-burrough-heatmap-1.png" alt="Heat Map" width=500/>

### **Violin Plot:** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

A violin plot is an enhancement to the boxplot and plots the density estimate with the density on the y-axis. The density is mirrored and flipped over, and the resulting shape is filled in, creating an image resembling a violin. The advantage of a violin plot is that it can show nuances in the distribution that aren't perceptible in a boxplot. On the other hand, the boxplot more clearly shows the outliers in the data.

```python
import seaborn as sns

ax = sns.violineplot(DataFrame[categorical_col_1], DataFrame[numerical_col_1], inner="quartile", color="white")
ax.set_xlabel(categorical_col_1)
ax.set_ylabel(numerical_col_1)
```

<img src="https://miro.medium.com/max/1040/1*TTMOaNG1o4PgQd-e8LurMg.png" width=500 alt="Comparison between Box-Plot and Violin Plot"/>

---

## **Correlation:** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

Variables $X$ and $Y$ (each with measured data) are said to be *`positively correlated`* if high values of $X$ go with high values of $Y and low values of $X$ go to with low values of $Y. If high values of $X go with low values of $Y, and vice versa, the variables are *`negatively correlated`*.

- **`Correlation coefficient`:** A metric that measures the extent to which numeric variables are associated with one another (ranges from -1 to +1)
- **`Correlation matrix`:** A table where the variables are shown on both rows and columns, and the cell values are the correlations between the variables.

$$Pearson's \ correlation \ coefficient \ (r) = \frac{\sum_{i=1
}^{n}{(x_i - \bar{x})(y_i - \bar{y})}}{(n-1)s_xs_y}$$

```python
import seaborn as sns

sns.heatmap(DataFrame.corr(), vmin=-1, vmax=1, cmap=sns.diverging_palette(20, 220, as_cmap=True))
```

Like the `mean` and `standard deviation`, the correlation coefficient is sensitive to outliers in the data. `Spearman's rho` and `Kendall's tau` correlation techniques are based on the rank of the data and these are robust to outliers and can handle certain types of nonlinearities.

---

## **Pivot Table:** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

Whether the correlation coefficient helps to measure between two numeric columns, pivot table helps to measure between two categorical columns.

```python
crosstab = DataFrame.pivot_table(index=category_col_1, columns=category_col_2, aggfunc=lambda x: len(x), margins=True)
crosstab
```

# **Some more Statistical Concepts:** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

## **Random Sampling** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

*Random Sampling* is the process in which each available member of the population being sampled has an equal chance of being chosen for the sample at each draw. The sample that results is called a *`simple random sample`*. Sampling can be down **`with replacement`**, in which observations are put back in the population after each draw for possible future reselection. Or it can be done **`without replacement`**, in which case observations once selected are unavailable for future draws.

In **`stratified sampling`**, the population is divided up into *`strata`*, and random samples are taken from each stratum.

## **Statistical Bias:** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

Statistical bias refers to measurement or sampling errors that are *`systematic`* and *`produced by the measurement`* or *`sampling process`*. 

Consider the physical process of a gun shooting at a target. It will not hit the absolute center of the target every time or even much at all. An unbiased process will produce error, but it is random and does not tend strongly in any direction. 

Bias comes in different forms, may be `observable` or `invisible`. When a result does suggest bias, it is often an indicator that a statistical or machine learning model has been misspecified or an important variable left out.

## **Selection Bias:** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

Selection bias refers to the practice of selectively choosing data - consciously or unconsciously - in a way that leads to a conclusion that is misleading or ephemeral.

`Data snooping` is extensive hunting through the data until something interesting emerges. There is a saying among statisticians: "If you torture the data long enough, sooner or later it will confess."

If you repeatedly run different models and ask different questions with a large data set, you are bound to find something interesting. This is called `vast search effect.`

## **Central Limit Theorem / Sampling Distribution:** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

The statistics (e.g., mean) drawn from multiple samples will resemble the familiar bell-shaped normal curve, even if the source population is not normally distributed, provided that the sample size is large enough and the departure of the data from normality is not too great.

## **Standard Error:** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

The standard error is a single metric that sums up the variability in the sampling distribution for a statistics.

$$Standard \ Error \ (SE) = \frac{std}{\sqrt{sample \ size}} = \frac{s}{\sqrt{n}}$$

Consider the following approach to measuring standard error:
1. Collect a number of brand-new samples from the population.
2. For each new sample, calculate the statistics (e.g., mean)
3. Calculate the standard deviation of the statistics computed in step 2; use this as your estimate of standard error.

## **Bootstrapping:** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

One easy and effective way to estimate the sampling distribution of a statistics, or of model parameters is to draw additional `samples, with replacement` from the sample itself and recalculate the statistics or model for each resample. This procedure is called **`bootstrap`**. It does not necessarily involve any assumptions about the data or the sample statistics being normally distributed. 

The algorithm for a bootstrap resampling of the mean, for a sample of size $n$, is as follows:
1. Draw a sample value, record it and then replace it.
2. Repeat $n$ times.
3. Record the mean of the $n$ resampled values.
4. Repeat steps 1-3 $R$ times.
5. Use the $R$ results to:
    1. Calculate their standard deviation (this estimates sample mean standard error).
    2. Procedure a histogram or boxplot.
    3. Find a confidence interval.

```python
from sklearn.utils import resample

results = []
for nrepeat in range(1000):
    sample = resample(DataFrame[column_name])
    results.append(sample.mean())

results = pd.Series(results)
print('Bootstrap Statistics:')
print(f'original: {DataFrame[column_name].median()}')
print(f"bias: {results.median() - DataFrame[column_name].median()}")
print(f"std. error: {results.std()}")
```

## **Confidence Interval (CI):** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

Confidence intervals always come with a coverage level, expressed as a (high) percentage, say 90% or 95%. One way to think of a 90% confidence interval is as follows: it is the interval that encloses the central 90% of the bootstrap sampling distribution of a sample statistic. More generally, an $x\%$ confidence interval around a sample estimate should, on average, contain similar sample estimates $x\%$ of the time.

Given a sample of size $n$, and a sample statistic of interest, the algorithm for a bootstrap confidence interval is as follows:
1. Draw a random sample of size $n$ with replacement from the data (a resample).
2. Record the statistics of interest for the resample.
3. Repeat steps 1-2 many ($R$) times.
4. For an $x\%$ confidence interval, trim $[(100-x)/2]\%$ of the $R$ resample results from either end of the distribution.
5. The trim points are the endpoints of an $x\%$ bootstrap confidence interval.

The higher the level of confidence, the wider the interval. Also, the smaller the sample, the wider the interval (i.e., the greater the uncertainty).

## **Normal Distribution:** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

$$\large f(x) = \frac{1}{\sigma\sqrt{2\pi}}{e^{-\frac{1}{2}(\frac{x - \mu}{\sigma})^2}}$$

$f(x) = probability density function$

$\sigma = standard deviation$

$\mu = mean$

<img src="https://i.stack.imgur.com/jkMDV.png" width=500 alt="Normal Distribution"/>

### **Standardization / Z-Score** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

To compare the data to a standard normal distribution, you subtract the mean and then divided by the standard deviation. This is called *standardization* or *z-score*.

$$\large Z \ - Score = \frac{x_i - \bar{x}}{\sigma_x}$$

### **QQ-Plot:** <sup><sub>[**Go to top**](https://github.com/Sayan-Roy-729/Data-Science#index)</sub></sup>

A QQ - Plot is used to visually determine how close a sample specified distribution - in this case, the normal distribution.

```python
import scipy.stats as stats

fig, ax = plt.subplots(figsize=(4, 4))
norm_sample = stats.norm.rvs(size=100)
stats.probplot(norm_sample, plot=ax)
```

## **Long-Tailed Distribution:**

Sometimes, the distribution is highly skewed, such as with income data or the distribution can be discrete, as with binominal data. The long narrow portion of a frequency distribution, where relatively extreme values occur at low frequency.

<img src="https://i.stack.imgur.com/QCGKr.png" alt="Long-Tailed distribution" width=500/>
