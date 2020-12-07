from common import bots_outputs

print(next(i for i, bot in bots_outputs()[0].items()
           if bot.inputs == {17, 61}))
