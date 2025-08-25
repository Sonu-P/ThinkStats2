## Module `code.timeseries`

This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.timeseries import *  # or import specific names
```

### Functions

- `AddWeeklySeasonality(daily)`

Adds a weekly pattern.

daily: DataFrame of daily prices

returns: new DataFrame of daily prices

```python
from code.timeseries import AddWeeklySeasonality
# Example usage:
result = AddWeeklySeasonality(...)  # fill in arguments
```

- `Correlate(dailies)`

Compute the correlation matrix between prices for difference qualities.

dailies: map from quality to time series of ppg

returns: correlation matrix

```python
from code.timeseries import Correlate
# Example usage:
result = Correlate(...)  # fill in arguments
```

- `CorrelateResid(dailies)`

Compute the correlation matrix between residuals.

dailies: map from quality to time series of ppg

returns: correlation matrix

```python
from code.timeseries import CorrelateResid
# Example usage:
result = CorrelateResid(...)  # fill in arguments
```

- `FillMissing(daily, span=...)`

Fills missing values with an exponentially weighted moving average.

Resulting DataFrame has new columns 'ewma' and 'resid'.

daily: DataFrame of daily prices
span: window size (sort of) passed to ewma

returns: new DataFrame of daily prices

```python
from code.timeseries import FillMissing
# Example usage:
result = FillMissing(...)  # fill in arguments
```

- `GeneratePredictions(result_seq, years, add_resid=...)`

Generates an array of predicted values from a list of model results.

When add_resid is False, predictions represent sampling error only.

When add_resid is True, they also include residual error (which is
more relevant to prediction).

result_seq: list of model results
years: sequence of times (in years) to make predictions for
add_resid: boolean, whether to add in resampled residuals

returns: sequence of predictions

```python
from code.timeseries import GeneratePredictions
# Example usage:
result = GeneratePredictions(...)  # fill in arguments
```

- `GenerateSimplePrediction(results, years)`

Generates a simple prediction.

results: results object
years: sequence of times (in years) to make predictions for

returns: sequence of predicted values

```python
from code.timeseries import GenerateSimplePrediction
# Example usage:
result = GenerateSimplePrediction(...)  # fill in arguments
```

- `GroupByDay(transactions, func=...)`

Groups transactions by day and compute the daily mean ppg.

transactions: DataFrame of transactions

returns: DataFrame of daily prices

```python
from code.timeseries import GroupByDay
# Example usage:
result = GroupByDay(...)  # fill in arguments
```

- `GroupByQualityAndDay(transactions)`

Divides transactions by quality and computes mean daily price.

transaction: DataFrame of transactions

returns: map from quality to time series of ppg

```python
from code.timeseries import GroupByQualityAndDay
# Example usage:
result = GroupByQualityAndDay(...)  # fill in arguments
```

- `main(name)`
```python
from code.timeseries import main
# Example usage:
result = main(...)  # fill in arguments
```

- `MakeAcfPlot(dailies)`

Makes a figure showing autocorrelation functions.

dailies: map from category name to DataFrame of daily prices    

```python
from code.timeseries import MakeAcfPlot
# Example usage:
result = MakeAcfPlot(...)  # fill in arguments
```

- `PlotAutoCorrelation(dailies, nlags=..., add_weekly=...)`

Plots autocorrelation functions.

dailies: map from category name to DataFrame of daily prices
nlags: number of lags to compute
add_weekly: boolean, whether to add a simulated weekly pattern

```python
from code.timeseries import PlotAutoCorrelation
# Example usage:
result = PlotAutoCorrelation(...)  # fill in arguments
```

- `PlotDailies(dailies)`

Makes a plot with daily prices for different qualities.

dailies: map from name to DataFrame

```python
from code.timeseries import PlotDailies
# Example usage:
result = PlotDailies(...)  # fill in arguments
```

- `PlotFilled(daily, name)`

Plots the EWMA and filled data.

daily: DataFrame of daily prices

```python
from code.timeseries import PlotFilled
# Example usage:
result = PlotFilled(...)  # fill in arguments
```

- `PlotFittedValues(model, results, label=...)`

Plots original data and fitted values.

model: StatsModel model object
results: StatsModel results object

```python
from code.timeseries import PlotFittedValues
# Example usage:
result = PlotFittedValues(...)  # fill in arguments
```

- `PlotIntervals(daily, years, iters=..., percent=..., func=...)`

Plots predictions based on different intervals.

daily: DataFrame of daily prices
years: sequence of times (in years) to make predictions for
iters: number of simulations
percent: what percentile range to show
func: function that fits a model to the data

```python
from code.timeseries import PlotIntervals
# Example usage:
result = PlotIntervals(...)  # fill in arguments
```

- `PlotLinearModel(daily, name)`

Plots a linear fit to a sequence of prices, and the residuals.

daily: DataFrame of daily prices
name: string

```python
from code.timeseries import PlotLinearModel
# Example usage:
result = PlotLinearModel(...)  # fill in arguments
```

- `PlotPredictions(daily, years, iters=..., percent=..., func=...)`

Plots predictions.

daily: DataFrame of daily prices
years: sequence of times (in years) to make predictions for
iters: number of simulations
percent: what percentile range to show
func: function that fits a model to the data

```python
from code.timeseries import PlotPredictions
# Example usage:
result = PlotPredictions(...)  # fill in arguments
```

- `PlotResidualPercentiles(model, results, index=..., num_bins=...)`

Plots percentiles of the residuals.

model: StatsModel model object
results: StatsModel results object
index: which exogenous variable to use
num_bins: how many bins to divide the x-axis into

```python
from code.timeseries import PlotResidualPercentiles
# Example usage:
result = PlotResidualPercentiles(...)  # fill in arguments
```

- `PlotResiduals(model, results)`

Plots the residuals of a model.

model: StatsModel model object
results: StatsModel results object    

```python
from code.timeseries import PlotResiduals
# Example usage:
result = PlotResiduals(...)  # fill in arguments
```

- `PlotRollingMean(daily, name)`

Plots rolling mean and EWMA.

daily: DataFrame of daily prices

```python
from code.timeseries import PlotRollingMean
# Example usage:
result = PlotRollingMean(...)  # fill in arguments
```

- `PrintSerialCorrelations(dailies)`

Prints a table of correlations with different lags.

dailies: map from category name to DataFrame of daily prices

```python
from code.timeseries import PrintSerialCorrelations
# Example usage:
result = PrintSerialCorrelations(...)  # fill in arguments
```

- `ReadData()`

Reads data about cannabis transactions.

http://zmjones.com/static/data/mj-clean.csv

returns: DataFrame

```python
from code.timeseries import ReadData
# Example usage:
result = ReadData(...)  # fill in arguments
```

- `RunLinearModel(daily)`

Runs a linear model of prices versus years.

daily: DataFrame of daily prices

returns: model, results

```python
from code.timeseries import RunLinearModel
# Example usage:
result = RunLinearModel(...)  # fill in arguments
```

- `RunModels(dailies)`

Runs linear regression for each group in dailies.

dailies: map from group name to DataFrame

```python
from code.timeseries import RunModels
# Example usage:
result = RunModels(...)  # fill in arguments
```

- `SimulateAutocorrelation(daily, iters=..., nlags=...)`

Resample residuals, compute autocorrelation, and plot percentiles.

daily: DataFrame
iters: number of simulations to run
nlags: maximum lags to compute autocorrelation

```python
from code.timeseries import SimulateAutocorrelation
# Example usage:
result = SimulateAutocorrelation(...)  # fill in arguments
```

- `SimulateIntervals(daily, iters=..., func=...)`

Run simulations based on different subsets of the data.

daily: DataFrame of daily prices
iters: number of simulations
func: function that fits a model to the data

returns: list of result objects

```python
from code.timeseries import SimulateIntervals
# Example usage:
result = SimulateIntervals(...)  # fill in arguments
```

- `SimulateResults(daily, iters=..., func=...)`

Run simulations based on resampling residuals.

daily: DataFrame of daily prices
iters: number of simulations
func: function that fits a model to the data

returns: list of result objects

```python
from code.timeseries import SimulateResults
# Example usage:
result = SimulateResults(...)  # fill in arguments
```

- `TestCorrelateResid(dailies, iters=...)`

Tests observed correlations.

dailies: map from quality to time series of ppg
iters: number of simulations

```python
from code.timeseries import TestCorrelateResid
# Example usage:
result = TestCorrelateResid(...)  # fill in arguments
```

- `tmean(series)`

Computes a trimmed mean.

series: Series 

returns: float

```python
from code.timeseries import tmean
# Example usage:
result = tmean(...)  # fill in arguments
```
