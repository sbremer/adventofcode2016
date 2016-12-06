import os
from collections import Counter
import get_input

day = int(os.path.basename(__file__).replace('day', '').replace('.py', ''))
data = get_input.get_input(day)

lines = data.split('\n')

char_counter = [[] for i in range(len(lines[0]))]

for line in lines:
    for i, char in enumerate(line):
        char_counter[i].append(char)

message_most_common = []
message_least_common = []

for char_list in char_counter:
    counter = Counter(char_list)

    char_occurances = counter.most_common()
    (char_most_common, _) = char_occurances[0]
    message_most_common.append(char_most_common)
    (char_least_common, _) = char_occurances[-1]
    message_least_common.append(char_least_common)


print('Decorrupted message (most common): {}'.format(''.join(message_most_common)))
print('Decorrupted message (least common): {}'.format(''.join(message_least_common)))
