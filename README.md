# NumPy & Pandas Practice

Hands-on exercises while learning NumPy and Pandas as part of my AI/ML journey.

| Notebook | Topic |
|---|---|
| `02_pandas_numpy_dtype_loc_indexing.ipynb` | Reshaping & descending sort with NumPy (`np.sort()` + reverse slicing); dict → DataFrame conversion; `.loc` row lookup; `type()` vs `.dtype` on a Pandas column |
| `03_pandas_groupby_fillna_map.ipynb` | Filling missing values with a per-group average using `groupby().mean()` + `Series.map()`; why `fillna(other_series)` aligns by index label, not category; correct order of `fillna` → `groupby().sum()` |

### What this covers
- Reshaping a flat list into a 2D NumPy array with `.reshape()`
- Sorting descending using `np.sort()` combined with reverse slicing (`[::-1]`) instead of a manual loop
- Why `.loc` only works on a Pandas DataFrame, not a raw NumPy array
- The difference between `type(df["col"])` (always returns `Series`) and `df["col"].dtype` (the actual dtype of the values inside, e.g. `object` for text columns)
- Why `Series.fillna(other_series)` aligns by index label and silently fills nothing if the indexes don't match (e.g. filling row-indexed data with a category-indexed `groupby().mean()` result)
- Using `Series.map()` to translate a column of labels into per-row values from a lookup Series/dict, producing a result aligned to the original row index
- Why `fillna()` returns a new Series instead of modifying in place, and why the result must be reassigned
- Filling missing values *before* aggregating with `groupby().sum()`, not after
