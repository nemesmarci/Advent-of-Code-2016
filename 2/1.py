from common import solve


def up(pos):
    return pos if pos in (1, 2, 3) else pos - 3


def down(pos):
    return pos if pos in (7, 8, 9) else pos + 3


def left(pos):
    return pos if pos in (1, 4, 7) else pos - 1


def right(pos):
    return pos if pos in (3, 6, 9) else pos + 1


print(solve(up, down, left, right))
