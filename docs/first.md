## Module `code.first`

This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.first import *  # or import specific names
```

### Functions

- `main(script)`
```python
from code.first import main
# Example usage:
result = main(...)  # fill in arguments
```

- `MakeComparison(firsts, others)`

Plots histograms of pregnancy length for first babies and others.

firsts: DataFrame
others: DataFrame

```python
from code.first import MakeComparison
# Example usage:
result = MakeComparison(...)  # fill in arguments
```

- `MakeFrames()`

Reads pregnancy data and partitions first babies and others.

returns: DataFrames (all live births, first babies, others)

```python
from code.first import MakeFrames
# Example usage:
result = MakeFrames(...)  # fill in arguments
```

- `MakeHists(live)`

Plot Hists for live births

live: DataFrame
others: DataFrame

```python
from code.first import MakeHists
# Example usage:
result = MakeHists(...)  # fill in arguments
```

- `PrintExtremes(live)`

Plots the histogram of pregnancy lengths and prints the extremes.

live: DataFrame of live births

```python
from code.first import PrintExtremes
# Example usage:
result = PrintExtremes(...)  # fill in arguments
```

- `Summarize(live, firsts, others)`

Print various summary statistics.

```python
from code.first import Summarize
# Example usage:
result = Summarize(...)  # fill in arguments
```
