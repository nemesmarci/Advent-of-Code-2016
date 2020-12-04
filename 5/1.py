from common import find_hash

hasher = find_hash()
print(''.join(next(hasher)[5] for i in range(8)))
