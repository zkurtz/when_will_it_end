# When will it end

This consists of a single class `LoopProgressMonitor` that you instantiate right before a loop
and then call inside the loop. It monitors how long each iteration is taking and issues a forecast of when
the loop will conclude based on the number of iterations remaining and the average time per iteration so far.
It prints a new predicted end time only when the most recent forecast falls too far from its internal estimate 
modulo some tolerance.

## Requirements

Python 3 with the following modules: `datetime`, `time`

## Setup

- Clone this repository
- `cd when_will_it_end`
- `python setup.py install`

## Example

```python
import numpy as np
import time
import when_will_it_end as wwie

number_of_iterations = 10

print('Starting time: ' + wwie.format_time(time.time()))

lpm = wwie.LoopProgressMonitor(n = number_of_iterations)
for k in range(number_of_iterations):
    lpm()
    _ = np.random.uniform(0,1,size=100000000)

print('Actual ending time: ' + wwie.format_time(time.time()))
```

Results:

```
Starting time: 12:14:44
Starting first of 10 iterations ...
Est. finish 12:15:01 after 9 iters at 1.7 sec/iter
Est. finish 12:15:03 after 5 iters at 1.8 sec/iter
Actual ending time: 12:15:03
```
