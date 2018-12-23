import sys
import re

def part1(input):
    max_line = max(input, key = lambda line: line['r'])
    res = len(list(filter(lambda line: abs(line['x'] - max_line['x']) + abs(line['y'] - max_line['y']) + abs(line['z'] - max_line['z']) <= max_line['r'] , input)))
    print('Number of nanobots in range %i' % res)


def main():
    regex = re.compile(r'pos=<(-?\d+),(-?\d+),(-?\d+)>,\sr=(\d+)')
    input = []
    for line in sys.stdin:
        m = regex.match(line)
        input.append({'x': int(m.group(1)), 'y': int(m.group(2)), 'z': int(m.group(3)), 'r': int(m.group(4))})
    print('Part 1')
    part1(input)

if __name__ == '__main__':
    main()
