## Module `code.chap12soln`

This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.chap12soln import *  # or import specific names
```

### Functions

- `main(name)`
```python
from code.chap12soln import main
# Example usage:
result = main(...)  # fill in arguments
```

- `PlotEwmaPredictions(daily, name)`

    

```python
from code.chap12soln import PlotEwmaPredictions
# Example usage:
result = PlotEwmaPredictions(...)  # fill in arguments
```

- `PlotQuadraticModel(daily, name)`

    

```python
from code.chap12soln import PlotQuadraticModel
# Example usage:
result = PlotQuadraticModel(...)  # fill in arguments
```

- `RunQuadraticModel(daily)`

Runs a linear model of prices versus years.

daily: DataFrame of daily prices

returns: model, results

```python
from code.chap12soln import RunQuadraticModel
# Example usage:
result = RunQuadraticModel(...)  # fill in arguments
```

- `TestSerialCorr(daily)`

Tests serial correlations in daily prices and their residuals.

daily: DataFrame of daily prices

```python
from code.chap12soln import TestSerialCorr
# Example usage:
result = TestSerialCorr(...)  # fill in arguments
```

### Classes

- `SerialCorrelationTest`

Tests serial correlations by permutation.

```python
from code.chap12soln import SerialCorrelationTest
obj = SerialCorrelationTest(...)  # construct with appropriate arguments
```

Methods:

  - `SerialCorrelationTest.TestStatistic(self, data)`

Computes the test statistic.

data: tuple of xs and ys

```python
# obj is an instance of SerialCorrelationTest
obj.TestStatistic(...)  # fill in arguments
```

  - `SerialCorrelationTest.RunModel(self)`

Run the model of the null hypothesis.

returns: simulated data

```python
# obj is an instance of SerialCorrelationTest
obj.RunModel(...)  # fill in arguments
```
