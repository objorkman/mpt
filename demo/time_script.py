import os
import csv
from timeit import default_timer as timer
import math

def percentile(data, perc):
    size = len(data)
    return sorted(data)[int(math.ceil((size * perc) / 100)) - 1]

result= []
data = []
threads = [1, 2, 4, 8, 16, 32, 48]
percents = [25, 50, 75, 95, 99]

for t in threads:
    times = []
    for i in range(50):
        start = timer()
        os.system('OMP_NUM_THREADS=' + str(t) + ' build/Release/se3_rigid_body_planning-GNAT-double-mt -S /omplapp/resources/3D/Twistycool.cfg')
        end = timer()
        times.append(end - start) 
    
    result.append([sum(times) / len(times)] + [percentile(times, p) for p in percents])
    
    data.append(times)

with open('result.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['mean'] + [str(p) for p in percents])
    writer.writerows(result)

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerows(data)