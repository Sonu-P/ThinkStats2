## Module `code.density`

This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.density import *  # or import specific names
```

### Functions

- `ComputeSkewnesses()`

Plots KDE of birthweight and adult weight.
    

```python
from code.density import ComputeSkewnesses
# Example usage:
result = ComputeSkewnesses(...)  # fill in arguments
```

- `main()`
```python
from code.density import main
# Example usage:
result = main(...)  # fill in arguments
```

- `MakePdfExample(n=...)`

Plots a normal density function and a KDE estimate.

n: sample size

```python
from code.density import MakePdfExample
# Example usage:
result = MakePdfExample(...)  # fill in arguments
```

- `Summarize(data)`

Prints summary statistics.

data: pandas Series

```python
from code.density import Summarize
# Example usage:
result = Summarize(...)  # fill in arguments
```
