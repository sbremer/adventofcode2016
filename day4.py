import os
from collections import Counter, OrderedDict
import itertools
import get_input

def decrypt(name, shift):
    decrypted = []

    for char in name:
        if char == ' ':
            decrypted.append(char)
            continue

        decrypted_char = chr(((ord(char) - ord('a')) + shift) % 26 + ord('a'))
        decrypted.append(decrypted_char)

    return ''.join(decrypted)


day = int(os.path.basename(__file__).replace('day', '').replace('.py', ''))
data = get_input.get_input(day)

lines = data.split('\n')

sum_sectorIDs = 0

for line in lines:
    pieces = line.split('-')

    meta = pieces[-1].split('[')
    checksum = meta[1].replace(']', '')
    sectorID = int(meta[0])

    char_list = list(itertools.chain.from_iterable(pieces[:-1:]))
    counted = dict(Counter(char_list))
    counted_sorted = OrderedDict(sorted(counted.items(), key=lambda t: (-t[1], ord(t[0]))))

    checksum_computed = ''.join([item[0] for item in list(counted_sorted.items())[:5:]])

    if checksum == checksum_computed:
        sum_sectorIDs += sectorID
        room_name = ' '.join(pieces[:-1:])
        decrypted_room_name = decrypt(room_name, sectorID % 26)
        if decrypted_room_name == 'northpole object storage':
            print('SectorID of "northpole object storage": {}'.format(sectorID))

print('Sum of sectorIDs of valid rooms: {}'.format(sum_sectorIDs))
