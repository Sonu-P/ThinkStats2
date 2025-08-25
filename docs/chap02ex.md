## Module `code.chap02ex`

This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.chap02ex import *  # or import specific names
```

### Functions

- `AllModes(hist)`

Returns value-freq pairs in decreasing order of frequency.

hist: Hist object

returns: iterator of value-freq pairs

```python
from code.chap02ex import AllModes
# Example usage:
result = AllModes(...)  # fill in arguments
```

- `main(script)`

Tests the functions in this module.

script: string script name

```python
from code.chap02ex import main
# Example usage:
result = main(...)  # fill in arguments
```

- `Mode(hist)`

Returns the value with the highest frequency.

hist: Hist object

returns: value from Hist

```python
from code.chap02ex import Mode
# Example usage:
result = Mode(...)  # fill in arguments
```
