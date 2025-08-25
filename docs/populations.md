## Module `code.populations`

This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.populations import *  # or import specific names
```

### Functions

- `main()`
```python
from code.populations import main
# Example usage:
result = main(...)  # fill in arguments
```

- `MakeFigures()`

Plots the CDF of populations in several forms.

On a log-log scale the tail of the CCDF looks like a straight line,
which suggests a Pareto distribution, but that turns out to be misleading.

On a log-x scale the distribution has the characteristic sigmoid of
a lognormal distribution.

The normal probability plot of log(sizes) confirms that the data fit the
lognormal model very well.

Many phenomena that have been described with Pareto models can be described
as well, or better, with lognormal models.

```python
from code.populations import MakeFigures
# Example usage:
result = MakeFigures(...)  # fill in arguments
```

- `ReadData(filename=...)`

Reads filename and returns populations in thousands

filename: string

returns: pandas Series of populations in thousands

```python
from code.populations import ReadData
# Example usage:
result = ReadData(...)  # fill in arguments
```
