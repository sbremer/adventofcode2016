import os
import re
import get_input

search_term = re.compile('\(\d+x\d+\)')


def get_len_compression(compressed):
    start = 0
    uncompressed_len = 0

    marker_match = re.search(search_term, compressed[start:])
    while marker_match is not None:
        marker_info = marker_match.group().lstrip('(').rstrip(')').split('x')
        m_len, m_rep = map(int, marker_info)
        m_start, m_end = marker_match.span()

        uncompressed_len += m_start + m_len * m_rep

        start += m_end + m_len
        marker_match = re.search(search_term, compressed[start:])

    uncompressed_len += len(compressed) - start
    return uncompressed_len


def get_len_compression2(compressed):
    start = 0
    uncompressed_len = 0

    marker_match = re.search(search_term, compressed[start:])
    while marker_match is not None:
        marker_info = marker_match.group().lstrip('(').rstrip(')').split('x')
        m_len, m_rep = map(int, marker_info)
        m_start, m_end = marker_match.span()

        uncompressed_len += m_start + get_len_compression2(compressed[start + m_end:start + m_end + m_len]) * m_rep

        start += m_end + m_len
        marker_match = re.search(search_term, compressed[start:])

    uncompressed_len += len(compressed) - start
    return uncompressed_len

day = int(os.path.basename(__file__).replace('day', '').replace('.py', ''))
data = get_input.get_input(day)

output_len_1 = get_len_compression(data)
output_len_2 = get_len_compression2(data)

print('Decompressed length: {}'.format(output_len_1))
print('Decompressed length using compression v2: {}'.format(output_len_2))
