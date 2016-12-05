import itertools
import hashlib

data = 'uqwqemis'

key = ''

for a in itertools.count():
    to_hash = (data + str(a)).encode('ascii')
    hashed = hashlib.md5(to_hash).hexdigest()
    if hashed[:5:] == '00000':
        keydigit = hashed[5]
        key += keydigit
        print('Found key digit at {}: {}'.format(a, keydigit))

        if len(key) == 8:
            break

print('Found key: {}'.format(key))
