import os
import numpy as np
from itertools import combinations, permutations
from collections import namedtuple

import get_input


class Map(list):
    State = namedtuple('State', ['pos', 'performance'])

    def __init__(self, data):
        data = data.split('\n')
        self.scan = len(data[0])
        super().__init__(''.join(data))

    def get_coord(self, pos):
        x = pos % self.scan
        y = int(pos / self.scan)
        return x, y

    def get_dist(self, pos_a, pos_b):
        xa, ya = self.get_coord(pos_a)
        xb, yb = self.get_coord(pos_b)
        return abs(xa-xb) + abs(ya-yb)

    def get_steps(self, pos_start, pos_end):

        moves = [1, -1, self.scan, -self.scan]

        steps = [1e10] * len(self)
        states = [Map.State(pos_start, 0 + self.get_dist(pos_start, pos_end))]
        steps[pos_start] = 0

        def get_states_new(state_):
            states_new = []
            for move in moves:
                pos_new = state_.pos + move
                if self[pos_new] != '#' and steps[pos_new] > steps[state_.pos] + 1:
                    state_new = Map.State(pos_new, steps[state_.pos] + 1 + self.get_dist(pos_new, pos_end))
                    steps[pos_new] = steps[state_.pos] + 1
                    states_new.append(state_new)
            return states_new

        while True:
            # Get best state
            performance_best = 1e10
            i_best = -1
            for i, state in enumerate(states):
                if state.performance < performance_best:
                    performance_best = state.performance
                    i_best = i

            state_best = states[i_best]
            del states[i_best]

            if state_best.pos == pos_end:
                return steps[pos_end]

            states.extend(get_states_new(state_best))


def main():
    day = int(os.path.basename(__file__).replace('day', '').replace('.py', ''))
    data = get_input.get_input(day)

    hvac_map = Map(data)

    poi = {}

    for i, c in enumerate(hvac_map):
        if c.isdigit():
            poi[int(c)] = i

    n_poi = len(poi)

    dists = np.zeros((n_poi, n_poi), dtype=np.int32)

    for a, b in combinations(range(n_poi), 2):
        pos_a = poi[a]
        pos_b = poi[b]
        steps = hvac_map.get_steps(pos_a, pos_b)
        dists[a, b] = dists[b, a] = steps

    # Part 1: Random end position
    total_dist_min = 1e10
    for order in permutations(range(1, n_poi)):
        order = [0] + list(order)
        total_dist = 0
        for i in range(1, len(order)):
            total_dist += dists[order[i-1], order[i]]

        if total_dist < total_dist_min:
            total_dist_min = total_dist

    print('Minimum steps to visit all important places starting at 0: {}'.format(total_dist_min))

    # Part 2: Back to position 0
    total_dist_min = 1e10
    for order in permutations(range(1, n_poi)):
        order = [0] + list(order) + [0]
        total_dist = 0
        for i in range(1, len(order)):
            total_dist += dists[order[i-1], order[i]]

        if total_dist < total_dist_min:
            total_dist_min = total_dist

    print('Minimum steps to visit all important places starting at 0 and back to 0: {}'.format(total_dist_min))

if __name__ == '__main__':
    main()
