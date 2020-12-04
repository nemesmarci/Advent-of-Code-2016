from hashlib import md5
from itertools import count


def find_hash():
    with open('input.txt') as data:
        base = data.read().strip()
    for i in count():
        hashed = md5((base + str(i)).encode('utf-8')).hexdigest()
        if hashed.startswith('00000'):
            yield hashed
