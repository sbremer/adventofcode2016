data = '10111100110001111'
disc_size = 272
disc_size = 35651584


def generate_data(data_: str):
    data_new = data_[::-1]
    data_new = data_new.replace('1', '_')
    data_new = data_new.replace('0', '1')
    data_new = data_new.replace('_', '0')

    return data_ + '0' + data_new


while len(data) < disc_size:
    data = generate_data(data)

data = data[:disc_size]


def generate_checksum(checksum_):
    checksum_new = ''
    for a, b in zip(checksum_[::2], checksum_[1::2]):
        if a == b:
            checksum_new += '1'
        else:
            checksum_new += '0'
    return checksum_new


checksum = data

while len(checksum) % 2 == 0:
    checksum = generate_checksum(checksum)

print('Checksum: {}'.format(checksum))
