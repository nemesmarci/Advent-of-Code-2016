import re
import numpy as np

X, Y = 50, 6

RECT = r'rect (\d+)x(\d+)'
COL = r'rotate column x=(\d+) by (\d+)'
ROW = r'rotate row y=(\d+) by (\d+)'


def run():
    display = np.zeros((Y, X), dtype=int)
    with open('input.txt') as data:
        for instr in data:
            rect = re.match(RECT, instr)
            col = re.match(COL, instr)
            row = re.match(ROW, instr)
            if rect:
                a, b = map(int, rect.groups())
                display[:b, :a] = 1
            elif col:
                x, n = map(int, col.groups())
                display[:, x] = np.roll(display[:, x], n)
            else:
                y, n = map(int, row.groups())
                display[y] = np.roll(display[y], n)
    return display
