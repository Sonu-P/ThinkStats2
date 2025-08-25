## Module `code.chap01soln`

This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.chap01soln import *  # or import specific names
```

### Functions

- `CleanFemResp(df)`

Recodes variables from the respondent frame.

df: DataFrame

```python
from code.chap01soln import CleanFemResp
# Example usage:
result = CleanFemResp(...)  # fill in arguments
```

- `main(script)`

Tests the functions in this module.

script: string script name

```python
from code.chap01soln import main
# Example usage:
result = main(...)  # fill in arguments
```

- `ReadFemResp(dct_file=..., dat_file=..., nrows=...)`

Reads the NSFG respondent data.

dct_file: string file name
dat_file: string file name

returns: DataFrame

```python
from code.chap01soln import ReadFemResp
# Example usage:
result = ReadFemResp(...)  # fill in arguments
```

- `ValidatePregnum(resp)`

Validate pregnum in the respondent file.

resp: respondent DataFrame

```python
from code.chap01soln import ValidatePregnum
# Example usage:
result = ValidatePregnum(...)  # fill in arguments
```
