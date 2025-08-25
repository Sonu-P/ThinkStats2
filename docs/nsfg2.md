## Module `code.nsfg2`

This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.nsfg2 import *  # or import specific names
```

### Functions

- `CleanFemPreg(df)`

Recodes variables from the pregnancy frame.

df: DataFrame

```python
from code.nsfg2 import CleanFemPreg
# Example usage:
result = CleanFemPreg(...)  # fill in arguments
```

- `main()`
```python
from code.nsfg2 import main
# Example usage:
result = main(...)  # fill in arguments
```

- `MakeFrames()`

Reads pregnancy data and partitions first babies and others.

returns: DataFrames (all live births, first babies, others)

```python
from code.nsfg2 import MakeFrames
# Example usage:
result = MakeFrames(...)  # fill in arguments
```

- `ReadFemPreg(dct_file=..., dat_file=...)`

Reads the NSFG 2006-2010 pregnancy data.

dct_file: string file name
dat_file: string file name

returns: DataFrame

```python
from code.nsfg2 import ReadFemPreg
# Example usage:
result = ReadFemPreg(...)  # fill in arguments
```
