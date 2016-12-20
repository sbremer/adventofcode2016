import numpy as np
from collections import namedtuple
fav_number = 1352

State = namedtuple('State', ['at', 'steps', 'dist'])


def is_wall(x, y):
    i = x*x + 3*x + 2*x*y + y + y*y + fav_number
    bits = str(bin(i))[2:]
    return (bits.count('1') % 2) == 1


def generate_map(size_x, size_y):
    wall_map = np.zeros((size_x, size_y))

    for x in range(size_x):
        for y in range(size_y):
            if is_wall(x, y):
                wall_map[x, y] = -1

    return wall_map


def valid_pos(at, map_size):
    if at[0] < 0 or at[1] < 0 or at[0] >= map_size[0] or at[1] >= map_size[1]:
        return False
    else:
        return True


def get_dist(v):
    return np.linalg.norm(v, ord=1)


if __name__ == '__main__':
    start = np.array([1, 1])
    target = np.array([31, 39])

    map_size = target + 25

    steps = [np.array([0, 1]), np.array([0, -1]), np.array([1, 0]), np.array([-1, 0])]

    wall_map = generate_map(map_size[0], map_size[1])

    states = [State(start, 0, get_dist(target-start))]

    while True:
        dist_min = np.sum(map_size)
        i_min = -1

        # Get best current location
        for i, state in enumerate(states):
            if state.dist < dist_min:
                dist_min = state.dist
                i_min = i

        state = states[i_min]
        del states[i_min]
        wall_map[state.at[0], state.at[1]] = 1

        if dist_min == 0:
            break

        # Generate new steps
        states_new = []

        for step in steps:
            new_pos = state.at + step

            if not valid_pos(new_pos, map_size) or wall_map[new_pos[0], new_pos[1]] != 0:
                continue

            new_state = State(new_pos, state.steps + 1, get_dist(target-new_pos))
            states_new.append(new_state)

        states.extend(states_new)

    print('Minimum distance to target: {}'.format(state.steps))

    # Reset map
    wall_map = generate_map(map_size[0], map_size[1])

    positions = [start]
    wall_map[start[0], start[1]] = 1
    total_fields = 1

    for a in range(50):

        positions_new = []

        for position in positions:

            for step in steps:
                position_new = position + step

                if not valid_pos(position_new, map_size) or wall_map[position_new[0], position_new[1]] != 0:
                    continue

                wall_map[position_new[0], position_new[1]] = 1
                positions_new.append(position_new)
                total_fields += 1

        positions = positions_new

    print('Total positions accessible in 50 steps: {}'.format(total_fields))







