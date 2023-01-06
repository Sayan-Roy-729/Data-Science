# EDA Approach:

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