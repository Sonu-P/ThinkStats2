## Module `code.brfss`

This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.brfss import *  # or import specific names
```

### Functions

- `CleanBrfssFrame(df)`

Recodes BRFSS variables.

df: DataFrame

```python
from code.brfss import CleanBrfssFrame
# Example usage:
result = CleanBrfssFrame(...)  # fill in arguments
```

- `main(script, nrows=...)`

Tests the functions in this module.

script: string script name

```python
from code.brfss import main
# Example usage:
result = main(...)  # fill in arguments
```

- `MakeFigures(df)`

Generates CDFs and normal prob plots for weights and log weights.

```python
from code.brfss import MakeFigures
# Example usage:
result = MakeFigures(...)  # fill in arguments
```

- `MakeNormalModel(weights)`

Plots a CDF with a Normal model.

weights: sequence

```python
from code.brfss import MakeNormalModel
# Example usage:
result = MakeNormalModel(...)  # fill in arguments
```

- `MakeNormalPlot(weights)`

Generates a normal probability plot of birth weights.

weights: sequence

```python
from code.brfss import MakeNormalPlot
# Example usage:
result = MakeNormalPlot(...)  # fill in arguments
```

- `ReadBrfss(filename=..., compression=..., nrows=...)`

Reads the BRFSS data.

filename: string
compression: string
nrows: int number of rows to read, or None for all

returns: DataFrame

```python
from code.brfss import ReadBrfss
# Example usage:
result = ReadBrfss(...)  # fill in arguments
```

- `Summarize(df, column, title)`

Print summary statistics male, female and all.

```python
from code.brfss import Summarize
# Example usage:
result = Summarize(...)  # fill in arguments
```
