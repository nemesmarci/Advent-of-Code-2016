from common import valid

with open('input.txt') as data:
    print(sum(valid(*map(int, line.split())) for line in data))
