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

    def cmp(self, other):
        for x in range(self.width):
            for y in range(self.height):
                if self.read(x, y) != other.read(x, y):
                    return False
        return True

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

    def value(self):
        lumberyards = 0
        woods = 0
        for x in range(self.width):
            for y in range(self.height):
                value = self.read(x, y)
                if value == '#':
                    lumberyards += 1
                elif value == '|':
                    woods += 1
        return lumberyards * woods


def part1(input):
    new_area = input.evolve()
    for i in range(1, 10):
        new_area = new_area.evolve()
    new_area.print()

    print('Lumber value %i' % new_area.value())


def part2(input):
    new_area = input
    for i in range(0, 900):
        new_area = new_area.evolve()
    cached_areas = []
    for i in range(900, 1000):
        cached_areas.append(new_area.value())
        new_area = new_area.evolve()
        print('%i: %i' % (i, new_area.value()))
    cycle_length = 0
    for i in range(1, 100):
        if cached_areas[i] == cached_areas[0]:
            cycle_length = i
            break
    print('Cycle length %i' % cycle_length)
    final_value = cached_areas[(1000000000 - 900) % cycle_length]
    print('Value after 10.000 years is %i' % final_value)


def main():
    data = [[char for char in line.rstrip()] for line in sys.stdin.readlines()]
    input = Area(len(data[0]), len(data))
    input.data = data

    print('Part 1')
    part1(input)
    print('Part 2')
    part2(input)

if __name__ == '__main__':
    main()
