import os
import csv
from timeit import default_timer as timer
import math
from docker import Client

def percentile(data, perc):
    size = len(data)
    return sorted(data)[int(math.ceil((size * perc) / 100)) - 1]

result= []
data = []
threads = [1, 2, 4, 8, 16, 32, 48]
percents = [25, 50, 75, 95, 99]

cli = Client(base_url='unix://var/run/docker.sock')
HOSTNAME = os.environ.get("HOSTNAME")
all_containers = cli.containers()
our_container = [c for c in all_containers if c['Id'][:12] == HOSTNAME[:12]][0]

container_num = our_container['Labels']['com.docker.compose.container-number']

for t in threads:
    times = []
    for i in range(2):
        start = timer()
        os.system('OMP_NUM_THREADS=' + str(t) + ' build/Release/se3_rigid_body_planning-GNAT-double-mt -S /omplapp/resources/3D/Twistycool.cfg')
        end = timer()
        times.append(end - start)

    result.append([sum(times) / len(times)] + [percentile(times, p) for p in percents])

    data.append(times)

with open('../../data/result_' + container_num + '.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['mean'] + [str(p) for p in percents])
    writer.writerows(result)

with open('../../data/data_' + container_num + '.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerows(data)

