
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