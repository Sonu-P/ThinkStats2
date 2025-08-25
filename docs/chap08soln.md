## Module `code.chap08soln`

This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.chap08soln import *  # or import specific names
```

### Functions

- `Estimate1(n=..., m=...)`

Mean error for xbar and median as estimators of population mean.

n: sample size
m: number of iterations

```python
from code.chap08soln import Estimate1
# Example usage:
result = Estimate1(...)  # fill in arguments
```

- `Estimate2(n=..., m=...)`

RMSE for biased and unbiased estimators of population variance.

n: sample size
m: number of iterations

```python
from code.chap08soln import Estimate2
# Example usage:
result = Estimate2(...)  # fill in arguments
```

- `Estimate4(lam=..., m=...)`
```python
from code.chap08soln import Estimate4
# Example usage:
result = Estimate4(...)  # fill in arguments
```

- `main()`
```python
from code.chap08soln import main
# Example usage:
result = main(...)  # fill in arguments
```

- `SimulateGame(lam)`

Simulates a game and returns the estimated goal-scoring rate.

lam: actual goal scoring rate in goals per game

```python
from code.chap08soln import SimulateGame
# Example usage:
result = SimulateGame(...)  # fill in arguments
```

- `SimulateSample(lam=..., n=..., m=...)`

Sampling distribution of L as an estimator of exponential parameter.

lam: parameter of an exponential distribution
n: sample size
m: number of iterations

```python
from code.chap08soln import SimulateSample
# Example usage:
result = SimulateSample(...)  # fill in arguments
```
