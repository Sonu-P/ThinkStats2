## Module `code.cumulative`

This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.cumulative import *  # or import specific names
```

### Functions

- `EvalCdf(sample, x)`

Computes CDF(x) in a sample.

sample: sequence
x: value

returns: cumulative probability

```python
from code.cumulative import EvalCdf
# Example usage:
result = EvalCdf(...)  # fill in arguments
```

- `main(name, data_dir=...)`
```python
from code.cumulative import main
# Example usage:
result = main(...)  # fill in arguments
```

- `MakeCdf(live)`

Plot the CDF of pregnancy lengths for live births.

live: DataFrame for live births

```python
from code.cumulative import MakeCdf
# Example usage:
result = MakeCdf(...)  # fill in arguments
```

- `MakeExample()`

Makes a simple example CDF.

```python
from code.cumulative import MakeExample
# Example usage:
result = MakeExample(...)  # fill in arguments
```

- `MakeFigures(live, firsts, others)`

Creates several figures for the book.

live: DataFrame
firsts: DataFrame
others: DataFrame

```python
from code.cumulative import MakeFigures
# Example usage:
result = MakeFigures(...)  # fill in arguments
```

- `Percentile(scores, percentile_rank)`

Computes the value that corresponds to a given percentile rank. 

```python
from code.cumulative import Percentile
# Example usage:
result = Percentile(...)  # fill in arguments
```

- `Percentile2(scores, percentile_rank)`

Computes the value that corresponds to a given percentile rank.

Slightly more efficient.

```python
from code.cumulative import Percentile2
# Example usage:
result = Percentile2(...)  # fill in arguments
```

- `PercentileRank(scores, your_score)`

Computes the percentile rank relative to a sample of scores.

```python
from code.cumulative import PercentileRank
# Example usage:
result = PercentileRank(...)  # fill in arguments
```

- `PercentileToPosition(percentile, field_size)`

Converts from percentile to hypothetical position in the field.

percentile: 0-100
field_size: int

```python
from code.cumulative import PercentileToPosition
# Example usage:
result = PercentileToPosition(...)  # fill in arguments
```

- `PositionToPercentile(position, field_size)`

Converts from position in the field to percentile.

position: int
field_size: int

```python
from code.cumulative import PositionToPercentile
# Example usage:
result = PositionToPercentile(...)  # fill in arguments
```

- `RandomFigure(live)`
```python
from code.cumulative import RandomFigure
# Example usage:
result = RandomFigure(...)  # fill in arguments
```

- `TestSample(live)`

Plots the distribution of weights against a random sample.

live: DataFrame for live births

```python
from code.cumulative import TestSample
# Example usage:
result = TestSample(...)  # fill in arguments
```
