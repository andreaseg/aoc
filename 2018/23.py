import sys
import re
from z3 import *

def part1(input):
    max_line = max(input, key = lambda line: line['r'])
    res = len(list(filter(lambda line: abs(line['x'] - max_line['x']) + abs(line['y'] - max_line['y']) + abs(line['z'] - max_line['z']) <= max_line['r'] , input)))
    print('Number of nanobots in range %i' % res)

def distance(p, q):
    return abs(q['x'] - p['x']) + abs(q['y'] - p['y']) + abs(q['z'] - p['z']) 

origo = {'x': 0, 'y': 0, 'z': 0}
    

def part2(input):
    Tie, Shirt = Bools('Tie Shirt')
    s = Solver()
    s.add(Or(Tie, Shirt),
          Or(Not(Tie), Shirt),
          Or(Shirt, Not(Tie)))
    print(s.check())
    print(s.model())
   #print('Point overlapping most areas, closest to origin, is (%i, %i, %i) with score %i and distance %i' % (point['x'], point['y'], point['z'], point['score'], distance(origo, point)))


def main():
    regex = re.compile(r'pos=<(-?\d+),(-?\d+),(-?\d+)>,\sr=(\d+)')
    input = []
    for line in sys.stdin:
        m = regex.match(line)
        input.append({'x': int(m.group(1)), 'y': int(m.group(2)), 'z': int(m.group(3)), 'r': int(m.group(4))})
    print('Part 1')
    part1(input)
    print('Part 2')
    part2(input)

if __name__ == '__main__':
    main()
