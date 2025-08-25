## Module `code.probability`

This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.probability import *  # or import specific names
```

### Functions

- `BiasPmf(pmf, label=...)`

Returns the Pmf with oversampling proportional to value.

If pmf is the distribution of true values, the result is the
distribution that would be seen if values are oversampled in
proportion to their values; for example, if you ask students
how big their classes are, large classes are oversampled in
proportion to their size.

Args:
  pmf: Pmf object.
  label: string label for the new Pmf.

 Returns:
   Pmf object

```python
from code.probability import BiasPmf
# Example usage:
result = BiasPmf(...)  # fill in arguments
```

- `ClassSizes()`

Generate PMFs of observed and actual class size.
    

```python
from code.probability import ClassSizes
# Example usage:
result = ClassSizes(...)  # fill in arguments
```

- `main(script)`
```python
from code.probability import main
# Example usage:
result = main(...)  # fill in arguments
```

- `MakeFigures(firsts, others)`

Plot Pmfs of pregnancy length.

firsts: DataFrame
others: DataFrame

```python
from code.probability import MakeFigures
# Example usage:
result = MakeFigures(...)  # fill in arguments
```

- `MakeHists(live)`

Plot Hists for live births

live: DataFrame
others: DataFrame

```python
from code.probability import MakeHists
# Example usage:
result = MakeHists(...)  # fill in arguments
```

- `UnbiasPmf(pmf, label=...)`

Returns the Pmf with oversampling proportional to 1/value.

Args:
  pmf: Pmf object.
  label: string label for the new Pmf.

 Returns:
   Pmf object

```python
from code.probability import UnbiasPmf
# Example usage:
result = UnbiasPmf(...)  # fill in arguments
```
