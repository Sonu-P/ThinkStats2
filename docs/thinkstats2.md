## Module `code.thinkstats2`

This file contains code for use with "Think Stats" and
"Think Bayes", both by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.thinkstats2 import *  # or import specific names
```

### Functions

- `BinomialCoef(n, k)`

Compute the binomial coefficient "n choose k".

n: number of trials
k: number of successes

Returns: float

```python
from code.thinkstats2 import BinomialCoef
# Example usage:
result = BinomialCoef(...)  # fill in arguments
```

- `CentralMoment(xs, k)`

Computes the kth central moment of xs.
    

```python
from code.thinkstats2 import CentralMoment
# Example usage:
result = CentralMoment(...)  # fill in arguments
```

- `CoefDetermination(ys, res)`

Computes the coefficient of determination (R^2) for given residuals.

Args:
    ys: dependent variable
    res: residuals
    
Returns:
    float coefficient of determination

```python
from code.thinkstats2 import CoefDetermination
# Example usage:
result = CoefDetermination(...)  # fill in arguments
```

- `CohenEffectSize(group1, group2)`

Compute Cohen's d.

group1: Series or NumPy array
group2: Series or NumPy array

returns: float

```python
from code.thinkstats2 import CohenEffectSize
# Example usage:
result = CohenEffectSize(...)  # fill in arguments
```

- `Corr(xs, ys)`

Computes Corr(X, Y).

Args:
    xs: sequence of values
    ys: sequence of values

Returns:
    Corr(X, Y)

```python
from code.thinkstats2 import Corr
# Example usage:
result = Corr(...)  # fill in arguments
```

- `CorrelatedGenerator(rho)`

Generates standard normal variates with serial correlation.

rho: target coefficient of correlation

Returns: iterable

```python
from code.thinkstats2 import CorrelatedGenerator
# Example usage:
result = CorrelatedGenerator(...)  # fill in arguments
```

- `CorrelatedNormalGenerator(mu, sigma, rho)`

Generates normal variates with serial correlation.

mu: mean of variate
sigma: standard deviation of variate
rho: target coefficient of correlation

Returns: iterable

```python
from code.thinkstats2 import CorrelatedNormalGenerator
# Example usage:
result = CorrelatedNormalGenerator(...)  # fill in arguments
```

- `Cov(xs, ys, meanx=..., meany=...)`

Computes Cov(X, Y).

Args:
    xs: sequence of values
    ys: sequence of values
    meanx: optional float mean of xs
    meany: optional float mean of ys

Returns:
    Cov(X, Y)

```python
from code.thinkstats2 import Cov
# Example usage:
result = Cov(...)  # fill in arguments
```

- `CredibleInterval(pmf, percentage=...)`

Computes a credible interval for a given distribution.

If percentage=90, computes the 90% CI.

Args:
    pmf: Pmf object representing a posterior distribution
    percentage: float between 0 and 100

Returns:
    sequence of two floats, low and high

```python
from code.thinkstats2 import CredibleInterval
# Example usage:
result = CredibleInterval(...)  # fill in arguments
```

- `EvalBinomialPmf(k, n, p)`

Evaluates the binomial PMF.

Returns the probabily of k successes in n trials with probability p.

```python
from code.thinkstats2 import EvalBinomialPmf
# Example usage:
result = EvalBinomialPmf(...)  # fill in arguments
```

- `EvalExponentialCdf(x, lam)`

Evaluates CDF of the exponential distribution with parameter lam.

```python
from code.thinkstats2 import EvalExponentialCdf
# Example usage:
result = EvalExponentialCdf(...)  # fill in arguments
```

- `EvalExponentialPdf(x, lam)`

Computes the exponential PDF.

x: value
lam: parameter lambda in events per unit time

returns: float probability density

```python
from code.thinkstats2 import EvalExponentialPdf
# Example usage:
result = EvalExponentialPdf(...)  # fill in arguments
```

- `EvalHypergeomPmf(k, N, K, n)`

Evaluates the hypergeometric PMF.

Returns the probabily of k successes in n trials from a population
N with K successes in it.

```python
from code.thinkstats2 import EvalHypergeomPmf
# Example usage:
result = EvalHypergeomPmf(...)  # fill in arguments
```

- `EvalLognormalCdf(x, mu=..., sigma=...)`

Evaluates the CDF of the lognormal distribution.

x: float or sequence
mu: mean parameter
sigma: standard deviation parameter
            
Returns: float or sequence

```python
from code.thinkstats2 import EvalLognormalCdf
# Example usage:
result = EvalLognormalCdf(...)  # fill in arguments
```

- `EvalNormalCdf(x, mu=..., sigma=...)`

Evaluates the CDF of the normal distribution.

Args:
    x: float

    mu: mean parameter
    
    sigma: standard deviation parameter
            
Returns:
    float

```python
from code.thinkstats2 import EvalNormalCdf
# Example usage:
result = EvalNormalCdf(...)  # fill in arguments
```

- `EvalNormalCdfInverse(p, mu=..., sigma=...)`

Evaluates the inverse CDF of the normal distribution.

See http://en.wikipedia.org/wiki/Normal_distribution#Quantile_function  

Args:
    p: float

    mu: mean parameter
    
    sigma: standard deviation parameter
            
Returns:
    float

```python
from code.thinkstats2 import EvalNormalCdfInverse
# Example usage:
result = EvalNormalCdfInverse(...)  # fill in arguments
```

- `EvalNormalPdf(x, mu, sigma)`

Computes the unnormalized PDF of the normal distribution.

x: value
mu: mean
sigma: standard deviation

returns: float probability density

```python
from code.thinkstats2 import EvalNormalPdf
# Example usage:
result = EvalNormalPdf(...)  # fill in arguments
```

- `EvalPoissonPmf(k, lam)`

Computes the Poisson PMF.

k: number of events
lam: parameter lambda in events per unit time

returns: float probability

```python
from code.thinkstats2 import EvalPoissonPmf
# Example usage:
result = EvalPoissonPmf(...)  # fill in arguments
```

- `FitLine(xs, inter, slope)`

Fits a line to the given data.

xs: sequence of x

returns: tuple of numpy arrays (sorted xs, fit ys)

```python
from code.thinkstats2 import FitLine
# Example usage:
result = FitLine(...)  # fill in arguments
```

- `IQR(xs)`

Computes the interquartile of a sequence.

xs: sequence or anything else that can initialize a Cdf

returns: pair of floats

```python
from code.thinkstats2 import IQR
# Example usage:
result = IQR(...)  # fill in arguments
```

- `Jitter(values, jitter=...)`

Jitters the values by adding a uniform variate in (-jitter, jitter).

values: sequence
jitter: scalar magnitude of jitter

returns: new numpy array

```python
from code.thinkstats2 import Jitter
# Example usage:
result = Jitter(...)  # fill in arguments
```

- `LeastSquares(xs, ys)`

Computes a linear least squares fit for ys as a function of xs.

Args:
    xs: sequence of values
    ys: sequence of values

Returns:
    tuple of (intercept, slope)

```python
from code.thinkstats2 import LeastSquares
# Example usage:
result = LeastSquares(...)  # fill in arguments
```

- `LogBinomialCoef(n, k)`

Computes the log of the binomial coefficient.

http://math.stackexchange.com/questions/64716/
approximating-the-logarithm-of-the-binomial-coefficient

n: number of trials
k: number of successes

Returns: float

```python
from code.thinkstats2 import LogBinomialCoef
# Example usage:
result = LogBinomialCoef(...)  # fill in arguments
```

- `main()`
```python
from code.thinkstats2 import main
# Example usage:
result = main(...)  # fill in arguments
```

- `MakeBinomialPmf(n, p)`

Evaluates the binomial PMF.

Returns the distribution of successes in n trials with probability p.

```python
from code.thinkstats2 import MakeBinomialPmf
# Example usage:
result = MakeBinomialPmf(...)  # fill in arguments
```

- `MakeCdfFromDict(d, label=...)`

Makes a CDF from a dictionary that maps values to frequencies.

Args:
   d: dictionary that maps values to frequencies.
   label: string label for the data.

Returns:
    Cdf object

```python
from code.thinkstats2 import MakeCdfFromDict
# Example usage:
result = MakeCdfFromDict(...)  # fill in arguments
```

- `MakeCdfFromHist(hist, label=...)`

Makes a CDF from a Hist object.

Args:
   hist: Pmf.Hist object
   label: string label for the data.

Returns:
    Cdf object

```python
from code.thinkstats2 import MakeCdfFromHist
# Example usage:
result = MakeCdfFromHist(...)  # fill in arguments
```

- `MakeCdfFromItems(items, label=...)`

Makes a cdf from an unsorted sequence of (value, frequency) pairs.

Args:
    items: unsorted sequence of (value, frequency) pairs
    label: string label for this CDF

Returns:
    cdf: list of (value, fraction) pairs

```python
from code.thinkstats2 import MakeCdfFromItems
# Example usage:
result = MakeCdfFromItems(...)  # fill in arguments
```

- `MakeCdfFromList(seq, label=...)`

Creates a CDF from an unsorted sequence.

Args:
    seq: unsorted sequence of sortable values
    label: string label for the cdf

Returns:
   Cdf object

```python
from code.thinkstats2 import MakeCdfFromList
# Example usage:
result = MakeCdfFromList(...)  # fill in arguments
```

- `MakeCdfFromPmf(pmf, label=...)`

Makes a CDF from a Pmf object.

Args:
   pmf: Pmf.Pmf object
   label: string label for the data.

Returns:
    Cdf object

```python
from code.thinkstats2 import MakeCdfFromPmf
# Example usage:
result = MakeCdfFromPmf(...)  # fill in arguments
```

- `MakeExponentialPmf(lam, high, n=...)`

Makes a PMF discrete approx to an exponential distribution.

lam: parameter lambda in events per unit time
high: upper bound
n: number of values in the Pmf

returns: normalized Pmf

```python
from code.thinkstats2 import MakeExponentialPmf
# Example usage:
result = MakeExponentialPmf(...)  # fill in arguments
```

- `MakeHistFromDict(d, label=...)`

Makes a histogram from a map from values to frequencies.

Args:
    d: dictionary that maps values to frequencies
    label: string label for this histogram

Returns:
    Hist object

```python
from code.thinkstats2 import MakeHistFromDict
# Example usage:
result = MakeHistFromDict(...)  # fill in arguments
```

- `MakeHistFromList(t, label=...)`

Makes a histogram from an unsorted sequence of values.

Args:
    t: sequence of numbers
    label: string label for this histogram

Returns:
    Hist object

```python
from code.thinkstats2 import MakeHistFromList
# Example usage:
result = MakeHistFromList(...)  # fill in arguments
```

- `MakeJoint(pmf1, pmf2)`

Joint distribution of values from pmf1 and pmf2.

Assumes that the PMFs represent independent random variables.

Args:
    pmf1: Pmf object
    pmf2: Pmf object

Returns:
    Joint pmf of value pairs

```python
from code.thinkstats2 import MakeJoint
# Example usage:
result = MakeJoint(...)  # fill in arguments
```

- `MakeMixture(metapmf, label=...)`

Make a mixture distribution.

Args:
  metapmf: Pmf that maps from Pmfs to probs.
  label: string label for the new Pmf.

Returns: Pmf object.

```python
from code.thinkstats2 import MakeMixture
# Example usage:
result = MakeMixture(...)  # fill in arguments
```

- `MakeNormalPmf(mu, sigma, num_sigmas, n=...)`

Makes a PMF discrete approx to a Normal distribution.

mu: float mean
sigma: float standard deviation
num_sigmas: how many sigmas to extend in each direction
n: number of values in the Pmf

returns: normalized Pmf

```python
from code.thinkstats2 import MakeNormalPmf
# Example usage:
result = MakeNormalPmf(...)  # fill in arguments
```

- `MakePmfFromDict(d, label=...)`

Makes a PMF from a map from values to probabilities.

Args:
    d: dictionary that maps values to probabilities
    label: string label for this PMF

Returns:
    Pmf object

```python
from code.thinkstats2 import MakePmfFromDict
# Example usage:
result = MakePmfFromDict(...)  # fill in arguments
```

- `MakePmfFromHist(hist, label=...)`

Makes a normalized PMF from a Hist object.

Args:
    hist: Hist object
    label: string label

Returns:
    Pmf object

```python
from code.thinkstats2 import MakePmfFromHist
# Example usage:
result = MakePmfFromHist(...)  # fill in arguments
```

- `MakePmfFromItems(t, label=...)`

Makes a PMF from a sequence of value-probability pairs

Args:
    t: sequence of value-probability pairs
    label: string label for this PMF

Returns:
    Pmf object

```python
from code.thinkstats2 import MakePmfFromItems
# Example usage:
result = MakePmfFromItems(...)  # fill in arguments
```

- `MakePmfFromList(t, label=...)`

Makes a PMF from an unsorted sequence of values.

Args:
    t: sequence of numbers
    label: string label for this PMF

Returns:
    Pmf object

```python
from code.thinkstats2 import MakePmfFromList
# Example usage:
result = MakePmfFromList(...)  # fill in arguments
```

- `MakePoissonPmf(lam, high, step=...)`

Makes a PMF discrete approx to a Poisson distribution.

lam: parameter lambda in events per unit time
high: upper bound of the Pmf

returns: normalized Pmf

```python
from code.thinkstats2 import MakePoissonPmf
# Example usage:
result = MakePoissonPmf(...)  # fill in arguments
```

- `MakeSuiteFromDict(d, label=...)`

Makes a suite from a map from values to probabilities.

Args:
    d: dictionary that maps values to probabilities
    label: string label for this suite

Returns:
    Suite object

```python
from code.thinkstats2 import MakeSuiteFromDict
# Example usage:
result = MakeSuiteFromDict(...)  # fill in arguments
```

- `MakeSuiteFromHist(hist, label=...)`

Makes a normalized suite from a Hist object.

Args:
    hist: Hist object
    label: string label

Returns:
    Suite object

```python
from code.thinkstats2 import MakeSuiteFromHist
# Example usage:
result = MakeSuiteFromHist(...)  # fill in arguments
```

- `MakeSuiteFromList(t, label=...)`

Makes a suite from an unsorted sequence of values.

Args:
    t: sequence of numbers
    label: string label for this suite

Returns:
    Suite object

```python
from code.thinkstats2 import MakeSuiteFromList
# Example usage:
result = MakeSuiteFromList(...)  # fill in arguments
```

- `MakeUniformPmf(low, high, n)`

Make a uniform Pmf.

low: lowest value (inclusive)
high: highest value (inclusize)
n: number of values

```python
from code.thinkstats2 import MakeUniformPmf
# Example usage:
result = MakeUniformPmf(...)  # fill in arguments
```

- `MapToRanks(t)`

Returns a list of ranks corresponding to the elements in t.

Args:
    t: sequence of numbers

Returns:
    list of integer ranks, starting at 1

```python
from code.thinkstats2 import MapToRanks
# Example usage:
result = MapToRanks(...)  # fill in arguments
```

- `Mean(xs)`

Computes mean.

xs: sequence of values

returns: float mean

```python
from code.thinkstats2 import Mean
# Example usage:
result = Mean(...)  # fill in arguments
```

- `MeanVar(xs, ddof=...)`

Computes mean and variance.

Based on http://stackoverflow.com/questions/19391149/
numpy-mean-and-variance-from-single-function

xs: sequence of values
ddof: delta degrees of freedom

returns: pair of float, mean and var

```python
from code.thinkstats2 import MeanVar
# Example usage:
result = MeanVar(...)  # fill in arguments
```

- `Median(xs)`

Computes the median (50th percentile) of a sequence.

xs: sequence or anything else that can initialize a Cdf

returns: float

```python
from code.thinkstats2 import Median
# Example usage:
result = Median(...)  # fill in arguments
```

- `NormalProbability(ys, jitter=...)`

Generates data for a normal probability plot.

ys: sequence of values
jitter: float magnitude of jitter added to the ys 

returns: numpy arrays xs, ys

```python
from code.thinkstats2 import NormalProbability
# Example usage:
result = NormalProbability(...)  # fill in arguments
```

- `NormalProbabilityPlot(sample, fit_color=..., **options)`

Makes a normal probability plot with a fitted line.

sample: sequence of numbers
fit_color: color string for the fitted line
options: passed along to Plot

```python
from code.thinkstats2 import NormalProbabilityPlot
# Example usage:
result = NormalProbabilityPlot(...)  # fill in arguments
```

- `Odds(p)`

Computes odds for a given probability.

Example: p=0.75 means 75 for and 25 against, or 3:1 odds in favor.

Note: when p=1, the formula for odds divides by zero, which is
normally undefined.  But I think it is reasonable to define Odds(1)
to be infinity, so that's what this function does.

p: float 0-1

Returns: float odds

```python
from code.thinkstats2 import Odds
# Example usage:
result = Odds(...)  # fill in arguments
```

- `PearsonMedianSkewness(xs)`

Computes the Pearson median skewness.
    

```python
from code.thinkstats2 import PearsonMedianSkewness
# Example usage:
result = PearsonMedianSkewness(...)  # fill in arguments
```

- `PercentileRow(array, p)`

Selects the row from a sorted array that maps to percentile p.

p: float 0--100

returns: NumPy array (one row)

```python
from code.thinkstats2 import PercentileRow
# Example usage:
result = PercentileRow(...)  # fill in arguments
```

- `PercentileRows(ys_seq, percents)`

Given a collection of lines, selects percentiles along vertical axis.

For example, if ys_seq contains simulation results like ys as a
function of time, and percents contains (5, 95), the result would
be a 90% CI for each vertical slice of the simulation results.

ys_seq: sequence of lines (y values)
percents: list of percentiles (0-100) to select

returns: list of NumPy arrays, one for each percentile

```python
from code.thinkstats2 import PercentileRows
# Example usage:
result = PercentileRows(...)  # fill in arguments
```

- `PmfProbEqual(pmf1, pmf2)`

Probability that a value from pmf1 equals a value from pmf2.

Args:
    pmf1: Pmf object
    pmf2: Pmf object

Returns:
    float probability

```python
from code.thinkstats2 import PmfProbEqual
# Example usage:
result = PmfProbEqual(...)  # fill in arguments
```

- `PmfProbGreater(pmf1, pmf2)`

Probability that a value from pmf1 is less than a value from pmf2.

Args:
    pmf1: Pmf object
    pmf2: Pmf object

Returns:
    float probability

```python
from code.thinkstats2 import PmfProbGreater
# Example usage:
result = PmfProbGreater(...)  # fill in arguments
```

- `PmfProbLess(pmf1, pmf2)`

Probability that a value from pmf1 is less than a value from pmf2.

Args:
    pmf1: Pmf object
    pmf2: Pmf object

Returns:
    float probability

```python
from code.thinkstats2 import PmfProbLess
# Example usage:
result = PmfProbLess(...)  # fill in arguments
```

- `Probability(o)`

Computes the probability corresponding to given odds.

Example: o=2 means 2:1 odds in favor, or 2/3 probability

o: float odds, strictly positive

Returns: float probability

```python
from code.thinkstats2 import Probability
# Example usage:
result = Probability(...)  # fill in arguments
```

- `Probability2(yes, no)`

Computes the probability corresponding to given odds.

Example: yes=2, no=1 means 2:1 odds in favor, or 2/3 probability.

yes, no: int or float odds in favor

```python
from code.thinkstats2 import Probability2
# Example usage:
result = Probability2(...)  # fill in arguments
```

- `RandomSeed(x)`

Initialize the random and np.random generators.

x: int seed

```python
from code.thinkstats2 import RandomSeed
# Example usage:
result = RandomSeed(...)  # fill in arguments
```

- `RandomSum(dists)`

Chooses a random value from each dist and returns the sum.

dists: sequence of Pmf or Cdf objects

returns: numerical sum

```python
from code.thinkstats2 import RandomSum
# Example usage:
result = RandomSum(...)  # fill in arguments
```

- `RawMoment(xs, k)`

Computes the kth raw moment of xs.
    

```python
from code.thinkstats2 import RawMoment
# Example usage:
result = RawMoment(...)  # fill in arguments
```

- `ReadStataDct(dct_file, **options)`

Reads a Stata dictionary file.

dct_file: string filename
options: dict of options passed to open()

returns: FixedWidthVariables object

```python
from code.thinkstats2 import ReadStataDct
# Example usage:
result = ReadStataDct(...)  # fill in arguments
```

- `RenderExpoCdf(lam, low, high, n=...)`

Generates sequences of xs and ps for an exponential CDF.

lam: parameter
low: float
high: float
n: number of points to render

returns: numpy arrays (xs, ps)

```python
from code.thinkstats2 import RenderExpoCdf
# Example usage:
result = RenderExpoCdf(...)  # fill in arguments
```

- `RenderNormalCdf(mu, sigma, low, high, n=...)`

Generates sequences of xs and ps for a Normal CDF.

mu: parameter
sigma: parameter
low: float
high: float
n: number of points to render

returns: numpy arrays (xs, ps)

```python
from code.thinkstats2 import RenderNormalCdf
# Example usage:
result = RenderNormalCdf(...)  # fill in arguments
```

- `RenderParetoCdf(xmin, alpha, low, high, n=...)`

Generates sequences of xs and ps for a Pareto CDF.

xmin: parameter
alpha: parameter
low: float
high: float
n: number of points to render

returns: numpy arrays (xs, ps)

```python
from code.thinkstats2 import RenderParetoCdf
# Example usage:
result = RenderParetoCdf(...)  # fill in arguments
```

- `Resample(xs, n=...)`

Draw a sample from xs with the same length as xs.

xs: sequence
n: sample size (default: len(xs))

returns: NumPy array

```python
from code.thinkstats2 import Resample
# Example usage:
result = Resample(...)  # fill in arguments
```

- `ResampleRows(df)`

Resamples rows from a DataFrame.

df: DataFrame

returns: DataFrame

```python
from code.thinkstats2 import ResampleRows
# Example usage:
result = ResampleRows(...)  # fill in arguments
```

- `ResampleRowsWeighted(df, column=...)`

Resamples a DataFrame using probabilities proportional to given column.

df: DataFrame
column: string column name to use as weights

returns: DataFrame

```python
from code.thinkstats2 import ResampleRowsWeighted
# Example usage:
result = ResampleRowsWeighted(...)  # fill in arguments
```

- `Residuals(xs, ys, inter, slope)`

Computes residuals for a linear fit with parameters inter and slope.

Args:
    xs: independent variable
    ys: dependent variable
    inter: float intercept
    slope: float slope

Returns:
    list of residuals

```python
from code.thinkstats2 import Residuals
# Example usage:
result = Residuals(...)  # fill in arguments
```

- `SampleRows(df, nrows, replace=...)`

Choose a sample of rows from a DataFrame.

df: DataFrame
nrows: number of rows
replace: whether to sample with replacement

returns: DataDf

```python
from code.thinkstats2 import SampleRows
# Example usage:
result = SampleRows(...)  # fill in arguments
```

- `SampleSum(dists, n)`

Draws a sample of sums from a list of distributions.

dists: sequence of Pmf or Cdf objects
n: sample size

returns: new Pmf of sums

```python
from code.thinkstats2 import SampleSum
# Example usage:
result = SampleSum(...)  # fill in arguments
```

- `SerialCorr(series, lag=...)`

Computes the serial correlation of a series.

series: Series
lag: integer number of intervals to shift

returns: float correlation

```python
from code.thinkstats2 import SerialCorr
# Example usage:
result = SerialCorr(...)  # fill in arguments
```

- `Skewness(xs)`

Computes skewness.
    

```python
from code.thinkstats2 import Skewness
# Example usage:
result = Skewness(...)  # fill in arguments
```

- `Smooth(xs, sigma=..., **options)`

Smooths a NumPy array with a Gaussian filter.

xs: sequence
sigma: standard deviation of the filter

```python
from code.thinkstats2 import Smooth
# Example usage:
result = Smooth(...)  # fill in arguments
```

- `SpearmanCorr(xs, ys)`

Computes Spearman's rank correlation.

Args:
    xs: sequence of values
    ys: sequence of values

Returns:
    float Spearman's correlation

```python
from code.thinkstats2 import SpearmanCorr
# Example usage:
result = SpearmanCorr(...)  # fill in arguments
```

- `StandardizedMoment(xs, k)`

Computes the kth standardized moment of xs.
    

```python
from code.thinkstats2 import StandardizedMoment
# Example usage:
result = StandardizedMoment(...)  # fill in arguments
```

- `StandardNormalCdf(x)`

Evaluates the CDF of the standard Normal distribution.

See http://en.wikipedia.org/wiki/Normal_distribution
#Cumulative_distribution_function

Args:
    x: float
            
Returns:
    float

```python
from code.thinkstats2 import StandardNormalCdf
# Example usage:
result = StandardNormalCdf(...)  # fill in arguments
```

- `Std(xs, mu=..., ddof=...)`

Computes standard deviation.

xs: sequence of values
mu: option known mean
ddof: delta degrees of freedom

returns: float

```python
from code.thinkstats2 import Std
# Example usage:
result = Std(...)  # fill in arguments
```

- `Trim(t, p=...)`

Trims the largest and smallest elements of t.

Args:
    t: sequence of numbers
    p: fraction of values to trim off each end

Returns:
    sequence of values

```python
from code.thinkstats2 import Trim
# Example usage:
result = Trim(...)  # fill in arguments
```

- `TrimmedMean(t, p=...)`

Computes the trimmed mean of a sequence of numbers.

Args:
    t: sequence of numbers
    p: fraction of values to trim off each end

Returns:
    float

```python
from code.thinkstats2 import TrimmedMean
# Example usage:
result = TrimmedMean(...)  # fill in arguments
```

- `TrimmedMeanVar(t, p=...)`

Computes the trimmed mean and variance of a sequence of numbers.

Side effect: sorts the list.

Args:
    t: sequence of numbers
    p: fraction of values to trim off each end

Returns:
    float

```python
from code.thinkstats2 import TrimmedMeanVar
# Example usage:
result = TrimmedMeanVar(...)  # fill in arguments
```

- `Var(xs, mu=..., ddof=...)`

Computes variance.

xs: sequence of values
mu: option known mean
ddof: delta degrees of freedom

returns: float

```python
from code.thinkstats2 import Var
# Example usage:
result = Var(...)  # fill in arguments
```

### Classes

- `Beta`

Represents a Beta distribution.

See http://en.wikipedia.org/wiki/Beta_distribution

```python
from code.thinkstats2 import Beta
obj = Beta(...)  # construct with appropriate arguments
```

Methods:

  - `Beta.Update(self, data)`

Updates a Beta distribution.

data: pair of int (heads, tails)

```python
# obj is an instance of Beta
obj.Update(...)  # fill in arguments
```

  - `Beta.Mean(self)`

Computes the mean of this distribution.

```python
# obj is an instance of Beta
obj.Mean(...)  # fill in arguments
```

  - `Beta.Random(self)`

Generates a random variate from this distribution.

```python
# obj is an instance of Beta
obj.Random(...)  # fill in arguments
```

  - `Beta.Sample(self, n)`

Generates a random sample from this distribution.

n: int sample size

```python
# obj is an instance of Beta
obj.Sample(...)  # fill in arguments
```

  - `Beta.EvalPdf(self, x)`

Evaluates the PDF at x.

```python
# obj is an instance of Beta
obj.EvalPdf(...)  # fill in arguments
```

  - `Beta.MakePmf(self, steps=..., label=...)`

Returns a Pmf of this distribution.

Note: Normally, we just evaluate the PDF at a sequence
of points and treat the probability density as a probability
mass.

But if alpha or beta is less than one, we have to be
more careful because the PDF goes to infinity at x=0
and x=1.  In that case we evaluate the CDF and compute
differences.

The result is a little funny, because the values at 0 and 1
are not symmetric.  Nevertheless, it is a reasonable discrete
model of the continuous distribution, and behaves well as
the number of values increases.

```python
# obj is an instance of Beta
obj.MakePmf(...)  # fill in arguments
```

  - `Beta.MakeCdf(self, steps=...)`

Returns the CDF of this distribution.

```python
# obj is an instance of Beta
obj.MakeCdf(...)  # fill in arguments
```

  - `Beta.Percentile(self, ps)`

Returns the given percentiles from this distribution.

ps: scalar, array, or list of [0-100]

```python
# obj is an instance of Beta
obj.Percentile(...)  # fill in arguments
```

- `Cdf`

Represents a cumulative distribution function.

Attributes:
    xs: sequence of values
    ps: sequence of probabilities
    label: string used as a graph label.

```python
from code.thinkstats2 import Cdf
obj = Cdf(...)  # construct with appropriate arguments
```

Methods:

  - `Cdf.Copy(self, label=...)`

Returns a copy of this Cdf.

label: string label for the new Cdf

```python
# obj is an instance of Cdf
obj.Copy(...)  # fill in arguments
```

  - `Cdf.MakePmf(self, label=...)`

Makes a Pmf.

```python
# obj is an instance of Cdf
obj.MakePmf(...)  # fill in arguments
```

  - `Cdf.Values(self)`

Returns a sorted list of values.
        

```python
# obj is an instance of Cdf
obj.Values(...)  # fill in arguments
```

  - `Cdf.Items(self)`

Returns a sorted sequence of (value, probability) pairs.

Note: in Python3, returns an iterator.

```python
# obj is an instance of Cdf
obj.Items(...)  # fill in arguments
```

  - `Cdf.Shift(self, term)`

Adds a term to the xs.

term: how much to add

```python
# obj is an instance of Cdf
obj.Shift(...)  # fill in arguments
```

  - `Cdf.Scale(self, factor)`

Multiplies the xs by a factor.

factor: what to multiply by

```python
# obj is an instance of Cdf
obj.Scale(...)  # fill in arguments
```

  - `Cdf.Prob(self, x)`

Returns CDF(x), the probability that corresponds to value x.

Args:
    x: number

Returns:
    float probability

```python
# obj is an instance of Cdf
obj.Prob(...)  # fill in arguments
```

  - `Cdf.Probs(self, xs)`

Gets probabilities for a sequence of values.

xs: any sequence that can be converted to NumPy array

returns: NumPy array of cumulative probabilities

```python
# obj is an instance of Cdf
obj.Probs(...)  # fill in arguments
```

  - `Cdf.Value(self, p)`

Returns InverseCDF(p), the value that corresponds to probability p.

Args:
    p: number in the range [0, 1]

Returns:
    number value

```python
# obj is an instance of Cdf
obj.Value(...)  # fill in arguments
```

  - `Cdf.ValueArray(self, ps)`

Returns InverseCDF(p), the value that corresponds to probability p.

Args:
    ps: NumPy array of numbers in the range [0, 1]

Returns:
    NumPy array of values

```python
# obj is an instance of Cdf
obj.ValueArray(...)  # fill in arguments
```

  - `Cdf.Percentile(self, p)`

Returns the value that corresponds to percentile p.

Args:
    p: number in the range [0, 100]

Returns:
    number value

```python
# obj is an instance of Cdf
obj.Percentile(...)  # fill in arguments
```

  - `Cdf.PercentileRank(self, x)`

Returns the percentile rank of the value x.

x: potential value in the CDF

returns: percentile rank in the range 0 to 100

```python
# obj is an instance of Cdf
obj.PercentileRank(...)  # fill in arguments
```

  - `Cdf.Random(self)`

Chooses a random value from this distribution.

```python
# obj is an instance of Cdf
obj.Random(...)  # fill in arguments
```

  - `Cdf.Sample(self, n)`

Generates a random sample from this distribution.

n: int length of the sample
returns: NumPy array

```python
# obj is an instance of Cdf
obj.Sample(...)  # fill in arguments
```

  - `Cdf.Mean(self)`

Computes the mean of a CDF.

Returns:
    float mean

```python
# obj is an instance of Cdf
obj.Mean(...)  # fill in arguments
```

  - `Cdf.CredibleInterval(self, percentage=...)`

Computes the central credible interval.

If percentage=90, computes the 90% CI.

Args:
    percentage: float between 0 and 100

Returns:
    sequence of two floats, low and high

```python
# obj is an instance of Cdf
obj.CredibleInterval(...)  # fill in arguments
```

  - `Cdf.Render(self, **options)`

Generates a sequence of points suitable for plotting.

An empirical CDF is a step function; linear interpolation
can be misleading.

Note: options are ignored

Returns:
    tuple of (xs, ps)

```python
# obj is an instance of Cdf
obj.Render(...)  # fill in arguments
```

  - `Cdf.Max(self, k)`

Computes the CDF of the maximum of k selections from this dist.

k: int

returns: new Cdf

```python
# obj is an instance of Cdf
obj.Max(...)  # fill in arguments
```

- `Dirichlet`

Represents a Dirichlet distribution.

See http://en.wikipedia.org/wiki/Dirichlet_distribution

```python
from code.thinkstats2 import Dirichlet
obj = Dirichlet(...)  # construct with appropriate arguments
```

Methods:

  - `Dirichlet.Update(self, data)`

Updates a Dirichlet distribution.

data: sequence of observations, in order corresponding to params

```python
# obj is an instance of Dirichlet
obj.Update(...)  # fill in arguments
```

  - `Dirichlet.Random(self)`

Generates a random variate from this distribution.

Returns: normalized vector of fractions

```python
# obj is an instance of Dirichlet
obj.Random(...)  # fill in arguments
```

  - `Dirichlet.Likelihood(self, data)`

Computes the likelihood of the data.

Selects a random vector of probabilities from this distribution.

Returns: float probability

```python
# obj is an instance of Dirichlet
obj.Likelihood(...)  # fill in arguments
```

  - `Dirichlet.LogLikelihood(self, data)`

Computes the log likelihood of the data.

Selects a random vector of probabilities from this distribution.

Returns: float log probability

```python
# obj is an instance of Dirichlet
obj.LogLikelihood(...)  # fill in arguments
```

  - `Dirichlet.MarginalBeta(self, i)`

Computes the marginal distribution of the ith element.

See http://en.wikipedia.org/wiki/Dirichlet_distribution
#Marginal_distributions

i: int

Returns: Beta object

```python
# obj is an instance of Dirichlet
obj.MarginalBeta(...)  # fill in arguments
```

  - `Dirichlet.PredictivePmf(self, xs, label=...)`

Makes a predictive distribution.

xs: values to go into the Pmf

Returns: Pmf that maps from x to the mean prevalence of x

```python
# obj is an instance of Dirichlet
obj.PredictivePmf(...)  # fill in arguments
```

- `EstimatedPdf`

Represents a PDF estimated by KDE.

```python
from code.thinkstats2 import EstimatedPdf
obj = EstimatedPdf(...)  # construct with appropriate arguments
```

Methods:

  - `EstimatedPdf.GetLinspace(self)`

Get a linspace for plotting.

Returns: numpy array

```python
# obj is an instance of EstimatedPdf
obj.GetLinspace(...)  # fill in arguments
```

  - `EstimatedPdf.Density(self, xs)`

Evaluates this Pdf at xs.

returns: float or NumPy array of probability density

```python
# obj is an instance of EstimatedPdf
obj.Density(...)  # fill in arguments
```

  - `EstimatedPdf.Sample(self, n)`

Generates a random sample from the estimated Pdf.

n: size of sample

```python
# obj is an instance of EstimatedPdf
obj.Sample(...)  # fill in arguments
```

- `ExponentialPdf`

Represents the PDF of an exponential distribution.

```python
from code.thinkstats2 import ExponentialPdf
obj = ExponentialPdf(...)  # construct with appropriate arguments
```

Methods:

  - `ExponentialPdf.GetLinspace(self)`

Get a linspace for plotting.

Returns: numpy array

```python
# obj is an instance of ExponentialPdf
obj.GetLinspace(...)  # fill in arguments
```

  - `ExponentialPdf.Density(self, xs)`

Evaluates this Pdf at xs.

xs: scalar or sequence of floats

returns: float or NumPy array of probability density

```python
# obj is an instance of ExponentialPdf
obj.Density(...)  # fill in arguments
```

- `FixedWidthVariables`

Represents a set of variables in a fixed width file.

```python
from code.thinkstats2 import FixedWidthVariables
obj = FixedWidthVariables(...)  # construct with appropriate arguments
```

Methods:

  - `FixedWidthVariables.ReadFixedWidth(self, filename, **options)`

Reads a fixed width ASCII file.

filename: string filename

returns: DataFrame

```python
# obj is an instance of FixedWidthVariables
obj.ReadFixedWidth(...)  # fill in arguments
```

- `Hist`

Represents a histogram, which is a map from values to frequencies.

Values can be any hashable type; frequencies are integer counters.

```python
from code.thinkstats2 import Hist
obj = Hist(...)  # construct with appropriate arguments
```

Methods:

  - `Hist.Freq(self, x)`

Gets the frequency associated with the value x.

Args:
    x: number value

Returns:
    int frequency

```python
# obj is an instance of Hist
obj.Freq(...)  # fill in arguments
```

  - `Hist.Freqs(self, xs)`

Gets frequencies for a sequence of values.

```python
# obj is an instance of Hist
obj.Freqs(...)  # fill in arguments
```

  - `Hist.IsSubset(self, other)`

Checks whether the values in this histogram are a subset of
the values in the given histogram.

```python
# obj is an instance of Hist
obj.IsSubset(...)  # fill in arguments
```

  - `Hist.Subtract(self, other)`

Subtracts the values in the given histogram from this histogram.

```python
# obj is an instance of Hist
obj.Subtract(...)  # fill in arguments
```

- `HypothesisTest`

Represents a hypothesis test.

```python
from code.thinkstats2 import HypothesisTest
obj = HypothesisTest(...)  # construct with appropriate arguments
```

Methods:

  - `HypothesisTest.PValue(self, iters=...)`

Computes the distribution of the test statistic and p-value.

iters: number of iterations

returns: float p-value

```python
# obj is an instance of HypothesisTest
obj.PValue(...)  # fill in arguments
```

  - `HypothesisTest.MaxTestStat(self)`

Returns the largest test statistic seen during simulations.
        

```python
# obj is an instance of HypothesisTest
obj.MaxTestStat(...)  # fill in arguments
```

  - `HypothesisTest.PlotCdf(self, label=...)`

Draws a Cdf with vertical lines at the observed test stat.
        

```python
# obj is an instance of HypothesisTest
obj.PlotCdf(...)  # fill in arguments
```

  - `HypothesisTest.TestStatistic(self, data)`

Computes the test statistic.

data: data in whatever form is relevant        

```python
# obj is an instance of HypothesisTest
obj.TestStatistic(...)  # fill in arguments
```

  - `HypothesisTest.MakeModel(self)`

Build a model of the null hypothesis.
        

```python
# obj is an instance of HypothesisTest
obj.MakeModel(...)  # fill in arguments
```

  - `HypothesisTest.RunModel(self)`

Run the model of the null hypothesis.

returns: simulated data

```python
# obj is an instance of HypothesisTest
obj.RunModel(...)  # fill in arguments
```

- `Interpolator`

Represents a mapping between sorted sequences; performs linear interp.

Attributes:
    xs: sorted list
    ys: sorted list

```python
from code.thinkstats2 import Interpolator
obj = Interpolator(...)  # construct with appropriate arguments
```

Methods:

  - `Interpolator.Lookup(self, x)`

Looks up x and returns the corresponding value of y.

```python
# obj is an instance of Interpolator
obj.Lookup(...)  # fill in arguments
```

  - `Interpolator.Reverse(self, y)`

Looks up y and returns the corresponding value of x.

```python
# obj is an instance of Interpolator
obj.Reverse(...)  # fill in arguments
```

- `Joint`

Represents a joint distribution.

The values are sequences (usually tuples)

```python
from code.thinkstats2 import Joint
obj = Joint(...)  # construct with appropriate arguments
```

Methods:

  - `Joint.Marginal(self, i, label=...)`

Gets the marginal distribution of the indicated variable.

i: index of the variable we want

Returns: Pmf

```python
# obj is an instance of Joint
obj.Marginal(...)  # fill in arguments
```

  - `Joint.Conditional(self, i, j, val, label=...)`

Gets the conditional distribution of the indicated variable.

Distribution of vs[i], conditioned on vs[j] = val.

i: index of the variable we want
j: which variable is conditioned on
val: the value the jth variable has to have

Returns: Pmf

```python
# obj is an instance of Joint
obj.Conditional(...)  # fill in arguments
```

  - `Joint.MaxLikeInterval(self, percentage=...)`

Returns the maximum-likelihood credible interval.

If percentage=90, computes a 90% CI containing the values
with the highest likelihoods.

percentage: float between 0 and 100

Returns: list of values from the suite

```python
# obj is an instance of Joint
obj.MaxLikeInterval(...)  # fill in arguments
```

- `NormalPdf`

Represents the PDF of a Normal distribution.

```python
from code.thinkstats2 import NormalPdf
obj = NormalPdf(...)  # construct with appropriate arguments
```

Methods:

  - `NormalPdf.GetLinspace(self)`

Get a linspace for plotting.

Returns: numpy array

```python
# obj is an instance of NormalPdf
obj.GetLinspace(...)  # fill in arguments
```

  - `NormalPdf.Density(self, xs)`

Evaluates this Pdf at xs.

xs: scalar or sequence of floats

returns: float or NumPy array of probability density

```python
# obj is an instance of NormalPdf
obj.Density(...)  # fill in arguments
```

- `Pdf`

Represents a probability density function (PDF).

```python
from code.thinkstats2 import Pdf
obj = Pdf(...)  # construct with appropriate arguments
```

Methods:

  - `Pdf.Density(self, x)`

Evaluates this Pdf at x.

Returns: float or NumPy array of probability density

```python
# obj is an instance of Pdf
obj.Density(...)  # fill in arguments
```

  - `Pdf.GetLinspace(self)`

Get a linspace for plotting.

Not all subclasses of Pdf implement this.

Returns: numpy array

```python
# obj is an instance of Pdf
obj.GetLinspace(...)  # fill in arguments
```

  - `Pdf.MakePmf(self, **options)`

Makes a discrete version of this Pdf.

options can include
label: string
low: low end of range
high: high end of range
n: number of places to evaluate

Returns: new Pmf

```python
# obj is an instance of Pdf
obj.MakePmf(...)  # fill in arguments
```

  - `Pdf.Render(self, **options)`

Generates a sequence of points suitable for plotting.

If options includes low and high, it must also include n;
in that case the density is evaluated an n locations between
low and high, including both.

If options includes xs, the density is evaluate at those location.

Otherwise, self.GetLinspace is invoked to provide the locations.

Returns:
    tuple of (xs, densities)

```python
# obj is an instance of Pdf
obj.Render(...)  # fill in arguments
```

  - `Pdf.Items(self)`

Generates a sequence of (value, probability) pairs.
        

```python
# obj is an instance of Pdf
obj.Items(...)  # fill in arguments
```

- `Pmf`

Represents a probability mass function.

Values can be any hashable type; probabilities are floating-point.
Pmfs are not necessarily normalized.

```python
from code.thinkstats2 import Pmf
obj = Pmf(...)  # construct with appropriate arguments
```

Methods:

  - `Pmf.Prob(self, x, default=...)`

Gets the probability associated with the value x.

Args:
    x: number value
    default: value to return if the key is not there

Returns:
    float probability

```python
# obj is an instance of Pmf
obj.Prob(...)  # fill in arguments
```

  - `Pmf.Probs(self, xs)`

Gets probabilities for a sequence of values.

```python
# obj is an instance of Pmf
obj.Probs(...)  # fill in arguments
```

  - `Pmf.Percentile(self, percentage)`

Computes a percentile of a given Pmf.

Note: this is not super efficient.  If you are planning
to compute more than a few percentiles, compute the Cdf.

percentage: float 0-100

returns: value from the Pmf

```python
# obj is an instance of Pmf
obj.Percentile(...)  # fill in arguments
```

  - `Pmf.ProbGreater(self, x)`

Probability that a sample from this Pmf exceeds x.

x: number

returns: float probability

```python
# obj is an instance of Pmf
obj.ProbGreater(...)  # fill in arguments
```

  - `Pmf.ProbLess(self, x)`

Probability that a sample from this Pmf is less than x.

x: number

returns: float probability

```python
# obj is an instance of Pmf
obj.ProbLess(...)  # fill in arguments
```

  - `Pmf.Normalize(self, fraction=...)`

Normalizes this PMF so the sum of all probs is fraction.

Args:
    fraction: what the total should be after normalization

Returns: the total probability before normalizing

```python
# obj is an instance of Pmf
obj.Normalize(...)  # fill in arguments
```

  - `Pmf.Random(self)`

Chooses a random element from this PMF.

Note: this is not very efficient.  If you plan to call
this more than a few times, consider converting to a CDF.

Returns:
    float value from the Pmf

```python
# obj is an instance of Pmf
obj.Random(...)  # fill in arguments
```

  - `Pmf.Mean(self)`

Computes the mean of a PMF.

Returns:
    float mean

```python
# obj is an instance of Pmf
obj.Mean(...)  # fill in arguments
```

  - `Pmf.Var(self, mu=...)`

Computes the variance of a PMF.

mu: the point around which the variance is computed;
        if omitted, computes the mean

returns: float variance

```python
# obj is an instance of Pmf
obj.Var(...)  # fill in arguments
```

  - `Pmf.Std(self, mu=...)`

Computes the standard deviation of a PMF.

mu: the point around which the variance is computed;
        if omitted, computes the mean

returns: float standard deviation

```python
# obj is an instance of Pmf
obj.Std(...)  # fill in arguments
```

  - `Pmf.MaximumLikelihood(self)`

Returns the value with the highest probability.

Returns: float probability

```python
# obj is an instance of Pmf
obj.MaximumLikelihood(...)  # fill in arguments
```

  - `Pmf.CredibleInterval(self, percentage=...)`

Computes the central credible interval.

If percentage=90, computes the 90% CI.

Args:
    percentage: float between 0 and 100

Returns:
    sequence of two floats, low and high

```python
# obj is an instance of Pmf
obj.CredibleInterval(...)  # fill in arguments
```

  - `Pmf.AddPmf(self, other)`

Computes the Pmf of the sum of values drawn from self and other.

other: another Pmf

returns: new Pmf

```python
# obj is an instance of Pmf
obj.AddPmf(...)  # fill in arguments
```

  - `Pmf.AddConstant(self, other)`

Computes the Pmf of the sum a constant and values from self.

other: a number

returns: new Pmf

```python
# obj is an instance of Pmf
obj.AddConstant(...)  # fill in arguments
```

  - `Pmf.SubPmf(self, other)`

Computes the Pmf of the diff of values drawn from self and other.

other: another Pmf

returns: new Pmf

```python
# obj is an instance of Pmf
obj.SubPmf(...)  # fill in arguments
```

  - `Pmf.MulPmf(self, other)`

Computes the Pmf of the diff of values drawn from self and other.

other: another Pmf

returns: new Pmf

```python
# obj is an instance of Pmf
obj.MulPmf(...)  # fill in arguments
```

  - `Pmf.MulConstant(self, other)`

Computes the Pmf of the product of a constant and values from self.

other: a number

returns: new Pmf

```python
# obj is an instance of Pmf
obj.MulConstant(...)  # fill in arguments
```

  - `Pmf.DivPmf(self, other)`

Computes the Pmf of the ratio of values drawn from self and other.

other: another Pmf

returns: new Pmf

```python
# obj is an instance of Pmf
obj.DivPmf(...)  # fill in arguments
```

  - `Pmf.Max(self, k)`

Computes the CDF of the maximum of k selections from this dist.

k: int

returns: new Cdf

```python
# obj is an instance of Pmf
obj.Max(...)  # fill in arguments
```

- `Suite`

Represents a suite of hypotheses and their probabilities.

```python
from code.thinkstats2 import Suite
obj = Suite(...)  # construct with appropriate arguments
```

Methods:

  - `Suite.Update(self, data)`

Updates each hypothesis based on the data.

data: any representation of the data

returns: the normalizing constant

```python
# obj is an instance of Suite
obj.Update(...)  # fill in arguments
```

  - `Suite.LogUpdate(self, data)`

Updates a suite of hypotheses based on new data.

Modifies the suite directly; if you want to keep the original, make
a copy.

Note: unlike Update, LogUpdate does not normalize.

Args:
    data: any representation of the data

```python
# obj is an instance of Suite
obj.LogUpdate(...)  # fill in arguments
```

  - `Suite.UpdateSet(self, dataset)`

Updates each hypothesis based on the dataset.

This is more efficient than calling Update repeatedly because
it waits until the end to Normalize.

Modifies the suite directly; if you want to keep the original, make
a copy.

dataset: a sequence of data

returns: the normalizing constant

```python
# obj is an instance of Suite
obj.UpdateSet(...)  # fill in arguments
```

  - `Suite.LogUpdateSet(self, dataset)`

Updates each hypothesis based on the dataset.

Modifies the suite directly; if you want to keep the original, make
a copy.

dataset: a sequence of data

returns: None

```python
# obj is an instance of Suite
obj.LogUpdateSet(...)  # fill in arguments
```

  - `Suite.Likelihood(self, data, hypo)`

Computes the likelihood of the data under the hypothesis.

hypo: some representation of the hypothesis
data: some representation of the data

```python
# obj is an instance of Suite
obj.Likelihood(...)  # fill in arguments
```

  - `Suite.LogLikelihood(self, data, hypo)`

Computes the log likelihood of the data under the hypothesis.

hypo: some representation of the hypothesis
data: some representation of the data

```python
# obj is an instance of Suite
obj.LogLikelihood(...)  # fill in arguments
```

  - `Suite.Print(self)`

Prints the hypotheses and their probabilities.

```python
# obj is an instance of Suite
obj.Print(...)  # fill in arguments
```

  - `Suite.MakeOdds(self)`

Transforms from probabilities to odds.

Values with prob=0 are removed.

```python
# obj is an instance of Suite
obj.MakeOdds(...)  # fill in arguments
```

  - `Suite.MakeProbs(self)`

Transforms from odds to probabilities.

```python
# obj is an instance of Suite
obj.MakeProbs(...)  # fill in arguments
```

- `UnimplementedMethodException`

Exception if someone calls a method that should be overridden.

```python
from code.thinkstats2 import UnimplementedMethodException
obj = UnimplementedMethodException(...)  # construct with appropriate arguments
```
