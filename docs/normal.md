## Module `code.normal`

This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.normal import *  # or import specific names
```

### Functions

- `ChiSquaredCdf(n)`

Discrete approximation of the chi-squared CDF with df=n-1.

n: sample size

returns: Cdf

```python
from code.normal import ChiSquaredCdf
# Example usage:
result = ChiSquaredCdf(...)  # fill in arguments
```

- `GenerateCorrelated(rho, n)`

Generates a sequence of correlated values from a standard normal dist.

rho: coefficient of correlation
n: length of sequence

returns: iterator

```python
from code.normal import GenerateCorrelated
# Example usage:
result = GenerateCorrelated(...)  # fill in arguments
```

- `GenerateExpoCorrelated(rho, n)`

Generates a sequence of correlated values from an exponential dist.

rho: coefficient of correlation
n: length of sequence

returns: NumPy array

```python
from code.normal import GenerateExpoCorrelated
# Example usage:
result = GenerateExpoCorrelated(...)  # fill in arguments
```

- `main()`
```python
from code.normal import main
# Example usage:
result = main(...)  # fill in arguments
```

- `MakeCltPlots()`

Makes plot showing distributions of sums converging to normal.
    

```python
from code.normal import MakeCltPlots
# Example usage:
result = MakeCltPlots(...)  # fill in arguments
```

- `MakeCorrelatedSamples(rho=..., iters=...)`

Generates samples from a correlated exponential distribution.

rho: correlation
iters: number of samples to generate for each size

returns: list of samples

```python
from code.normal import MakeCorrelatedSamples
# Example usage:
result = MakeCorrelatedSamples(...)  # fill in arguments
```

- `MakeExpoSamples(beta=..., iters=...)`

Generates samples from an exponential distribution.

beta: parameter
iters: number of samples to generate for each size

returns: list of samples

```python
from code.normal import MakeExpoSamples
# Example usage:
result = MakeExpoSamples(...)  # fill in arguments
```

- `MakeLognormalSamples(mu=..., sigma=..., iters=...)`

Generates samples from a lognormal distribution.

mu: parmeter
sigma: parameter
iters: number of samples to generate for each size

returns: list of samples

```python
from code.normal import MakeLognormalSamples
# Example usage:
result = MakeLognormalSamples(...)  # fill in arguments
```

- `MakeParetoSamples(alpha=..., iters=...)`

Generates samples from a Pareto distribution.

alpha: parameter
iters: number of samples to generate for each size

returns: list of samples

```python
from code.normal import MakeParetoSamples
# Example usage:
result = MakeParetoSamples(...)  # fill in arguments
```

- `NormalPlotSamples(samples, plot=..., ylabel=...)`

Makes normal probability plots for samples.

samples: list of samples
label: string

```python
from code.normal import NormalPlotSamples
# Example usage:
result = NormalPlotSamples(...)  # fill in arguments
```

- `PlotPregLengths(live, firsts, others)`

Plots sampling distribution of difference in means.

live, firsts, others: DataFrames

```python
from code.normal import PlotPregLengths
# Example usage:
result = PlotPregLengths(...)  # fill in arguments
```

- `ResampleCorrelations(live)`

Tests the correlation between birth weight and mother's age.

live: DataFrame for live births

returns: sample size, observed correlation, CDF of resampled correlations

```python
from code.normal import ResampleCorrelations
# Example usage:
result = ResampleCorrelations(...)  # fill in arguments
```

- `SamplingDistMean(data, n)`

Computes the sampling distribution of the mean.

data: sequence of values representing the population
n: sample size

returns: Normal object

```python
from code.normal import SamplingDistMean
# Example usage:
result = SamplingDistMean(...)  # fill in arguments
```

- `StudentCdf(n)`

Computes the CDF correlations from uncorrelated variables.

n: sample size

returns: Cdf

```python
from code.normal import StudentCdf
# Example usage:
result = StudentCdf(...)  # fill in arguments
```

- `TestChiSquared()`

Performs a chi-squared test analytically.
    

```python
from code.normal import TestChiSquared
# Example usage:
result = TestChiSquared(...)  # fill in arguments
```

- `TestCorrelation(live)`

Tests correlation analytically.

live: DataFrame for live births

```python
from code.normal import TestCorrelation
# Example usage:
result = TestCorrelation(...)  # fill in arguments
```

### Classes

- `CorrelationPermute`

Tests correlations by permutation.

```python
from code.normal import CorrelationPermute
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

- `Normal`

Represents a Normal distribution

```python
from code.normal import Normal
obj = Normal(...)  # construct with appropriate arguments
```

Methods:

  - `Normal.sigma(self)`

Returns the standard deviation.

```python
# obj is an instance of Normal
obj.sigma(...)  # fill in arguments
```

  - `Normal.Sum(self, n)`

Returns the distribution of the sum of n values.

n: int

returns: new Normal

```python
# obj is an instance of Normal
obj.Sum(...)  # fill in arguments
```

  - `Normal.Render(self)`

Returns pair of xs, ys suitable for plotting.
        

```python
# obj is an instance of Normal
obj.Render(...)  # fill in arguments
```

  - `Normal.Prob(self, x)`

Cumulative probability of x.

x: numeric

```python
# obj is an instance of Normal
obj.Prob(...)  # fill in arguments
```

  - `Normal.Percentile(self, p)`

Inverse CDF of p.

p: percentile rank 0-100

```python
# obj is an instance of Normal
obj.Percentile(...)  # fill in arguments
```
