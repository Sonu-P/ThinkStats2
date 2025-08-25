## Module `code.regression`

This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.regression import *  # or import specific names
```

### Functions

- `FormatRow(results, columns)`

Converts regression results to a string.

results: RegressionResults object

returns: string

```python
from code.regression import FormatRow
# Example usage:
result = FormatRow(...)  # fill in arguments
```

- `GoMining(df)`

Searches for variables that predict birth weight.

df: DataFrame of pregnancy records

returns: list of (rsquared, variable name) pairs

```python
from code.regression import GoMining
# Example usage:
result = GoMining(...)  # fill in arguments
```

- `JoinFemResp(df)`

Reads the female respondent file and joins on caseid.

df: DataFrame

```python
from code.regression import JoinFemResp
# Example usage:
result = JoinFemResp(...)  # fill in arguments
```

- `LogisticRegressionExample()`

Runs a simple example of logistic regression and prints results.
    

```python
from code.regression import LogisticRegressionExample
# Example usage:
result = LogisticRegressionExample(...)  # fill in arguments
```

- `main(name, data_dir=...)`
```python
from code.regression import main
# Example usage:
result = main(...)  # fill in arguments
```

- `MiningReport(variables, n=...)`

Prints variables with the highest R^2.

t: list of (R^2, variable name) pairs
n: number of pairs to print

```python
from code.regression import MiningReport
# Example usage:
result = MiningReport(...)  # fill in arguments
```

- `PivotTables(live)`

Prints a pivot table comparing first babies to others.

live: DataFrame of live births

```python
from code.regression import PivotTables
# Example usage:
result = PivotTables(...)  # fill in arguments
```

- `PredictBirthWeight(live)`

Predicts birth weight of a baby at 30 weeks.

live: DataFrame of live births

```python
from code.regression import PredictBirthWeight
# Example usage:
result = PredictBirthWeight(...)  # fill in arguments
```

- `PrintTabular(rows, header)`

Prints results in LaTeX tabular format.

rows: list of rows
header: list of strings

```python
from code.regression import PrintTabular
# Example usage:
result = PrintTabular(...)  # fill in arguments
```

- `QuickLeastSquares(xs, ys)`

Estimates linear least squares fit and returns MSE.

xs: sequence of values
ys: sequence of values

returns: inter, slope, mse

```python
from code.regression import QuickLeastSquares
# Example usage:
result = QuickLeastSquares(...)  # fill in arguments
```

- `ReadVariables()`

Reads Stata dictionary files for NSFG data.

returns: DataFrame that maps variables names to descriptions

```python
from code.regression import ReadVariables
# Example usage:
result = ReadVariables(...)  # fill in arguments
```

- `RunLogisticModels(live)`

Runs regressions that predict sex.

live: DataFrame of pregnancy records

```python
from code.regression import RunLogisticModels
# Example usage:
result = RunLogisticModels(...)  # fill in arguments
```

- `RunModels(live)`

Runs regressions that predict birth weight.

live: DataFrame of pregnancy records

```python
from code.regression import RunModels
# Example usage:
result = RunModels(...)  # fill in arguments
```

- `RunSimpleRegression(live)`

Runs a simple regression and compare results to thinkstats2 functions.

live: DataFrame of live births

```python
from code.regression import RunSimpleRegression
# Example usage:
result = RunSimpleRegression(...)  # fill in arguments
```

- `SummarizeResults(results)`

Prints the most important parts of linear regression results:

results: RegressionResults object

```python
from code.regression import SummarizeResults
# Example usage:
result = SummarizeResults(...)  # fill in arguments
```
