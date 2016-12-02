import os
import numpy as np
import get_input

day = int(os.path.basename(__file__).replace('day', '').replace('.py', ''))
data = get_input.get_input(day)

instructions = data.split(', ')

pos = np.zeros(2, dtype=np.int32)

north = np.array([0, 1])
east = np.array([1, 0])
south = np.array([0, -1])
west = np.array([-1, 0])

directions = [north, east, south, west]

current_direction = 0

pos_counter = {}

found = False

for instruction in instructions:
    if instruction[0] == 'L':
        current_direction = (current_direction - 1) % 4
    elif instruction[0] == 'R':
        current_direction = (current_direction + 1) % 4
    else:
        print('ERROR')

    walk = int(instruction[1:])

    for a in range(walk):
        pos += directions[current_direction]

        key = '{},{}'.format(pos[0], pos[1])

        if key not in pos_counter.keys():
            pos_counter[key] = 0

        pos_counter[key] += 1

        if pos_counter[key] == 2 and not found:
            distance = abs(pos[0]) + abs(pos[1])
            print('Total Manhatten distance of first location visited twice: {}'.format(distance))
            found = True



distance = abs(pos[0]) + abs(pos[1])
print('Total Manhatten distance: {}'.format(distance))
