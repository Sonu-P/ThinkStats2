## Module `code.thinkplot`

This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.thinkplot import *  # or import specific names
```

### Functions

- `Bar(xs, ys, **options)`

Plots a line.

Args:
  xs: sequence of x values
  ys: sequence of y values
  options: keyword args passed to plt.bar

```python
from code.thinkplot import Bar
# Example usage:
result = Bar(...)  # fill in arguments
```

- `Cdf(cdf, complement=..., transform=..., **options)`

Plots a CDF as a line.

Args:
  cdf: Cdf object
  complement: boolean, whether to plot the complementary CDF
  transform: string, one of 'exponential', 'pareto', 'weibull', 'gumbel'
  options: keyword args passed to plt.plot

Returns:
  dictionary with the scale options that should be passed to
  Config, Show or Save.

```python
from code.thinkplot import Cdf
# Example usage:
result = Cdf(...)  # fill in arguments
```

- `Cdfs(cdfs, complement=..., transform=..., **options)`

Plots a sequence of CDFs.

cdfs: sequence of CDF objects
complement: boolean, whether to plot the complementary CDF
transform: string, one of 'exponential', 'pareto', 'weibull', 'gumbel'
options: keyword args passed to plt.plot

```python
from code.thinkplot import Cdfs
# Example usage:
result = Cdfs(...)  # fill in arguments
```

- `Clf()`

Clears the figure and any hints that have been set.

```python
from code.thinkplot import Clf
# Example usage:
result = Clf(...)  # fill in arguments
```

- `Config(**options)`

Configures the plot.

Pulls options out of the option dictionary and passes them to
the corresponding plt functions.

```python
from code.thinkplot import Config
# Example usage:
result = Config(...)  # fill in arguments
```

- `Contour(obj, pcolor=..., contour=..., imshow=..., **options)`

Makes a contour plot.

d: map from (x, y) to z, or object that provides GetDict
pcolor: boolean, whether to make a pseudocolor plot
contour: boolean, whether to make a contour plot
imshow: boolean, whether to use plt.imshow
options: keyword args passed to plt.pcolor and/or plt.contour

```python
from code.thinkplot import Contour
# Example usage:
result = Contour(...)  # fill in arguments
```

- `Diff(t)`

Compute the differences between adjacent elements in a sequence.

Args:
    t: sequence of number

Returns:
    sequence of differences (length one less than t)

```python
from code.thinkplot import Diff
# Example usage:
result = Diff(...)  # fill in arguments
```

- `Figure(**options)`

Sets options for the current figure.

```python
from code.thinkplot import Figure
# Example usage:
result = Figure(...)  # fill in arguments
```

- `FillBetween(xs, y1, y2=..., where=..., **options)`

Fills the space between two lines.

Args:
  xs: sequence of x values
  y1: sequence of y values
  y2: sequence of y values
  where: sequence of boolean
  options: keyword args passed to plt.fill_between

```python
from code.thinkplot import FillBetween
# Example usage:
result = FillBetween(...)  # fill in arguments
```

- `HexBin(xs, ys, **options)`

Makes a scatter plot.

xs: x values
ys: y values
options: options passed to plt.scatter

```python
from code.thinkplot import HexBin
# Example usage:
result = HexBin(...)  # fill in arguments
```

- `Hist(hist, **options)`

Plots a Pmf or Hist with a bar plot.

The default width of the bars is based on the minimum difference
between values in the Hist.  If that's too small, you can override
it by providing a width keyword argument, in the same units
as the values.

Args:
  hist: Hist or Pmf object
  options: keyword args passed to plt.bar

```python
from code.thinkplot import Hist
# Example usage:
result = Hist(...)  # fill in arguments
```

- `Hists(hists, **options)`

Plots two histograms as interleaved bar plots.

Options are passed along for all PMFs.  If you want different
options for each pmf, make multiple calls to Pmf.

Args:
  hists: list of two Hist or Pmf objects
  options: keyword args passed to plt.plot

```python
from code.thinkplot import Hists
# Example usage:
result = Hists(...)  # fill in arguments
```

- `Hlines(ys, x1, x2, **options)`

Plots a set of horizontal lines.

Args:
  ys: sequence of y values
  x1: sequence of x values
  x2: sequence of x values
  options: keyword args passed to plt.vlines

```python
from code.thinkplot import Hlines
# Example usage:
result = Hlines(...)  # fill in arguments
```

- `main()`
```python
from code.thinkplot import main
# Example usage:
result = main(...)  # fill in arguments
```

- `Pcolor(xs, ys, zs, pcolor=..., contour=..., **options)`

Makes a pseudocolor plot.

xs:
ys:
zs:
pcolor: boolean, whether to make a pseudocolor plot
contour: boolean, whether to make a contour plot
options: keyword args passed to plt.pcolor and/or plt.contour

```python
from code.thinkplot import Pcolor
# Example usage:
result = Pcolor(...)  # fill in arguments
```

- `Pdf(pdf, **options)`

Plots a Pdf, Pmf, or Hist as a line.

Args:
  pdf: Pdf, Pmf, or Hist object
  options: keyword args passed to plt.plot

```python
from code.thinkplot import Pdf
# Example usage:
result = Pdf(...)  # fill in arguments
```

- `Pdfs(pdfs, **options)`

Plots a sequence of PDFs.

Options are passed along for all PDFs.  If you want different
options for each pdf, make multiple calls to Pdf.

Args:
  pdfs: sequence of PDF objects
  options: keyword args passed to plt.plot

```python
from code.thinkplot import Pdfs
# Example usage:
result = Pdfs(...)  # fill in arguments
```

- `Plot(obj, ys=..., style=..., **options)`

Plots a line.

Args:
  obj: sequence of x values, or Series, or anything with Render()
  ys: sequence of y values
  style: style string passed along to plt.plot
  options: keyword args passed to plt.plot

```python
from code.thinkplot import Plot
# Example usage:
result = Plot(...)  # fill in arguments
```

- `Plotly(**options)`

Shows the plot.

For options, see Config.

options: keyword args used to invoke various plt functions

```python
from code.thinkplot import Plotly
# Example usage:
result = Plotly(...)  # fill in arguments
```

- `Pmf(pmf, **options)`

Plots a Pmf or Hist as a line.

Args:
  pmf: Hist or Pmf object
  options: keyword args passed to plt.plot

```python
from code.thinkplot import Pmf
# Example usage:
result = Pmf(...)  # fill in arguments
```

- `Pmfs(pmfs, **options)`

Plots a sequence of PMFs.

Options are passed along for all PMFs.  If you want different
options for each pmf, make multiple calls to Pmf.

Args:
  pmfs: sequence of PMF objects
  options: keyword args passed to plt.plot

```python
from code.thinkplot import Pmfs
# Example usage:
result = Pmfs(...)  # fill in arguments
```

- `PrePlot(num=..., rows=..., cols=...)`

Takes hints about what's coming.

num: number of lines that will be plotted
rows: number of rows of subplots
cols: number of columns of subplots

```python
from code.thinkplot import PrePlot
# Example usage:
result = PrePlot(...)  # fill in arguments
```

- `Save(root=..., formats=..., **options)`

Saves the plot in the given formats and clears the figure.

For options, see Config.

Args:
  root: string filename root
  formats: list of string formats
  options: keyword args used to invoke various plt functions

```python
from code.thinkplot import Save
# Example usage:
result = Save(...)  # fill in arguments
```

- `SaveFormat(root, fmt=..., **options)`

Writes the current figure to a file in the given format.

Args:
  root: string filename root
  fmt: string format

```python
from code.thinkplot import SaveFormat
# Example usage:
result = SaveFormat(...)  # fill in arguments
```

- `Scatter(xs, ys=..., **options)`

Makes a scatter plot.

xs: x values
ys: y values
options: options passed to plt.scatter

```python
from code.thinkplot import Scatter
# Example usage:
result = Scatter(...)  # fill in arguments
```

- `Show(**options)`

Shows the plot.

For options, see Config.

options: keyword args used to invoke various plt functions

```python
from code.thinkplot import Show
# Example usage:
result = Show(...)  # fill in arguments
```

- `SubPlot(plot_number, rows=..., cols=..., **options)`

Configures the number of subplots and changes the current plot.

rows: int
cols: int
plot_number: int
options: passed to subplot

```python
from code.thinkplot import SubPlot
# Example usage:
result = SubPlot(...)  # fill in arguments
```

- `Text(x, y, s, **options)`

Puts text in a figure.

x: number
y: number
s: string
options: keyword args passed to plt.text

```python
from code.thinkplot import Text
# Example usage:
result = Text(...)  # fill in arguments
```

- `Vlines(xs, y1, y2, **options)`

Plots a set of vertical lines.

Args:
  xs: sequence of x values
  y1: sequence of y values
  y2: sequence of y values
  options: keyword args passed to plt.vlines

```python
from code.thinkplot import Vlines
# Example usage:
result = Vlines(...)  # fill in arguments
```
