import numpy as np

data = 'L2, L5, L5, R5, L2, L4, R1, R1, L4, R2, R1, L1, L4, R1, L4, L4, R5, R3, R1, L1, R1, L5, L1, R5, L4, R2, L5, L3, L3, R3, L3, R4, R4, L2, L5, R1, R2, L2, L1, R3, R4, L193, R3, L5, R45, L1, R4, R79, L5, L5, R5, R1, L4, R3, R3, L4, R185, L5, L3, L1, R5, L2, R1, R3, R2, L3, L4, L2, R2, L3, L2, L2, L3, L5, R3, R4, L5, R1, R2, L2, R4, R3, L4, L3, L1, R3, R2, R1, R1, L3, R4, L5, R2, R1, R3, L3, L2, L2, R2, R1, R2, R3, L3, L3, R4, L4, R4, R4, R4, L3, L1, L2, R5, R2, R2, R2, L4, L3, L4, R4, L5, L4, R2, L4, L4, R4, R1, R5, L2, L4, L5, L3, L2, L4, L4, R3, L3, L4, R1, L2, R3, L2, R1, R2, R5, L4, L2, L1, L3, R2, R3, L2, L1, L5, L2, L1, R4'

instructions = data.split(', ')

pos = np.zeros(2)

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