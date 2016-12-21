import os
import get_input

day = int(os.path.basename(__file__).replace('day', '').replace('.py', ''))
data = get_input.get_input(day)

rows = 40
rows = 400000
cols = len(data)

safe_tiles = data.count('.')
row = '.' + data + '.'

for r in range(1, rows):
    row_new = '.'

    for c in range(1, cols+1):
        if row[c-1] != row[c+1]:
            row_new += '^'
        else:
            row_new += '.'
            safe_tiles += 1

    row_new += '.'
    row = row_new

print('Safe tiles: {}'.format(safe_tiles))
