import sys

class Area:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.data = [['.' for x in range(width)] for y in range(height)] 

    def read(self, x_coord: int, y_coord: int) -> chr:
        return self.data[x_coord][y_coord]

    def write(self, x_coord: int, y_coord: int, value: chr):
        self.data[x_coord][y_coord] = value

    def width(self) -> int:
        return self.width

    def height(self) -> int:
        return self.height

    def surroundings(self, x_coord: int, y_coord: int):
        dict = {'.': 0, '|': 0, '#': 0}
        if x_coord > 0:
            dict[self.read(x_coord - 1, y_coord)] += 1
        if y_coord > 0:                   
            dict[self.read(x_coord, y_coord - 1)] += 1
        if x_coord + 1 < self.width:
            dict[self.read(x_coord + 1, y_coord)] += 1 
        if y_coord + 1 < self.height:
            dict[self.read(x_coord, y_coord + 1)] += 1
        if x_coord > 0 and y_coord > 0:
            dict[self.read(x_coord - 1, y_coord - 1)] += 1
        if x_coord + 1 < self.width and y_coord + 1 < self.height:
            dict[self.read(x_coord + 1, y_coord + 1)] += 1
        if x_coord > 0 and y_coord + 1 < self.height:
            dict[self.read(x_coord - 1, y_coord + 1)] += 1
        if x_coord + 1 < self.width and y_coord > 0:
            dict[self.read(x_coord + 1, y_coord - 1)] += 1
        return dict
    
    def print(self):
        for line in self.data:
            print(''.join(map(str, line)))

    def copy(self):
        new = Area(self.width, self.height)
        for x in range(self.width):
            for y in range(self.height):
                new.write(x, y, self.read(x, y))
        return new

    def evolve(self):
        next = self.copy() 
        for x in range(self.width):
            for y in range(self.height):
                dict = self.surroundings(x, y)
                if self.read(x, y) == '.' and dict['|'] >= 3:
                    next.write(x, y, '|')
                if self.read(x, y) == '|' and dict['#'] >= 3:
                    next.write(x, y, '#')
                if self.read(x, y) == '#' and (dict['#'] == 0 or dict['|'] == 0):
                    next.write(x, y, '.')

        return next


def part1(input):
    new_area = input.evolve()
    for i in range(1, 10):
        new_area = new_area.evolve()
    new_area.print()

    lumberyards = 0
    woods = 0
    for x in range(new_area.width):
        for y in range(new_area.height):
            value = new_area.read(x, y)
            if value == '#':
                lumberyards += 1
            elif value == '|':
                woods += 1
    print('Lumber valye %i' % (lumberyards * woods))

def main():
    data = [[char for char in line.rstrip()] for line in sys.stdin.readlines()]
    input = Area(len(data[0]), len(data))
    input.data = data

    print('Part 1')
    part1(input)

if __name__ == '__main__':
    main()
