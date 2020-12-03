class Keypad:
    def __init__(self, up, down, left, right):
        self.pos = 5
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    def process_line(self, line):
        for char in line:
            self.pos = self.up(self.pos) if char == 'U' else \
                       self.down(self.pos) if char == 'D' else \
                       self.left(self.pos) if char == 'L' else \
                       self.right(self.pos)
        return hex(self.pos)[2:].upper()


def solve(up, down, left, right):
    with open('input.txt') as data:
        keypad = Keypad(up, down, left, right)
        code = ''
        for line in (line.strip() for line in data):
            code += keypad.process_line(line)
        return code
