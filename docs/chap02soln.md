## Module `code.chap02soln`

This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.chap02soln import *  # or import specific names
```

### Functions

- `AllModes(hist)`

Returns value-freq pairs in decreasing order of frequency.

hist: Hist object

returns: iterator of value-freq pairs

```python
from code.chap02soln import AllModes
# Example usage:
result = AllModes(...)  # fill in arguments
```

- `main(script)`

Tests the functions in this module.

script: string script name

```python
from code.chap02soln import main
# Example usage:
result = main(...)  # fill in arguments
```

- `Mode(hist)`

Returns the value with the highest frequency.

hist: Hist object

returns: value from Hist

```python
from code.chap02soln import Mode
# Example usage:
result = Mode(...)  # fill in arguments
```

- `WeightDifference(live, firsts, others)`

Explore the difference in weight between first babies and others.

live: DataFrame of all live births
firsts: DataFrame of first babies
others: DataFrame of others

```python
from code.chap02soln import WeightDifference
# Example usage:
result = WeightDifference(...)  # fill in arguments
```
