import os
import get_input

day = int(os.path.basename(__file__).replace('day', '').replace('.py', ''))
data = get_input.get_input(day)

ranges = []

lines = data.split('\n')

for line in lines:
    parts = line.split('-')
    ranges.append((int(parts[0]), int(parts[1])))


ranges = sorted(ranges, key=lambda x: x[0])
ranges_new = []


low = ranges[0][0]
high = ranges[0][1]

for r in ranges[1:]:
    if r[0] <= high + 1:
        high = max(high, r[1])
    else:
        ranges_new.append((low, high))
        low = r[0]
        high = r[1]

ranges_new.append((low, high))

lowest = ranges_new[0][1] + 1

print('Lowest not blocked address: {}'.format(lowest))

unblocked = ranges_new[0][0]

for i in range(len(ranges_new)-1):
    unblocked += ranges_new[i+1][0] - ranges_new[i][1] - 1

unblocked += 4294967295 - ranges_new[-1][1]

print('Total number of unblocked addresses: {}'.format(unblocked))
