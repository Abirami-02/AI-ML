# NumPy & Pandas Practice

Hands-on exercises while learning NumPy and Pandas as part of my AI/ML journey.

| Notebook | Topic |
|---|---|
| `02_pandas_numpy_dtype_loc_indexing.ipynb` | Reshaping & descending sort with NumPy (`np.sort()` + reverse slicing); dict → DataFrame conversion; `.loc` row lookup; `type()` vs `.dtype` on a Pandas column |

### What this covers
- Reshaping a flat list into a 2D NumPy array with `.reshape()`
- Sorting descending using `np.sort()` combined with reverse slicing (`[::-1]`) instead of a manual loop
- Why `.loc` only works on a Pandas DataFrame, not a raw NumPy array
- The difference between `type(df["col"])` (always returns `Series`) and `df["col"].dtype` (the actual dtype of the values inside, e.g. `object` for text columns)
