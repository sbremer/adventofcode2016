import os
from copy import deepcopy
import get_input


def assem(reg, lines_parts):
    at = 0
    steps = 0

    while at < len(lines_parts):
        steps += 1
        parts = lines_parts[at]

        if parts[0] == 'nop':
            pass
        elif parts[0] == 'inc':
            reg[parts[1]] += 1
        elif parts[0] == 'dec':
            reg[parts[1]] -= 1
        elif parts[0] == 'mtp':
            reg[parts[1]] += reg[parts[2]] * reg[parts[3]]
        elif parts[0] == 'cpy':
            if not parts[2].lstrip('-').isdigit():
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
                if parts[2].lstrip('-').isdigit():
                    jump = int(parts[2])
                else:
                    jump = reg[parts[2]]

                at += jump
                continue
        elif parts[0] == 'tgl':
            tgl_at = reg[parts[1]] + at
            if 0 <= tgl_at < len(lines_parts):
                if lines_parts[tgl_at][0] == 'nop':
                    pass
                elif lines_parts[tgl_at][0] == 'inc':
                    lines_parts[tgl_at][0] = 'dec'
                elif lines_parts[tgl_at][0] == 'tgl' or lines_parts[tgl_at][0] == 'dec':
                    lines_parts[tgl_at][0] = 'inc'
                elif lines_parts[tgl_at][0] == 'cpy':
                    lines_parts[tgl_at][0] = 'jnz'
                elif lines_parts[tgl_at][0] == 'jnz':
                    lines_parts[tgl_at][0] = 'cpy'
                else:
                    print('Error at line {}'.format(' '.join(lines_parts[tgl_at])))
        else:
            print('Error at line {}'.format(' '.join(lines_parts[at])))

        at += 1

    print('Execution in {} steps.'.format(steps))
    return reg


def main():
    day = int(os.path.basename(__file__).replace('day', '').replace('.py', ''))
    data = get_input.get_input(day)

    # Altered data, changed multiplying loops to single command for speedup
    data = """cpy a b
dec b
cpy a d
cpy 0 a
cpy b c
nop #inc a
nop #dec c
nop #jnz c -2
nop #dec d
mtp a c d #jnz d -5
dec b
cpy b c
cpy c d
dec d
inc c
jnz d -2
tgl c
cpy -16 c
jnz 1 c
cpy 78 c
jnz 70 d
nop #inc a
nop #inc d
nop #jnz d -2
nop #inc c
mtp a c d #jnz c -5"""

    lines = data.split('\n')

    lines_parts = []

    for line in lines:
        lines_parts.append(line.split(' '))

    reg = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
    reg = assem(reg, deepcopy(lines_parts))

    print('Value in register a for input 7: {}'.format(reg['a']))

    reg = {'a': 12, 'b': 0, 'c': 0, 'd': 0}
    reg = assem(reg, deepcopy(lines_parts))

    print('Value in register a for input 12: {}'.format(reg['a']))

if __name__ == '__main__':
    main()
