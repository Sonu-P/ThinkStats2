## Module `code.nsfg`

This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.nsfg import *  # or import specific names
```

### Functions

- `CleanFemPreg(df)`

Recodes variables from the pregnancy frame.

df: DataFrame

```python
from code.nsfg import CleanFemPreg
# Example usage:
result = CleanFemPreg(...)  # fill in arguments
```

- `CleanFemResp(df)`

Recodes variables from the respondent frame.

df: DataFrame

```python
from code.nsfg import CleanFemResp
# Example usage:
result = CleanFemResp(...)  # fill in arguments
```

- `main(script)`

Tests the functions in this module.

script: string script name

```python
from code.nsfg import main
# Example usage:
result = main(...)  # fill in arguments
```

- `MakePregMap(df)`

Make a map from caseid to list of preg indices.

df: DataFrame

returns: dict that maps from caseid to list of indices into \`preg\`

```python
from code.nsfg import MakePregMap
# Example usage:
result = MakePregMap(...)  # fill in arguments
```

- `ReadFemPreg(dct_file=..., dat_file=...)`

Reads the NSFG pregnancy data.

dct_file: string file name
dat_file: string file name

returns: DataFrame

```python
from code.nsfg import ReadFemPreg
# Example usage:
result = ReadFemPreg(...)  # fill in arguments
```

- `ReadFemResp(dct_file=..., dat_file=..., nrows=...)`

Reads the NSFG respondent data.

dct_file: string file name
dat_file: string file name

returns: DataFrame

```python
from code.nsfg import ReadFemResp
# Example usage:
result = ReadFemResp(...)  # fill in arguments
```

- `ValidatePregnum(resp, preg)`

Validate pregnum in the respondent file.

resp: respondent DataFrame
preg: pregnancy DataFrame

```python
from code.nsfg import ValidatePregnum
# Example usage:
result = ValidatePregnum(...)  # fill in arguments
```
