import os
import get_input

day = int(os.path.basename(__file__).replace('day', '').replace('.py', ''))
data = get_input.get_input(day)

lines = data.split('\n')

at = 0
reg = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

while at < len(lines):
    parts = lines[at].split(' ')

    if parts[0] == 'inc':
        reg[parts[1]] += 1
    elif parts[0] == 'dec':
        reg[parts[1]] -= 1
    elif parts[0] == 'cpy':
        if parts[1].lstrip('-').isdigit():
            reg[parts[2]] = int(parts[1])
        else:
            reg[parts[2]] = reg[parts[1]]
    elif parts[0] == 'jnz':

        if parts[1].lstrip('-').isdigit():
            check = int(parts[1])
        else:
            check = reg[parts[1]]

        if check != 0:
            at += int(parts[2])
            continue
    else:
        print('Error at line {}'.format(lines[at]))

    at += 1

print('Value in register a: {}'.format(reg['a']))

at = 0
reg = {'a': 0, 'b': 0, 'c': 1, 'd': 0}

while at < len(lines):
    parts = lines[at].split(' ')

    if parts[0] == 'inc':
        reg[parts[1]] += 1
    elif parts[0] == 'dec':
        reg[parts[1]] -= 1
    elif parts[0] == 'cpy':
        if parts[1].lstrip('-').isdigit():
            reg[parts[2]] = int(parts[1])
        else:
            reg[parts[2]] = reg[parts[1]]
    elif parts[0] == 'jnz':

        if parts[1].lstrip('-').isdigit():
            check = int(parts[1])
        else:
            check = reg[parts[1]]

        if check != 0:
            at += int(parts[2])
            continue
    else:
        print('Error at line {}'.format(lines[at]))

    at += 1

print('Value in register a when c starts at 1: {}'.format(reg['a']))

