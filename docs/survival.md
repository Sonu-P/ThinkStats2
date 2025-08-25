## Module `code.survival`

This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.survival import *  # or import specific names
```

### Functions

- `AddLabelsByDecade(groups, **options)`

Draws fake points in order to add labels to the legend.

groups: GroupBy object

```python
from code.survival import AddLabelsByDecade
# Example usage:
result = AddLabelsByDecade(...)  # fill in arguments
```

- `CleanFemResp(resp)`

Cleans a respondent DataFrame.

resp: DataFrame of respondents

Adds columns: agemarry, age, decade, fives

```python
from code.survival import CleanFemResp
# Example usage:
result = CleanFemResp(...)  # fill in arguments
```

- `ConditionalSurvival(pmf, t0)`

Computes conditional survival function.

Probability that duration exceeds t0+t, given that
duration >= t0.

pmf: Pmf of durations
t0: minimum time

returns: tuple of (ts, conditional survivals)

```python
from code.survival import ConditionalSurvival
# Example usage:
result = ConditionalSurvival(...)  # fill in arguments
```

- `EstimateHazardFunction(complete, ongoing, label=..., verbose=...)`

Estimates the hazard function by Kaplan-Meier.

http://en.wikipedia.org/wiki/Kaplan%E2%80%93Meier_estimator

complete: list of complete lifetimes
ongoing: list of ongoing lifetimes
label: string
verbose: whether to display intermediate results

```python
from code.survival import EstimateHazardFunction
# Example usage:
result = EstimateHazardFunction(...)  # fill in arguments
```

- `EstimateHazardNumpy(complete, ongoing, label=...)`

Estimates the hazard function by Kaplan-Meier.

Just for fun, this is a version that uses NumPy to
eliminate loops.

complete: list of complete lifetimes
ongoing: list of ongoing lifetimes
label: string

```python
from code.survival import EstimateHazardNumpy
# Example usage:
result = EstimateHazardNumpy(...)  # fill in arguments
```

- `EstimateMarriageSurvival(resp)`

Estimates the survival curve.

resp: DataFrame of respondents

returns: pair of HazardFunction, SurvivalFunction

```python
from code.survival import EstimateMarriageSurvival
# Example usage:
result = EstimateMarriageSurvival(...)  # fill in arguments
```

- `EstimateMarriageSurvivalByDecade(groups, **options)`

Groups respondents by decade and plots survival curves.

groups: GroupBy object

```python
from code.survival import EstimateMarriageSurvivalByDecade
# Example usage:
result = EstimateMarriageSurvivalByDecade(...)  # fill in arguments
```

- `main()`
```python
from code.survival import main
# Example usage:
result = main(...)  # fill in arguments
```

- `MakeSurvivalFromCdf(cdf, label=...)`

Makes a survival function based on a CDF.

cdf: Cdf

returns: SurvivalFunction

```python
from code.survival import MakeSurvivalFromCdf
# Example usage:
result = MakeSurvivalFromCdf(...)  # fill in arguments
```

- `MakeSurvivalFromSeq(values, label=...)`

Makes a survival function based on a complete dataset.

values: sequence of observed lifespans

returns: SurvivalFunction

```python
from code.survival import MakeSurvivalFromSeq
# Example usage:
result = MakeSurvivalFromSeq(...)  # fill in arguments
```

- `PlotConditionalSurvival(durations)`

Plots conditional survival curves for a range of t0.

durations: list of durations

```python
from code.survival import PlotConditionalSurvival
# Example usage:
result = PlotConditionalSurvival(...)  # fill in arguments
```

- `PlotHazard(complete, ongoing)`

Plots the hazard function and survival function.

complete: list of complete lifetimes
ongoing: list of ongoing lifetimes

```python
from code.survival import PlotHazard
# Example usage:
result = PlotHazard(...)  # fill in arguments
```

- `PlotMarriageData(resp)`

Plots hazard and survival functions.

resp: DataFrame of respondents

```python
from code.survival import PlotMarriageData
# Example usage:
result = PlotMarriageData(...)  # fill in arguments
```

- `PlotPredictionsByDecade(groups, **options)`

Groups respondents by decade and plots survival curves.

groups: GroupBy object

```python
from code.survival import PlotPredictionsByDecade
# Example usage:
result = PlotPredictionsByDecade(...)  # fill in arguments
```

- `PlotPregnancyData(preg)`

Plots survival and hazard curves based on pregnancy lengths.

preg:


Outcome codes from http://www.icpsr.umich.edu/nsfg6/Controller?
displayPage=labelDetails&fileCode=PREG&section=&subSec=8016&srtLabel=611932

1   LIVE BIRTH              9148
2   INDUCED ABORTION        1862
3   STILLBIRTH              120
4   MISCARRIAGE             1921
5   ECTOPIC PREGNANCY       190
6   CURRENT PREGNANCY       352

```python
from code.survival import PlotPregnancyData
# Example usage:
result = PlotPregnancyData(...)  # fill in arguments
```

- `PlotRemainingLifetime(sf1, sf2)`

Plots remaining lifetimes for pregnancy and age at first marriage.

sf1: SurvivalFunction for pregnancy length
sf2: SurvivalFunction for age at first marriage

```python
from code.survival import PlotRemainingLifetime
# Example usage:
result = PlotRemainingLifetime(...)  # fill in arguments
```

- `PlotResampledByDecade(resps, iters=..., predict_flag=..., omit=...)`

Plots survival curves for resampled data.

resps: list of DataFrames
iters: number of resamples to plot
predict_flag: whether to also plot predictions

```python
from code.survival import PlotResampledByDecade
# Example usage:
result = PlotResampledByDecade(...)  # fill in arguments
```

- `PlotSurvival(complete)`

Plots survival and hazard curves.

complete: list of complete lifetimes

```python
from code.survival import PlotSurvival
# Example usage:
result = PlotSurvival(...)  # fill in arguments
```

- `ReadFemResp(dct_file=..., dat_file=..., **options)`

Reads the NSFG respondent data.

dct_file: string file name
dat_file: string file name

returns: DataFrame

```python
from code.survival import ReadFemResp
# Example usage:
result = ReadFemResp(...)  # fill in arguments
```

- `ReadFemResp1995()`

Reads respondent data from NSFG Cycle 5.

returns: DataFrame

```python
from code.survival import ReadFemResp1995
# Example usage:
result = ReadFemResp1995(...)  # fill in arguments
```

- `ReadFemResp2002()`

Reads respondent data from NSFG Cycle 6.

returns: DataFrame

```python
from code.survival import ReadFemResp2002
# Example usage:
result = ReadFemResp2002(...)  # fill in arguments
```

- `ReadFemResp2010()`

Reads respondent data from NSFG Cycle 7.

returns: DataFrame

```python
from code.survival import ReadFemResp2010
# Example usage:
result = ReadFemResp2010(...)  # fill in arguments
```

- `ReadFemResp2013()`

Reads respondent data from NSFG Cycle 8.

returns: DataFrame

```python
from code.survival import ReadFemResp2013
# Example usage:
result = ReadFemResp2013(...)  # fill in arguments
```

- `ResampleSurvival(resp, iters=...)`

Resamples respondents and estimates the survival function.

resp: DataFrame of respondents
iters: number of resamples

```python
from code.survival import ResampleSurvival
# Example usage:
result = ResampleSurvival(...)  # fill in arguments
```

### Classes

- `HazardFunction`

Represents a hazard function.

```python
from code.survival import HazardFunction
obj = HazardFunction(...)  # construct with appropriate arguments
```

Methods:

  - `HazardFunction.Get(self, t, default=...)`
```python
# obj is an instance of HazardFunction
obj.Get(...)  # fill in arguments
```

  - `HazardFunction.Render(self)`

Generates a sequence of points suitable for plotting.

returns: tuple of (sorted times, hazard function)

```python
# obj is an instance of HazardFunction
obj.Render(...)  # fill in arguments
```

  - `HazardFunction.MakeSurvival(self, label=...)`

Makes the survival function.

returns: SurvivalFunction

```python
# obj is an instance of HazardFunction
obj.MakeSurvival(...)  # fill in arguments
```

  - `HazardFunction.Extend(self, other)`

Extends this hazard function by copying the tail from another.
other: HazardFunction

```python
# obj is an instance of HazardFunction
obj.Extend(...)  # fill in arguments
```

  - `HazardFunction.Truncate(self, t)`

Truncates this hazard function at the given value of t.
t: number

```python
# obj is an instance of HazardFunction
obj.Truncate(...)  # fill in arguments
```

- `SurvivalFunction`

Represents a survival function.

```python
from code.survival import SurvivalFunction
obj = SurvivalFunction(...)  # construct with appropriate arguments
```

Methods:

  - `SurvivalFunction.Prob(self, t)`

Returns S(t), the probability that corresponds to value t.
t: time
returns: float probability

```python
# obj is an instance of SurvivalFunction
obj.Prob(...)  # fill in arguments
```

  - `SurvivalFunction.Probs(self, ts)`

Gets probabilities for a sequence of values.

```python
# obj is an instance of SurvivalFunction
obj.Probs(...)  # fill in arguments
```

  - `SurvivalFunction.Items(self)`

Sorted list of (t, s) pairs.

```python
# obj is an instance of SurvivalFunction
obj.Items(...)  # fill in arguments
```

  - `SurvivalFunction.Render(self)`

Generates a sequence of points suitable for plotting.
returns: tuple of (sorted times, survival function)

```python
# obj is an instance of SurvivalFunction
obj.Render(...)  # fill in arguments
```

  - `SurvivalFunction.MakeHazardFunction(self, label=...)`

Computes the hazard function.

This simple version does not take into account the
spacing between the ts.  If the ts are not equally
spaced, it is not valid to compare the magnitude of
the hazard function across different time steps.

label: string

returns: HazardFunction object

```python
# obj is an instance of SurvivalFunction
obj.MakeHazardFunction(...)  # fill in arguments
```

  - `SurvivalFunction.MakePmf(self, filler=...)`

Makes a PMF of lifetimes.

filler: value to replace missing values

returns: Pmf

```python
# obj is an instance of SurvivalFunction
obj.MakePmf(...)  # fill in arguments
```

  - `SurvivalFunction.RemainingLifetime(self, filler=..., func=...)`

Computes remaining lifetime as a function of age.
func: function from conditional Pmf to expected liftime
returns: Series that maps from age to remaining lifetime

```python
# obj is an instance of SurvivalFunction
obj.RemainingLifetime(...)  # fill in arguments
```
