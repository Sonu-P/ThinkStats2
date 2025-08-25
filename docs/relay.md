## Module `code.relay`

This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.relay import *  # or import specific names
```

### Functions

- `BinData(data, low, high, n)`

Rounds data off into bins.

data: sequence of numbers
low: low value
high: high value
n: number of bins

returns: sequence of numbers

```python
from code.relay import BinData
# Example usage:
result = BinData(...)  # fill in arguments
```

- `CleanLine(line)`

Converts a line from coolrunning results to a tuple of values.

```python
from code.relay import CleanLine
# Example usage:
result = CleanLine(...)  # fill in arguments
```

- `ConvertPaceToSpeed(pace)`

Converts pace in MM:SS per mile to MPH.

```python
from code.relay import ConvertPaceToSpeed
# Example usage:
result = ConvertPaceToSpeed(...)  # fill in arguments
```

- `GetSpeeds(results, column=...)`

Extract the pace column and return a list of speeds in MPH.

```python
from code.relay import GetSpeeds
# Example usage:
result = GetSpeeds(...)  # fill in arguments
```

- `main()`
```python
from code.relay import main
# Example usage:
result = main(...)  # fill in arguments
```

- `ReadResults(filename=...)`

Read results from a file and return a list of tuples.

```python
from code.relay import ReadResults
# Example usage:
result = ReadResults(...)  # fill in arguments
```
