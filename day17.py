from hashlib import md5
from collections import namedtuple
from itertools import count
import numpy as np


def valid_pos(at):
    if at[0] < 0 or at[1] < 0 or at[0] >= 4 or at[1] >= 4:
        return False
    else:
        return True


salt = b'pxxbnzuo'

move_possible = list('bcdef')

State = namedtuple('State', ['at', 'steps_char_history'])

start = np.array([0, 0])
goal = np.array([3, 3])

states = [State(start, b'')]

steps = [np.array([0, -1]), np.array([0, 1]), np.array([-1, 0]), np.array([1, 0])]
steps_char = [b'U', b'D', b'L', b'R']

found_after = []

for a in count():
    states_new = []

    for state in states:
        hash_ = md5((salt+state.steps_char_history)).hexdigest()[:4]

        for step, step_char, hash_char in zip(steps, steps_char, hash_):

            if hash_char not in move_possible:
                continue

            at_new = state.at + step

            if not valid_pos(at_new):
                continue

            steps_char_history_new = state.steps_char_history + step_char

            if at_new[0] == goal[0] and at_new[1] == goal[1]:
                if len(found_after) == 0:
                    print('Fastest way to goal: {}'.format(steps_char_history_new))

                found_after.append(len(steps_char_history_new))
                continue

            state_new = State(at_new, steps_char_history_new)
            states_new.append(state_new)

    # print('States after {} steps: {}'.format(a, len(states_new)))

    if len(states_new) == 0:
        break
    states = states_new

print('Longest path: {}'.format(found_after[-1]))
