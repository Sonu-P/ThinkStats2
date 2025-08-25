## Module `code.chap07soln`

This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.chap07soln import *  # or import specific names
```

### Functions

- `BinnedPercentiles(df)`

Bin the data by age and plot percentiles of weight for each bin.

df: DataFrame

```python
from code.chap07soln import BinnedPercentiles
# Example usage:
result = BinnedPercentiles(...)  # fill in arguments
```

- `HexBin(ages, weights, bins=...)`

Make a hexbin plot and save it.

ages: sequence of float
weights: sequence of float
bins: 'log' or None for linear

```python
from code.chap07soln import HexBin
# Example usage:
result = HexBin(...)  # fill in arguments
```

- `main(script)`
```python
from code.chap07soln import main
# Example usage:
result = main(...)  # fill in arguments
```

- `ScatterPlot(ages, weights, alpha=...)`

Make a scatter plot and save it.

ages: sequence of float
weights: sequence of float
alpha: float

```python
from code.chap07soln import ScatterPlot
# Example usage:
result = ScatterPlot(...)  # fill in arguments
```
