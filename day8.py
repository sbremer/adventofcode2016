import os
import numpy as np
from matplotlib import pyplot as plt
import get_input

day = int(os.path.basename(__file__).replace('day', '').replace('.py', ''))
data = get_input.get_input(day)

lines = data.split('\n')
pixels = np.zeros((50, 6), dtype=np.int32)

for line in lines:
    parts = line.split(' ')

    if parts[0] == 'rect':
        subparts = parts[1].split('x')
        x = int(subparts[0])
        y = int(subparts[1])
        pixels[:x, :y] = 1
    elif parts[0] == 'rotate':
        if parts[1] == 'column':
            x = int(parts[2].replace('x=', ''))
            by = int(parts[4])
            pixels[x, :] = np.roll(pixels[x, :], by)
        elif parts[1] == 'row':
            y = int(parts[2].replace('y=', ''))
            by = int(parts[4])
            pixels[:, y] = np.roll(pixels[:, y], by)
        else:
            print('Error at line {}'.format(line))
    else:
        print('Error at line {}'.format(line))

pixels_on = sum(sum(pixels))
print('On Pixels: {}'.format(pixels_on))

plt.imshow(np.transpose(pixels*255), interpolation='nearest', cmap='gray')
plt.show()
