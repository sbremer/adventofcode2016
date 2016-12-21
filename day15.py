import os
from collections import namedtuple
from itertools import count
import get_input

Disc = namedtuple('Disc', ['size', 'start'])

day = int(os.path.basename(__file__).replace('day', '').replace('.py', ''))
data = get_input.get_input(day)

lines = data.split('\n')

discs = []

for line in lines:
    parts = line.split(' ')
    # Disc #1 has 5 positions; at time=0, it is at position 2.
    size = int(parts[3])
    start = int(parts[11].replace('.', ''))
    disc = Disc(size, start)
    discs.append(disc)


def check(at):
    for offset, disc in enumerate(discs):
        if (at + disc.start + offset + 1) % disc.size != 0:
            return False

    return True


for at in count():
    if check(at):
        break

print('First time to successfully drop a capsule: {}'.format(at))

disc_new = Disc(11, 0)
discs.append(disc_new)

for at in count():
    if check(at):
        break

print('First time to successfully drop a capsule after new disc: {}'.format(at))
