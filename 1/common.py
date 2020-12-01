class Walker:
    def __init__(self, store_visited=False):
        self.x = 0
        self.y = 0
        self.direction = 0
        self.visited = {(0, 0)} if store_visited else None

    def turn(self, direction):
        self.direction += 1 if direction == 'R' else -1
        self.direction %= 4

    def check_visited(self):
        if self.visited is None:
            return False
        if (self.x, self.y) in self.visited:
            return True
        else:
            self.visited.add((self.x, self.y))
            return False

    def move(self, length):
        step = 1 if self.direction in [0, 1] else -1

        for l in range(length):
            if self.direction in [0, 2]:
                self.x += step
            else:
                self.y += step
            check = self.check_visited()
            if check:
                break
        return check

    def follow_path(self, steps):
        for step in steps:
            self.turn(step[0])
            if self.move(int(step[1:])):
                break


def tokenize():
    with open('input.txt') as data:
        return data.readline().strip().split(', ')


def solve(store_visited=False):
    walker = Walker(store_visited)
    walker.follow_path(tokenize())
    return abs(walker.x) + abs(walker.y)
