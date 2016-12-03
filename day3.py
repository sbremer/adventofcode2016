import os
import get_input

day = int(os.path.basename(__file__).replace('day', '').replace('.py', ''))
data = get_input.get_input(day)

lines = data.split('\n')

valid = 0

for line in lines:
    sides = list(map(int,filter(None, line.split(' '))))
    sides = sorted(sides)
    if sides[0] + sides[1] > sides[2]:
        valid += 1

print('Valid triangles: {}'.format(valid))

valid = 0

for line1, line2, line3 in zip(lines[0::3], lines[1::3], lines[2::3]):
    l1 = list(map(int, filter(None, line1.split(' '))))
    l2 = list(map(int, filter(None, line2.split(' '))))
    l3 = list(map(int, filter(None, line3.split(' '))))

    triangles = []

    for a in range(3):
        sides = [l1[a], l2[a], l3[a]]
        triangles.append(sides)

    for sides in triangles:
        sides = sorted(sides)
        if sides[0] + sides[1] > sides[2]:
            valid += 1

print('Valid triangles (vertical): {}'.format(valid))