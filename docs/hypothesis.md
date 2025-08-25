## Module `code.hypothesis`

This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.hypothesis import *  # or import specific names
```

### Functions

- `FalseNegRate(data, num_runs=...)`

Computes the chance of a false negative based on resampling.

data: pair of sequences
num_runs: how many experiments to simulate

returns: float false negative rate

```python
from code.hypothesis import FalseNegRate
# Example usage:
result = FalseNegRate(...)  # fill in arguments
```

- `main()`
```python
from code.hypothesis import main
# Example usage:
result = main(...)  # fill in arguments
```

- `PrintTest(p_value, ht)`

Prints results from a hypothesis test.

p_value: float
ht: HypothesisTest

```python
from code.hypothesis import PrintTest
# Example usage:
result = PrintTest(...)  # fill in arguments
```

- `ReplicateTests()`

Replicates tests with the new NSFG data.

```python
from code.hypothesis import ReplicateTests
# Example usage:
result = ReplicateTests(...)  # fill in arguments
```

- `RunDiceTest()`

Tests whether a die is fair.
    

```python
from code.hypothesis import RunDiceTest
# Example usage:
result = RunDiceTest(...)  # fill in arguments
```

- `RunTests(data, iters=...)`

Runs several tests on the given data.

data: pair of sequences
iters: number of iterations to run

```python
from code.hypothesis import RunTests
# Example usage:
result = RunTests(...)  # fill in arguments
```

### Classes

- `CoinTest`

Tests the hypothesis that a coin is fair.

```python
from code.hypothesis import CoinTest
obj = CoinTest(...)  # construct with appropriate arguments
```

Methods:

  - `CoinTest.TestStatistic(self, data)`

Computes the test statistic.

data: data in whatever form is relevant        

```python
# obj is an instance of CoinTest
obj.TestStatistic(...)  # fill in arguments
```

  - `CoinTest.RunModel(self)`

Run the model of the null hypothesis.

returns: simulated data

```python
# obj is an instance of CoinTest
obj.RunModel(...)  # fill in arguments
```

- `CorrelationPermute`

Tests correlations by permutation.

```python
from code.hypothesis import CorrelationPermute
obj = CorrelationPermute(...)  # construct with appropriate arguments
```

Methods:

  - `CorrelationPermute.TestStatistic(self, data)`

Computes the test statistic.

data: tuple of xs and ys

```python
# obj is an instance of CorrelationPermute
obj.TestStatistic(...)  # fill in arguments
```

  - `CorrelationPermute.RunModel(self)`

Run the model of the null hypothesis.

returns: simulated data

```python
# obj is an instance of CorrelationPermute
obj.RunModel(...)  # fill in arguments
```

- `DiceChiTest`

Tests a six-sided die using a chi-squared statistic.

```python
from code.hypothesis import DiceChiTest
obj = DiceChiTest(...)  # construct with appropriate arguments
```

Methods:

  - `DiceChiTest.TestStatistic(self, data)`

Computes the test statistic.

data: list of frequencies

```python
# obj is an instance of DiceChiTest
obj.TestStatistic(...)  # fill in arguments
```

- `DiceTest`

Tests whether a six-sided die is fair.

```python
from code.hypothesis import DiceTest
obj = DiceTest(...)  # construct with appropriate arguments
```

Methods:

  - `DiceTest.TestStatistic(self, data)`

Computes the test statistic.

data: list of frequencies

```python
# obj is an instance of DiceTest
obj.TestStatistic(...)  # fill in arguments
```

  - `DiceTest.RunModel(self)`

Run the model of the null hypothesis.

returns: simulated data

```python
# obj is an instance of DiceTest
obj.RunModel(...)  # fill in arguments
```

- `DiffMeansOneSided`

Tests a one-sided difference in means by permutation.

```python
from code.hypothesis import DiffMeansOneSided
obj = DiffMeansOneSided(...)  # construct with appropriate arguments
```

Methods:

  - `DiffMeansOneSided.TestStatistic(self, data)`

Computes the test statistic.

data: data in whatever form is relevant        

```python
# obj is an instance of DiffMeansOneSided
obj.TestStatistic(...)  # fill in arguments
```

- `DiffMeansPermute`

Tests a difference in means by permutation.

```python
from code.hypothesis import DiffMeansPermute
obj = DiffMeansPermute(...)  # construct with appropriate arguments
```

Methods:

  - `DiffMeansPermute.TestStatistic(self, data)`

Computes the test statistic.

data: data in whatever form is relevant        

```python
# obj is an instance of DiffMeansPermute
obj.TestStatistic(...)  # fill in arguments
```

  - `DiffMeansPermute.MakeModel(self)`

Build a model of the null hypothesis.
        

```python
# obj is an instance of DiffMeansPermute
obj.MakeModel(...)  # fill in arguments
```

  - `DiffMeansPermute.RunModel(self)`

Run the model of the null hypothesis.

returns: simulated data

```python
# obj is an instance of DiffMeansPermute
obj.RunModel(...)  # fill in arguments
```

- `DiffStdPermute`

Tests a one-sided difference in standard deviation by permutation.

```python
from code.hypothesis import DiffStdPermute
obj = DiffStdPermute(...)  # construct with appropriate arguments
```

Methods:

  - `DiffStdPermute.TestStatistic(self, data)`

Computes the test statistic.

data: data in whatever form is relevant        

```python
# obj is an instance of DiffStdPermute
obj.TestStatistic(...)  # fill in arguments
```

- `PregLengthTest`

Tests difference in pregnancy length using a chi-squared statistic.

```python
from code.hypothesis import PregLengthTest
obj = PregLengthTest(...)  # construct with appropriate arguments
```

Methods:

  - `PregLengthTest.TestStatistic(self, data)`

Computes the test statistic.

data: pair of lists of pregnancy lengths

```python
# obj is an instance of PregLengthTest
obj.TestStatistic(...)  # fill in arguments
```

  - `PregLengthTest.ChiSquared(self, lengths)`

Computes the chi-squared statistic.

lengths: sequence of lengths

returns: float

```python
# obj is an instance of PregLengthTest
obj.ChiSquared(...)  # fill in arguments
```

  - `PregLengthTest.MakeModel(self)`

Build a model of the null hypothesis.
        

```python
# obj is an instance of PregLengthTest
obj.MakeModel(...)  # fill in arguments
```

  - `PregLengthTest.RunModel(self)`

Run the model of the null hypothesis.

returns: simulated data

```python
# obj is an instance of PregLengthTest
obj.RunModel(...)  # fill in arguments
```
