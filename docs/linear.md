## Module `code.linear`

This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.linear import *  # or import specific names
```

### Functions

- `EstimateBirthWeight(live, iters=...)`

Estimate mean birth weight by resampling, with and without weights.

live: DataFrame
iters: number of experiments to run

```python
from code.linear import EstimateBirthWeight
# Example usage:
result = EstimateBirthWeight(...)  # fill in arguments
```

- `main()`
```python
from code.linear import main
# Example usage:
result = main(...)  # fill in arguments
```

- `PlotConfidenceIntervals(xs, inters, slopes, res=..., percent=..., **options)`

Plots the 90% confidence intervals for weights based on ages.

xs: sequence
inters: estimated intercepts
slopes: estimated slopes
res: residuals
percent: what percentile range to show

```python
from code.linear import PlotConfidenceIntervals
# Example usage:
result = PlotConfidenceIntervals(...)  # fill in arguments
```

- `PlotFit(live)`

Plots a scatter plot and fitted curve.

live: DataFrame

```python
from code.linear import PlotFit
# Example usage:
result = PlotFit(...)  # fill in arguments
```

- `PlotResiduals(live)`

Plots percentiles of the residuals.

live: DataFrame

```python
from code.linear import PlotResiduals
# Example usage:
result = PlotResiduals(...)  # fill in arguments
```

- `PlotSamplingDistributions(live)`

Plots confidence intervals for the fitted curve and sampling dists.

live: DataFrame

```python
from code.linear import PlotSamplingDistributions
# Example usage:
result = PlotSamplingDistributions(...)  # fill in arguments
```

- `ResampleRowsWeighted(df, attr=...)`

Resamples a DataFrame using probabilities proportional to finalwgt.

df: DataFrame
attr: string column name to use as weights

returns: DataFrame

```python
from code.linear import ResampleRowsWeighted
# Example usage:
result = ResampleRowsWeighted(...)  # fill in arguments
```

- `SamplingDistributions(live, iters=...)`

Estimates sampling distributions by resampling rows.

live: DataFrame
iters: number of times to run simulations

returns: pair of sequences (inters, slopes)

```python
from code.linear import SamplingDistributions
# Example usage:
result = SamplingDistributions(...)  # fill in arguments
```

- `Summarize(estimates, actual=...)`

Prints standard error and 90% confidence interval.

estimates: sequence of estimates
actual: float actual value

```python
from code.linear import Summarize
# Example usage:
result = Summarize(...)  # fill in arguments
```

### Classes

- `SlopeTest`

Tests the slope of a linear least squares fit. 

```python
from code.linear import SlopeTest
obj = SlopeTest(...)  # construct with appropriate arguments
```

Methods:

  - `SlopeTest.TestStatistic(self, data)`

Computes the test statistic.

data: data in whatever form is relevant        

```python
# obj is an instance of SlopeTest
obj.TestStatistic(...)  # fill in arguments
```

  - `SlopeTest.MakeModel(self)`

Builds a model of the null hypothesis.
        

```python
# obj is an instance of SlopeTest
obj.MakeModel(...)  # fill in arguments
```

  - `SlopeTest.RunModel(self)`

Runs the model of the null hypothesis.

returns: simulated data

```python
# obj is an instance of SlopeTest
obj.RunModel(...)  # fill in arguments
```
