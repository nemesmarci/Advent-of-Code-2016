from operator import mul
from functools import reduce

from common import bots_outputs

print(reduce(mul, (bots_outputs()[1][i].inputs.pop()
                   for i in ('0', '1', '2'))))
