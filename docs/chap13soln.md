## Module `code.chap13soln`

This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.chap13soln import *  # or import specific names
```

### Functions

- `CleanData(resp)`

Cleans respondent data.

resp: DataFrame

```python
from code.chap13soln import CleanData
# Example usage:
result = CleanData(...)  # fill in arguments
```

- `EstimateSurvival(resp)`

Estimates the survival curve.

resp: DataFrame of respondents

returns: pair of HazardFunction, SurvivalFunction

```python
from code.chap13soln import EstimateSurvival
# Example usage:
result = EstimateSurvival(...)  # fill in arguments
```

- `EstimateSurvivalByDecade(groups, **options)`

Groups respondents by decade and plots survival curves.

groups: GroupBy object

```python
from code.chap13soln import EstimateSurvivalByDecade
# Example usage:
result = EstimateSurvivalByDecade(...)  # fill in arguments
```

- `main()`
```python
from code.chap13soln import main
# Example usage:
result = main(...)  # fill in arguments
```

- `ResampleDivorceCurve(resps)`

Plots divorce curves based on resampled data.

resps: list of respondent DataFrames

```python
from code.chap13soln import ResampleDivorceCurve
# Example usage:
result = ResampleDivorceCurve(...)  # fill in arguments
```

- `ResampleDivorceCurveByDecade(resps)`

Plots divorce curves for each birth cohort.

resps: list of respondent DataFrames    

```python
from code.chap13soln import ResampleDivorceCurveByDecade
# Example usage:
result = ResampleDivorceCurveByDecade(...)  # fill in arguments
```
