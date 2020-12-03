from common import solve


def up(pos):
    return pos if pos in (5, 2, 1, 4, 9) else \
           pos - 2 if pos in (3, 13) else \
           pos - 4


def down(pos):
    return pos if pos in (5, 10, 13, 12, 9) else \
           pos + 2 if pos in (1, 11) else \
           pos + 4


def left(pos):
    return pos if pos in (1, 2, 5, 10, 13) else pos - 1


def right(pos):
    return pos if pos in (1, 4, 9, 12, 13) else pos + 1


print(solve(up, down, left, right))
