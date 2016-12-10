import os
import get_input

day = int(os.path.basename(__file__).replace('day', '').replace('.py', ''))
data = get_input.get_input(day)

lines = data.split('\n')

bots_gets = {}
bot_gives_low = {}
bot_gives_high = {}

for line in lines:
    parts = line.split(' ')

    if parts[0] == 'bot':
        bot = int(parts[1])

        if parts[5] == 'bot':
            bot_gives_low[bot] = (True, int(parts[6]))
        elif parts[5] == 'output':
            bot_gives_low[bot] = (False, int(parts[6]))
        else:
            print('Error in line: {}'.format(line))

        if parts[10] == 'bot':
            bot_gives_high[bot] = (True, int(parts[11]))
        elif parts[10] == 'output':
            bot_gives_high[bot] = (False, int(parts[11]))
        else:
            print('Error in line: {}'.format(line))
    elif parts[0] == 'value':
        bot = int(parts[5])
        chip = int(parts[1])

        if bot not in bots_gets.keys():
            bots_gets[bot] = []

        bots_gets[bot].append(chip)
    else:
        print('Error in line: {}'.format(line))

n_bots = len(bot_gives_low)
bots_done = set()
output_gets = {}

while len(bots_done) < n_bots:
    bots_todo = set()

    for bot in bots_gets.keys():

        if bot not in bots_done and len(bots_gets[bot]) == 2:
            bots_todo.add(bot)

    for bot in bots_todo:
        lower = min(bots_gets[bot])
        higher = max(bots_gets[bot])

        # Lower
        if bot_gives_low[bot][0]:
            bot_chip_to = bot_gives_low[bot][1]

            if bot_chip_to not in bots_gets.keys():
                bots_gets[bot_chip_to] = []

            bots_gets[bot_chip_to].append(lower)
        else:
            output_chip_to = bot_gives_low[bot][1]

            if output_chip_to not in output_gets.keys():
                output_gets[output_chip_to] = []

            output_gets[output_chip_to].append(lower)

        # Higher
        if bot_gives_high[bot][0]:
            bot_chip_to = bot_gives_high[bot][1]

            if bot_chip_to not in bots_gets.keys():
                bots_gets[bot_chip_to] = []

            bots_gets[bot_chip_to].append(higher)
        else:
            output_chip_to = bot_gives_high[bot][1]

            if output_chip_to not in output_gets.keys():
                output_gets[output_chip_to] = []

            output_gets[output_chip_to].append(higher)

    bots_done = bots_done | bots_todo

for bot in bots_gets.keys():
    if 17 in bots_gets[bot] and 61 in bots_gets[bot]:
        print('Bot {} gets 17 and 61!'.format(bot))

multiply = 1
for a in range(3):
    multiply *= output_gets[a][0]

print('Product of output [0,1,2]: {}'.format(multiply))



