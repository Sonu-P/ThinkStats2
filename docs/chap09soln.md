## Module `code.chap09soln`

This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.chap09soln import *  # or import specific names
```

### Functions

- `main()`
```python
from code.chap09soln import main
# Example usage:
result = main(...)  # fill in arguments
```

- `RunResampleTest(firsts, others)`

Tests differences in means by resampling.

firsts: DataFrame
others: DataFrame

```python
from code.chap09soln import RunResampleTest
# Example usage:
result = RunResampleTest(...)  # fill in arguments
```

- `RunTests(live, iters=...)`

Runs the tests from Chapter 9 with a subset of the data.

live: DataFrame
iters: how many iterations to run

```python
from code.chap09soln import RunTests
# Example usage:
result = RunTests(...)  # fill in arguments
```

### Classes

- `DiffMeansResample`

Tests a difference in means using resampling.

```python
from code.chap09soln import DiffMeansResample
obj = DiffMeansResample(...)  # construct with appropriate arguments
```

Methods:

  - `DiffMeansResample.RunModel(self)`

Run the model of the null hypothesis.

returns: simulated data

```python
# obj is an instance of DiffMeansResample
obj.RunModel(...)  # fill in arguments
```
