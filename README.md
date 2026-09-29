# NumPy, Pandas & Data Visualization Practice

Hands-on exercises while learning NumPy, Pandas, Matplotlib and Seaborn as part of my AI/ML journey.

## Notebooks

| Notebook | Topic |
|---|---|
| `02_pandas_numpy_dtype_loc_indexing.ipynb` | Reshaping & descending sort with NumPy (`np.sort()` + reverse slicing); dict → DataFrame conversion; `.loc` row lookup; `type()` vs `.dtype` on a Pandas column |
| `03_pandas_groupby_fillna_map.ipynb` | Filling missing values with a per-group average using `groupby().mean()` + `Series.map()`; why `fillna(other_series)` aligns by index label, not category; correct order of `fillna` → `groupby().sum()` |
| `04_matplotlib_seaborn_bar_lineplot.ipynb` | Matplotlib bar chart of total sales per branch; Seaborn `lineplot` with `hue` for the weekly trend per branch; how Matplotlib and Seaborn work together |

## What this covers

- Reshaping a flat list into a 2D NumPy array with `.reshape()`
- Sorting descending using `np.sort()` combined with reverse slicing (`[::-1]`) instead of a manual loop
- Why `.loc` only works on a Pandas DataFrame, not a raw NumPy array
- The difference between `type(df["col"])` (always returns `Series`) and `df["col"].dtype` (the actual dtype of the values inside, e.g. `object` for text columns)
- Why `Series.fillna(other_series)` aligns by index label and silently fills nothing if the indexes don't match
- Using `Series.map()` to translate a column of labels into per-row values from a lookup Series/dict
- Why `fillna()` returns a new Series instead of modifying in place, and why the result must be reassigned
- Filling missing values *before* aggregating with `groupby().sum()`, not after
- Aggregating with `groupby('branch')['sales'].sum().reset_index()` to get a plain DataFrame ready for plotting
- Building a labeled Matplotlib bar chart and a Seaborn line plot with one line per category (`hue`)

---

## Data Visualization: Key Concepts

### 1. Seaborn has many plotting functions

`sns.lineplot` is one of many. Common ones:

| Function | Use it for |
|---|---|
| `sns.lineplot` | Trend over time or an ordered x-axis |
| `sns.barplot` | Compare a value across categories |
| `sns.scatterplot` | Relationship between two numeric columns |
| `sns.histplot` | Distribution of one numeric column |
| `sns.boxplot` | Spread, median and outliers per category |
| `sns.heatmap` | A matrix of values shown as colours |

### 2. Why there is no `sns.title()`

Seaborn is a high-level library built **on top of Matplotlib**. Seaborn draws the plot (grouping, colours, legend), and Matplotlib handles the title, labels, ticks and display.

| Job | Library |
|---|---|
| Draw the plot from a DataFrame | Seaborn (`sns`) |
| Title, axis labels, ticks, `show()`, saving | Matplotlib (`plt`) |

```python
sns.lineplot(data=df, x='week', y='sales', hue='branch', marker='o')  # Seaborn draws
plt.title("Weekly sales by Branch")                                   # Matplotlib decorates
plt.show()                                                            # Matplotlib displays
```

---

## Seaborn `lineplot` Syntax

```python
sns.lineplot(data=df, x='week', y='sales', hue='branch', marker='o')
```

| Argument | Meaning |
|---|---|
| `data=df` | DataFrame to plot from |
| `x='week'`, `y='sales'` | Columns for the x and y axes |
| `hue='branch'` | One coloured line per branch, legend added automatically |
| `marker='o'` | Dot on every data point (optional) |

## Sample Data

```
branch,week,sales
Bangalore,1,15000
Bangalore,2,16200
Bangalore,3,15800
Chennai,1,18000
Chennai,2,17500
Chennai,3,19000
Pune,1,12000
Pune,2,12500
Pune,3,13100
```
