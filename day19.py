from collections import deque

n = 3017957

elves = deque([[a, 1] for a in range(n)])

at = 0

for a in range(n-1):
    elf_steals = elves.popleft()
    elf_steal_from = elves.popleft()
    elf_steals[1] += elf_steal_from[1]
    elves.append(elf_steals)

print('Elf {} now has all {} presents.'.format(elves[0][0] + 1, elves[0][1]))

elves_1 = deque([[a, 1] for a in range(int(n/2))])

elves_2 = deque([a, 1] for a in range(int(n/2), n))

for a in range(n-1):
    elf_steals = elves_1.popleft()
    elf_steal_from = elves_2.popleft()
    elf_steals[1] += elf_steal_from[1]
    elves_2.append(elf_steals)
    if a % 2 == 0:
        elves_1.append(elves_2.popleft())

if len(elves_1):
    last_elf = elves_1.pop()
else:
    last_elf = elves_2.pop()

print('Elf {} now has all {} presents (after change of rules).'.format(last_elf[0] + 1, last_elf[1]))


