## Module `code.hinc`

This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.hinc import *  # or import specific names
```

### Functions

- `Clean(s)`

Converts dollar amounts to integers.

```python
from code.hinc import Clean
# Example usage:
result = Clean(...)  # fill in arguments
```

- `main()`
```python
from code.hinc import main
# Example usage:
result = main(...)  # fill in arguments
```

- `ReadData(filename=...)`

Reads filename and returns populations in thousands

filename: string

returns: pandas Series of populations in thousands

```python
from code.hinc import ReadData
# Example usage:
result = ReadData(...)  # fill in arguments
```
