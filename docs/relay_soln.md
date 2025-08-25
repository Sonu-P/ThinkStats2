## Module `code.relay_soln`

This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.relay_soln import *  # or import specific names
```

### Functions

- `main()`
```python
from code.relay_soln import main
# Example usage:
result = main(...)  # fill in arguments
```

- `ObservedPmf(pmf, speed, label=...)`

Returns a new Pmf representing speeds observed at a given speed.

The chance of observing a runner is proportional to the difference
in speed.

Args:
    pmf: distribution of actual speeds
    speed: speed of the observing runner
    label: string label for the new dist

Returns:
    Pmf object

```python
from code.relay_soln import ObservedPmf
# Example usage:
result = ObservedPmf(...)  # fill in arguments
```
