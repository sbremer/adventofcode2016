import os
import get_input

day = int(os.path.basename(__file__).replace('day', '').replace('.py', ''))
data = get_input.get_input(day)

lines = data.split('\n')

# Filesystem              Size  Used  Avail  Use%
# /dev/grid/node-x0-y0     88T   67T    21T   76%

nodes = {}

x_max = -1
y_max = -1

for line in lines[2:]:
    parts = [x for x in line.split(' ') if x]
    subparts = parts[0].split('-')
    x = int(subparts[1].replace('x', ''))
    y = int(subparts[2].replace('y', ''))

    if y > y_max:
        y_max = y
    if x > x_max:
        x_max = x

    used = int(parts[2].replace('T', ''))
    avail = int(parts[3].replace('T', ''))

    nodes[(x,y)] = (used, avail)

viable_pairs = []

for a in nodes.keys():
    for b in nodes.keys():
        if a == b:
            continue

        if 0 < nodes[a][0] <= nodes[b][1]:
            viable_pairs.append((a, b))

print('Viable pairs: {}'.format(len(viable_pairs)))

for y in range(y_max+1):
    for x in range(x_max+1):
        if nodes[(x,y)][0] == 0:
            print('_', end='')
        elif nodes[(x,y)][0] < 100:
            print('.', end='')
        else:
            print('#', end='')

    print('')

# 225
