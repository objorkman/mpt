import os
from timeit import default_timer as timer
import math

def percentile(data, perc):
    size = len(data)
    return sorted(data)[int(math.ceil((size * perc) / 100)) - 1]

diffs = []
threads = 32
for i in range(50):
    start = timer()
    os.system('OMP_NUM_THREADS=' + str(threads) + ' build/Release/nao_cup_planning-KDTreeBatch-double-mt -S')
    end = timer()
    diffs.append(end - start) 

print('Mean: ', sum(diffs) / len(diffs))
print('25%: ', percentile(diffs, 25))
print('50%: ', percentile(diffs, 50))
print('75%: ', percentile(diffs, 75))
print('90%: ', percentile(diffs, 90))
print('95%: ', percentile(diffs, 95))
print('99%: ', percentile(diffs, 99))
