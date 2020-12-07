import re
from collections import defaultdict

INPUT_REGEX = re.compile(r'value (\d+) goes to bot (\d+)')
BOT_REGEX = re.compile(
    r'bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)')


class Bot:
    def __init__(self):
        self.inputs = set()
        self.low = None
        self.high = None


class Output:
    def __init__(self):
        self.inputs = set()


def bots_outputs():
    bots = defaultdict(Bot)
    outputs = defaultdict(Output)
    with open('input.txt') as data:
        for line in data:
            if input_match := re.match(INPUT_REGEX, line):
                value, bot_id = input_match.groups()
                bots[bot_id].inputs.add(int(value))
            elif bot_match := re.match(BOT_REGEX, line):
                bot_id, out1_type, out1_id, out2_type, out2_id = \
                    bot_match.groups()
                bots[bot_id].low = bots[out1_id] if out1_type == 'bot' \
                    else outputs[out1_id]
                bots[bot_id].high = bots[out2_id] if out2_type == 'bot' \
                    else outputs[out2_id]

    while any(len(bot.inputs) != 2 for bot in bots.values()):
        for bot in (bot for bot in bots.values() if len(bot.inputs) == 2):
            if len(bot.low.inputs) != 2:
                bot.low.inputs.add(min(bot.inputs))
            if len(bot.high.inputs) != 2:
                bot.high.inputs.add(max(bot.inputs))

    return bots, outputs
