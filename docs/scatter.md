## Module `code.scatter`

This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.scatter import *  # or import specific names
```

### Functions

- `BinnedPercentiles(df)`

Bin the data by height and plot percentiles of weight for eachbin.

df: DataFrame

```python
from code.scatter import BinnedPercentiles
# Example usage:
result = BinnedPercentiles(...)  # fill in arguments
```

- `Correlations(df)`
```python
from code.scatter import Correlations
# Example usage:
result = Correlations(...)  # fill in arguments
```

- `GetHeightWeight(df, hjitter=..., wjitter=...)`

Get sequences of height and weight.

df: DataFrame with htm3 and wtkg2
hjitter: float magnitude of random noise added to heights
wjitter: float magnitude of random noise added to weights

returns: tuple of sequences (heights, weights)

```python
from code.scatter import GetHeightWeight
# Example usage:
result = GetHeightWeight(...)  # fill in arguments
```

- `HexBin(heights, weights, bins=...)`

Make a hexbin plot and save it.

heights: sequence of float
weights: sequence of float
bins: 'log' or None for linear

```python
from code.scatter import HexBin
# Example usage:
result = HexBin(...)  # fill in arguments
```

- `main(script)`
```python
from code.scatter import main
# Example usage:
result = main(...)  # fill in arguments
```

- `MakeFigures(df)`

Make scatterplots.
    

```python
from code.scatter import MakeFigures
# Example usage:
result = MakeFigures(...)  # fill in arguments
```

- `ScatterPlot(heights, weights, alpha=...)`

Make a scatter plot and save it.

heights: sequence of float
weights: sequence of float
alpha: float

```python
from code.scatter import ScatterPlot
# Example usage:
result = ScatterPlot(...)  # fill in arguments
```
