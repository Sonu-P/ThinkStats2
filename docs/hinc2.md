## Module `code.hinc2`

This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.hinc2 import *  # or import specific names
```

### Functions

- `InterpolateSample(df, log_upper=...)`

Makes a sample of log10 household income.

Assumes that log10 income is uniform in each range.

df: DataFrame with columns income and freq
log_upper: log10 of the assumed upper bound for the highest range

returns: NumPy array of log10 household income

```python
from code.hinc2 import InterpolateSample
# Example usage:
result = InterpolateSample(...)  # fill in arguments
```

- `main()`
```python
from code.hinc2 import main
# Example usage:
result = main(...)  # fill in arguments
```
