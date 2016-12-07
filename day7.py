import os
import get_input


def check_abba(part):

    # Assuming even number of chars

    # Check abba at even positions
    prev_char1, prev_char2 = '_', '_'
    for char1, char2 in zip(part[::2], part[1::2]):

        if char1 == prev_char2 and char2 == prev_char1 and char1 != char2:
            return True

        prev_char1, prev_char2 = char1, char2

    # Check shifted at odd positions
    prev_char1, prev_char2 = '_', '_'
    for char1, char2 in zip(part[1::2], part[2::2]):

        if char1 == prev_char2 and char2 == prev_char1 and char1 != char2:
            return True

        prev_char1, prev_char2 = char1, char2

    return False


def check_address_abba(address):
    abba_out_brackets = False
    parts = address.split(']')

    for part in parts:
        sub = part.split('[')

        if len(sub) == 2 and check_abba(sub[1]):
            return False

        if check_abba(sub[0]):
            abba_out_brackets = True

    if abba_out_brackets:
        return True
    else:
        return False


def find_aba_bab(part):
    aba = []
    prev_char1, prev_char2 = '_', '_'

    for char in part:
        if char == prev_char2 and char != prev_char1:
            aba.append((char, prev_char1))

        prev_char1, prev_char2 = char, prev_char1

    return aba


def check_address_aba_bab(address):
    parts = address.split(']')

    aba = set()
    bab = set()

    for part in parts:
        sub = part.split('[')

        if len(sub) == 2:
            bab.update(find_aba_bab(sub[1]))

        aba.update(find_aba_bab(sub[0]))

    for (i, o) in aba:
        if (o, i) in bab:
            return True

    return False

day = int(os.path.basename(__file__).replace('day', '').replace('.py', ''))
data = get_input.get_input(day)

lines = data.split('\n')

abba = 0
aba_bab = 0

for line in lines:
    if check_address_abba(line):
        abba += 1

    if check_address_aba_bab(line):
        aba_bab += 1

print('IPs found with TLS support: {}'.format(abba))
print('IPs found with SSL support: {}'.format(aba_bab))
