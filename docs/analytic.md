## Module `code.analytic`

This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.analytic import *  # or import specific names
```

### Functions

- `main()`
```python
from code.analytic import main
# Example usage:
result = main(...)  # fill in arguments
```

- `MakeBabyBoom()`

Plot CDF of interarrival time on log and linear scales.
    

```python
from code.analytic import MakeBabyBoom
# Example usage:
result = MakeBabyBoom(...)  # fill in arguments
```

- `MakeExampleNormalPlot()`

Generates a sample normal probability plot.
    

```python
from code.analytic import MakeExampleNormalPlot
# Example usage:
result = MakeExampleNormalPlot(...)  # fill in arguments
```

- `MakeExpoCdf()`

Generates a plot of the exponential CDF.

```python
from code.analytic import MakeExpoCdf
# Example usage:
result = MakeExpoCdf(...)  # fill in arguments
```

- `MakeNormalCdf()`

Generates a plot of the normal CDF.

```python
from code.analytic import MakeNormalCdf
# Example usage:
result = MakeNormalCdf(...)  # fill in arguments
```

- `MakeNormalModel(weights)`

Plot the CDF of birthweights with a normal model.

```python
from code.analytic import MakeNormalModel
# Example usage:
result = MakeNormalModel(...)  # fill in arguments
```

- `MakeNormalPlot(weights, term_weights)`

Generates a normal probability plot of birth weights.

```python
from code.analytic import MakeNormalPlot
# Example usage:
result = MakeNormalPlot(...)  # fill in arguments
```

- `MakeParetoCdf()`

Generates a plot of the Pareto CDF.

```python
from code.analytic import MakeParetoCdf
# Example usage:
result = MakeParetoCdf(...)  # fill in arguments
```

- `MakeParetoCdf2()`

Generates a plot of the CDF of height in Pareto World.

```python
from code.analytic import MakeParetoCdf2
# Example usage:
result = MakeParetoCdf2(...)  # fill in arguments
```

- `ParetoMedian(xmin, alpha)`

Computes the median of a Pareto distribution.

```python
from code.analytic import ParetoMedian
# Example usage:
result = ParetoMedian(...)  # fill in arguments
```

- `ReadBabyBoom(filename=...)`

Reads the babyboom data.

filename: string

returns: DataFrame

```python
from code.analytic import ReadBabyBoom
# Example usage:
result = ReadBabyBoom(...)  # fill in arguments
```
