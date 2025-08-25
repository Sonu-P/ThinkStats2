## Module `code.chap03soln`

This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.chap03soln import *  # or import specific names
```

### Functions

- `Diffs(t)`

List of differences between the first elements and others.

t: list of numbers

returns: list of numbers

```python
from code.chap03soln import Diffs
# Example usage:
result = Diffs(...)  # fill in arguments
```

- `main(script)`

Tests the functions in this module.

script: string script name

```python
from code.chap03soln import main
# Example usage:
result = main(...)  # fill in arguments
```

- `PairWiseDifferences(live)`

Summarize pairwise differences for children of the same mother.

live: DataFrame of pregnancy records for live births

```python
from code.chap03soln import PairWiseDifferences
# Example usage:
result = PairWiseDifferences(...)  # fill in arguments
```

- `PmfMean(pmf)`

Computes the mean of a PMF.

Returns:
    float mean

```python
from code.chap03soln import PmfMean
# Example usage:
result = PmfMean(...)  # fill in arguments
```

- `PmfVar(pmf, mu=...)`

Computes the variance of a PMF.

Args:
    mu: the point around which the variance is computed;
        if omitted, computes the mean

Returns:
    float variance

```python
from code.chap03soln import PmfVar
# Example usage:
result = PmfVar(...)  # fill in arguments
```
