import os
import get_input

day = int(os.path.basename(__file__).replace('day', '').replace('.py', ''))
data = get_input.get_input(day)

lines = data.split('\n')

# y, x
pos = [1, 1]

# o-> x
# |
# v
# y

# Keypad
keypad = [list('123'),
          list('456'),
          list('789')]

# keypad[y][x]

combination = []


for line in lines:
    for char in line:
        if char == 'U':
            pos[0] = max(0, pos[0] - 1)
        elif char == 'D':
            pos[0] = min(2, pos[0] + 1)
        elif char == 'L':
            pos[1] = max(0, pos[1] - 1)
        elif char == 'R':
            pos[1] = min(2, pos[1] + 1)
        else:
            print('ERROR')

    combination.append(keypad[pos[0]][pos[1]])

print('Combination: {}'.format(''.join(combination)))

#     1
#   2 3 4
# 5 6 7 8 9
#   A B C
#     D

combination = []
keypad = [list('__1__'),
          list('_234_'),
          list('56789'),
          list('_ABC_'),
          list('__D__')]

pos = [2, 0]

for line in lines:
    for char in line:

        old_pos = pos.copy()

        if char == 'U':
            pos[0] = max(0, pos[0] - 1)
        elif char == 'D':
            pos[0] = min(4, pos[0] + 1)
        elif char == 'L':
            pos[1] = max(0, pos[1] - 1)
        elif char == 'R':
            pos[1] = min(4, pos[1] + 1)
        else:
            print('ERROR')

        if keypad[pos[0]][pos[1]] == '_':
            pos = old_pos

    combination.append(keypad[pos[0]][pos[1]])

print('Actual Combination: {}'.format(''.join(combination)))
