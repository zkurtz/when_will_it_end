# When will it end

This model essentially consists of a single class `LoopProgressMonitor` that you instantiate right before a loop
and then call inside the loop. It monitors how long each iteration is taking and issues a forecast of when
the loop will conclude based on the number of iterations remaining and the average time per iteration so far.
It prints a new predicted end time only when the most recent forecast falls too far from its internal estimate 
modulo some tolerance.

# Example

Coming soon ... 