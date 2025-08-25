## Module `code.estimation`

This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.estimation import *  # or import specific names
```

### Functions

- `Estimate1(n=..., m=...)`

Evaluates RMSE of sample mean and median as estimators.

n: sample size
m: number of iterations

```python
from code.estimation import Estimate1
# Example usage:
result = Estimate1(...)  # fill in arguments
```

- `Estimate2(n=..., m=...)`

Evaluates S and Sn-1 as estimators of sample variance.

n: sample size
m: number of iterations

```python
from code.estimation import Estimate2
# Example usage:
result = Estimate2(...)  # fill in arguments
```

- `Estimate3(n=..., m=...)`

Evaluates L and Lm as estimators of the exponential parameter.

n: sample size
m: number of iterations

```python
from code.estimation import Estimate3
# Example usage:
result = Estimate3(...)  # fill in arguments
```

- `main()`
```python
from code.estimation import main
# Example usage:
result = main(...)  # fill in arguments
```

- `MeanError(estimates, actual)`

Computes the mean error of a sequence of estimates.

estimate: sequence of numbers
actual: actual value

returns: float mean error

```python
from code.estimation import MeanError
# Example usage:
result = MeanError(...)  # fill in arguments
```

- `RMSE(estimates, actual)`

Computes the root mean squared error of a sequence of estimates.

estimate: sequence of numbers
actual: actual value

returns: float RMSE

```python
from code.estimation import RMSE
# Example usage:
result = RMSE(...)  # fill in arguments
```

- `SimulateSample(mu=..., sigma=..., n=..., m=...)`

Plots the sampling distribution of the sample mean.

mu: hypothetical population mean
sigma: hypothetical population standard deviation
n: sample size
m: number of iterations

```python
from code.estimation import SimulateSample
# Example usage:
result = SimulateSample(...)  # fill in arguments
```
