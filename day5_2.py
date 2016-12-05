import itertools
import hashlib

data = 'uqwqemis'

key = ['_', ] * 8

for a in itertools.count():
    to_hash = (data + str(a)).encode('ascii')
    hashed = hashlib.md5(to_hash).hexdigest()
    if hashed[:5:] == '00000':
        position = hashed[5]
        keydigit = hashed[6]
        if ord(position) >= ord('0') and ord(position) <= ord('7'):
            position = int(position)
            if key[position] == '_':
                key[position] = keydigit
                print('Found key digit at {}: {} at position {}'.format(a, keydigit, position))
                print('Current key: {}'.format(''.join(key)))

                if '_' not in key:
                    break


print('Found key: {}'.format(''.join(key)))
