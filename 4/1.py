from operator import itemgetter
from collections import Counter

from common import parse


def real(line):
    encrypted, sector, checksum = parse(line)
    letters = Counter(encrypted)
    del letters['-']
    return int(sector) if [letter[0] for letter in sorted(
        sorted(letters.items(), key=itemgetter(0)),
        key=itemgetter(1), reverse=True)[:5]] == list(checksum) else 0


with open('input.txt') as data:
    print(sum(real(line) for line in data))
