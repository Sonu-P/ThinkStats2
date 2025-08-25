## Module `code.chap14soln`

This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

### Import

```python
from code.chap14soln import *  # or import specific names
```

### Functions

- `GenerateAdultWeight(birth_weights, n)`

Generate a random adult weight by simulating annual gain.

birth_weights: sequence of birth weights in lbs
n: number of years to simulate

returns: adult weight in lbs

```python
from code.chap14soln import GenerateAdultWeight
# Example usage:
result = GenerateAdultWeight(...)  # fill in arguments
```

- `main()`
```python
from code.chap14soln import main
# Example usage:
result = main(...)  # fill in arguments
```

- `PlotAdultWeights(live)`

Makes a normal probability plot of log10 adult weight.

live: DataFrame of live births

results: 

With n=40 the distribution is approximately lognormal except for
the lowest weights.

Actual distribution might deviate from lognormal because it is
a mixture of people at different ages, or because annual weight
gains are correlated.

```python
from code.chap14soln import PlotAdultWeights
# Example usage:
result = PlotAdultWeights(...)  # fill in arguments
```

- `PlotPregLengths(live, firsts, others)`

Plots sampling distributions under the null and alternate hypotheses.

live, firsts, others: DataFrames

Results:  
null hypothesis N(0, 0.00319708)
0.0837707042554 0.0837707042554     (90% CI)

estimated params N(0.0780373, 0.00321144)
-0.0151758158699 0.171250349425     (90% CI)

Sampling distribution under the null hypothesis is centered
around 0.

Sampling distribution under the null hypothesis is centered
around the observed difference, 0.078.

The variance of the two distributions is very similar; in practice,
you could reasonably compute whichever one is easier.

```python
from code.chap14soln import PlotPregLengths
# Example usage:
result = PlotPregLengths(...)  # fill in arguments
```

- `TestIntervention()`

Tests whether reported changes are statistically significant.

Results:
-1.66 4.73095323208e-05
-0.26 0.125267987207
 1.4 0.00182694836898

Conclusions:

1) Gender gap before intervention was 1.66 points (p-value 5e-5)

2) Genger gap after was 0.26 points (p-value 0.13, no significant)

3) Change in gender gap was 1.4 points (p-value 0.002, significant).

```python
from code.chap14soln import TestIntervention
# Example usage:
result = TestIntervention(...)  # fill in arguments
```
