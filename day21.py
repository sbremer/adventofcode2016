import os
import get_input


def shift_left(seq, n):
    n %= len(seq)
    return seq[n:] + seq[:n]


def shift_right(seq, n):
    n %= len(seq)
    return seq[-n:] + seq[:-n]


day = int(os.path.basename(__file__).replace('day', '').replace('.py', ''))
data = get_input.get_input(day)

password = list('abcdefgh')

lines = data.split('\n')

for line in lines:
    parts = line.split(' ')

    if parts[0] == 'swap':
        if parts[1] == 'position':
            i1 = int(parts[2])
            i2 = int(parts[5])
            password[i1], password[i2] = password[i2], password[i1]
        elif parts[1] == 'letter':
            l1 = parts[2]
            l2 = parts[5]
            i1 = password.index(l1)
            i2 = password.index(l2)
            password[i1], password[i2] = password[i2], password[i1]
    elif parts[0] == 'rotate':
        if parts[1] == 'left':
            password = shift_left(password, int(parts[2]))
        elif parts[1] == 'right':
            password = shift_right(password, int(parts[2]))
        elif parts[1] == 'based':
            i = password.index(parts[6])
            if i < 4:
                r = 1 + i
            else:
                r = 2 + i
            password = shift_right(password, r)
    elif parts[0] == 'reverse':
        i1 = int(parts[2])
        i2 = int(parts[4])+1
        password[i1:i2] = reversed(password[i1:i2])
    elif parts[0] == 'move':
        i1 = int(parts[2])
        i2 = int(parts[5])
        letter = password.pop(i1)
        password.insert(i2, letter)

print('Scrambled password: {}'.format(''.join(password)))

password = list('fbgdceah')

# Magic on paper
reverse_based = [1, 1, 6, 2, 7, 3, 0, 4]

for line in lines[::-1]:
    parts = line.split(' ')

    if parts[0] == 'swap':
        if parts[1] == 'position':
            i1 = int(parts[2])
            i2 = int(parts[5])
            password[i1], password[i2] = password[i2], password[i1]
        elif parts[1] == 'letter':
            l1 = parts[2]
            l2 = parts[5]
            i1 = password.index(l1)
            i2 = password.index(l2)
            password[i1], password[i2] = password[i2], password[i1]
    elif parts[0] == 'rotate':
        if parts[1] == 'left':
            password = shift_right(password, int(parts[2]))
        elif parts[1] == 'right':
            password = shift_left(password, int(parts[2]))
        elif parts[1] == 'based':
            i = password.index(parts[6])
            r = reverse_based[i]
            password = shift_left(password, r)
    elif parts[0] == 'reverse':
        i1 = int(parts[2])
        i2 = int(parts[4])+1
        password[i1:i2] = reversed(password[i1:i2])
    elif parts[0] == 'move':
        i1 = int(parts[2])
        i2 = int(parts[5])
        letter = password.pop(i2)
        password.insert(i1, letter)

print('Decrambled password: {}'.format(''.join(password)))
