# EDA Approach:

## <span id="index">**Index:**</span>
1. [Data Types in Statistics](https://github.com/Sayan-Roy-729/Data-Science#data-types-in-statistics)
2. [Measures of Central Tendency](https://github.com/Sayan-Roy-729/Data-Science#measures-of-central-tendencyestimates-of-location)
    1. [Mean](https://github.com/Sayan-Roy-729/Data-Science#mean)
    2. [Trimmed Mean](https://github.com/Sayan-Roy-729/Data-Science#trimmed-mean)
    3. [Weighted Mean](https://github.com/Sayan-Roy-729/Data-Science#weighted-mean)
    4. [Median](https://github.com/Sayan-Roy-729/Data-Science#median)
3. [Measures of Dispersion](https://github.com/Sayan-Roy-729/Data-Science#measures-of-dispersionvariability)

## **Data Types in Statistics:**
Generally 2 types of data types we can see in Data-Science.
- **`Numeric`**: Data that are expressed on a numeric scale.
    - **Continuous**: Data that can take on any value in an interval.
    - **Discrete:** Data that can take on only integer values, such as counts
- **`Categorical`**: Data that can take on only a specofic set of values representing a set of possible categories.
    - **Binary**: A special case of categorical data with just two categories of values e.g., 0/1, true/false.
    - **Ordinal**: Categorical data that has an explicit ordering.

## Measures of Central Tendency/Estimates of Location:

### **Mean:**

$$\large \bar{x} = \frac{\sum_{i=1}^{n}{x_i}}{n}$$

```python
DataFrame.mean()
```

### **Trimmed Mean:**
A variation of the mean is a trimmed mean which you calculate by dropping a fixed number of sorted values at each end and then taking an average of the remaining values.

The formula to compute the trimmed mean with $p$ smallest and largest values omitted is:
$$\large \bar{x} = \frac{\sum_{i = p+1}^{n-p}{x_i}}{n - 2p}$$

```python
import scipy.stats as stats

# 0.1 means drop 10% from each end.
stats.trim_mean(column_name, 0.1)
```

### **Weighted Mean**:

$$\large \bar{x_w} = \frac{\sum_{i=1}^{n}{w_ix_i}}{\sum_{i=1}^{n}{w_i}}$$

```python
import numpy as np

np.average(DataFrame.column, weights=DataFrame.another_column)
```

### **Median:**

Compared to mean, which uses all the observations, the median depends only on the values in the center of the sorted data. It is also possible to compute the *weighted median*.

```python
DataFrame.median()
```
For weighted median, you can use the specialized package `wquantiles`.
```python
wquantiles.median(DataFrame.column, weights=DataFrame.another_column)
```

### **Mode:**
The mode is the value - or values in case of a tie - that appears most often in the data. The mode is a simple summary statistics for categorical data, and it is generally not used for numeric data.

### **Expected Value:**
A special type of categorical data is data in which the categories represent or can be mapped to discrete values on the same scale. A marketer for a new cloud technology, for example, offers two levels of service, one priced at $300/month and another at $50/month. The marketer offers free webinars to generate leads, and the firm figures that 5% of the attendees will sign up for the $300 service, 15% will sign up for the $50 service and rest 80% will not sign up for anything. This data can be summed up, for financial purpose, in a single "*expected value*," which is a form of weighted mean, in which the weights are probabilities. So, expected values are:

$\large EV = 0.05 * 300 + 0.15 * 50 + 0.80 * 0 = 22.5$

In that cloud service example, the expected value of a webinar attendee is thus $22.50 per month.

## **Measures of Dispersion/Variability:**

### **Mean Absolute Deviation (MAD):**

$$\large MAD = \frac{\sum_{i=1}^{n}|x_i - \bar{x}|}{n}$$

### **Variance & Standard Deviation:**

$$\large Variance \ (s^2) = \frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n-1}$$

$$\large STD \ (s) = \sqrt{s^2} = \sqrt{\frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n-1}}$$

```python
# STD calculation
DataFrame.std()
```

### **Median Absolute Variance:**

$$\large Median \ Absolute \ Variance = Median(|x_1 - m|, |x_2 - m|, ..., |x_n - m|)$$

where $m$ is the median.

### **Range:**

The difference between the largest and the smallest numbers. The minimum and maximum values themselves are useful to know and are helpful in identifying outliers. But the *range* is extremely sensitive to outliers and not very useful as a general measure of dispersion in the data.

### **Percentile | IQR:**
In a dataset, the $P$ th percentile is a value such that at least $P$ percent of the values take on this value or less and at least $(100-P)$ percent of the values take on this value or more.

The $median$ is the same thing as the 50th percentile. A common measurement of variability is the difference between the 25th percentile and the 75th percentile, called **Interquartile Range (IQR)**. For very large datasets, calculating exact percentiles can be computationally very expensive since it requires sorting all the data values.

```python
# calculate IQR
DataFrame[column_name].quantile(0.75) - DataFrame[column_name].quantile(0.25)
```

## **Visualization:**

### **Boxplot:**

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

### **Histogram:**

```python
ax = DataFrame[column_name].plot.hist(figsize=(4,4))
ax.set_xlabel("Some label based on X-Axis)
```
<img src="https://statistics.laerd.com/statistical-guides/img/uh/laerd-statistics-example-histogram-frequencies-for-age.png" alt="Histogram" width=500 heigh=auto/>

### **Density/KDE Plot:**

```python
ax = DataFrame[column_name].plot.hist(density=True)
DataFrame[column_name].plot.density(ax=ax)
ax.set_xlabel("Set some label of X-axis)
```

<img src="https://www.askpython.com/wp-content/uploads/2020/10/Density-plot-with-Histogram-1024x512.jpeg" width=500 alt="Density/KDE Plot"/>

### **Bar chart:**

Note that a bar chart resembles a histogram; in a bar chart the x-axis represents different categories of a factor variable, while in a histogram the x-axis represents values of a single variable on a numeric scale. In a histogram, the bars are typically shown touching each other, with gaps indicating values that did not occur in the data. In a bar chart, the bars are shown separate from one another.

```python
ax = DataFrame[column_name].plot.bar(figsize = (4, 4), legend=False)
ax.set_xlable("Set some x-axis label")
ax.set_ylabel("Count")
```
<img src="https://www.tutorialspoint.com/matplotlib/images/matplotlib_bar_plot.jpg" width=500 alt="Bar chart"/>

### **Scatter plots:**
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

### **Hexagonal Binning Plot:**

This plot is the solution of the disadvantages of scatter plot. Rather than plotting points, which would appear as a monolithic dark cloud, we can group the records into hexagonal bins and then can plot that hexagons with a color indicating the number of records in that bin.

```python
ax = DataFrame.plot.hexbin(x=column_name_1, y=column_name_2, gridsize=30, sharex=False, figsize=(5, 4))
ax.set_xlabel(column_name_1)
ax.set_ylabel(column_name_2)
```

<img src="https://pandas.pydata.org/docs/_images/pandas-DataFrame-plot-hexbin-1.png" alt="Hexagonal Binning Plot" width=500/>

### **Contour Plot:**
Another solution of the disadvantages of scatter plot. The contour plot overlaid onto a scatter plot to visualize the relationship between two numeric variables. The contours are essentially a topographical map to two variables; each contour band represents a specific density of points, increasing as one nears a "peak".

```python
import seaborn as sns

ax = sns.kdeplot(DataFrame[column_name_1], DataFrame[column_name_2], ax=ax)
ax.set_xlabel(column_name_1)
ax.set_ylabel(column_name_2)
```

<img src="https://www.wavemetrics.com/sites/www.wavemetrics.com/files/contourlabels2.png" alt="Contour Plot" width=500/>

### **Heat Maps:**
Another solution of the disadvantages of the scatter plot.

<img src="https://www.displayr.com/wp-content/uploads/2018/09/rat-burrough-heatmap-1.png" alt="Heat Map" width=500/>

### **Violin Plot:**

A violin plot is an enhancement to the boxplot and plots the density estimate with the density on the y-axis. The density is mirrored and flipped over, and the resulting shape is filled in, creating an image resembling a violin. The advantage of a violin plot is that it can show nuances in the distribution that aren't perceptible in a boxplot. On the other hand, the boxplot more clearly shows the outliers in the data.

```python
import seaborn as sns

ax = sns.violineplot(DataFrame[categorical_col_1], DataFrame[numerical_col_1], inner="quartile", color="white")
ax.set_xlabel(categorical_col_1)
ax.set_ylabel(numerical_col_1)
```

<img src="https://miro.medium.com/max/1040/1*TTMOaNG1o4PgQd-e8LurMg.png" width=500 alt="Comparison between Box-Plot and Violin Plot"/>

## **Correlation:**

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

## **Pivot Table:**

Whether the correlation coefficient helps to measure between two numeric columns, pivot table helps to measure between two categorical columns.

```python
crosstab = DataFrame.pivot_table(index=category_col_1, columns=category_col_2, aggfunc=lambda x: len(x), margins=True)
crosstab
```

