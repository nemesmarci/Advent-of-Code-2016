from common import valid

with open('input.txt') as data:
    lines = [list(map(int, line.split())) for line in data]
    print(sum(valid(lines[i][col], lines[i + 1][col], lines[i + 2][col])
              for col in range(3) for i in range(0, len(lines), 3)))
