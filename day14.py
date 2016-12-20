from hashlib import md5
from itertools import count
import re

salt = 'jlmsuwbz'
# salt = 'abc'

hashes = []
hashes_matches5 = []

match3 = re.compile(r'(.)\1{2,}')

partone = False


def generate(i):
    if partone:
        return md5((salt + str(i)).encode('ascii')).hexdigest()
    else:
        s = (salt + str(i))
        for _ in range(2017):
            s = md5(s.encode('ascii')).hexdigest()
        return s

def generate_till(i):
    while len(hashes) <= i:
        hash_ = generate(len(hashes))
        hashes.append(hash_)


def get_hash(i):
    if i + 1000 >= len(hashes):
        generate_till(i + 1000)

    return hashes[i]


def find_match5(at, char):
    match5 = re.compile('{}{{5,}}'.format(char))
    for a in range(1, 1001):
        if match5.search(hashes[at+a]):
            return True

    return False


def main():
    keys = []
    at = 0

    for at in count():
        hash_ = get_hash(at)

        match = match3.search(hash_)
        if match and find_match5(at, match.group(0)[0]):
            keys.append(hash_)
            print('Found key {} at {}'.format(len(keys), at))
            if len(keys) == 64:
                break

    print('Index of 64th key: {}'.format(at))




if __name__ == '__main__':
    main()