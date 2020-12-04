from collections import Counter, defaultdict


def solve(least_common=False):
    columns = defaultdict(Counter)
    with open('input.txt') as data:
        for line in map(str.strip, data):
            for i, c in enumerate(line):
                columns[i][c] += 1
    return(''.join(column.most_common()[-1 if least_common else 0][0]
           for column in columns.values()))
