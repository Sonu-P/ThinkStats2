## Module `code.hinc_soln`

This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.hinc_soln import *  # or import specific names
```

### Functions

- `main()`
```python
from code.hinc_soln import main
# Example usage:
result = main(...)  # fill in arguments
```

- `MakeFigures(df)`

Plots the CDF of income in several forms.
    

```python
from code.hinc_soln import MakeFigures
# Example usage:
result = MakeFigures(...)  # fill in arguments
```

### Classes

- `SmoothCdf`

Represents a CDF based on calculated quantiles.
    

```python
from code.hinc_soln import SmoothCdf
obj = SmoothCdf(...)  # construct with appropriate arguments
```

Methods:

  - `SmoothCdf.Render(self)`

Because this CDF was not computed from a sample, it
should not be rendered as a step function.

```python
# obj is an instance of SmoothCdf
obj.Render(...)  # fill in arguments
```

  - `SmoothCdf.Prob(self, x)`

Compute CDF(x), interpolating between known values.
        

```python
# obj is an instance of SmoothCdf
obj.Prob(...)  # fill in arguments
```

  - `SmoothCdf.Value(self, p)`

Compute inverse CDF(x), interpolating between probabilities.
        

```python
# obj is an instance of SmoothCdf
obj.Value(...)  # fill in arguments
```
