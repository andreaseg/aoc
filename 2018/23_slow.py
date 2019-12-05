import sys
import re
import math
from itertools import combinations

def part1(input):
    max_line = max(input, key = lambda line: line['r'])
    res = len(list(filter(lambda line: abs(line['x'] - max_line['x']) + abs(line['y'] - max_line['y']) + abs(line['z'] - max_line['z']) <= max_line['r'] , input)))
    print('Number of nanobots in range %i' % res)

def distance(p, q):
    return abs(q['x'] - p['x']) + abs(q['y'] - p['y']) + abs(q['z'] - p['z']) 

def intersects(area, point):
    if point['x'] > area['x_max'] + point['r'] or point['x'] < area['x_min'] - point['r']:
        return False
    if point['y'] > area['y_max'] + point['r'] or point['y'] < area['y_min'] - point['r']:
        return False
    if point['z'] > area['z_max'] + point['r'] or point['z'] < area['z_min'] - point['r']:
        return False

    maxr = max([abs(area['x_max'] - point['x']), abs(area['x_min'] - point['x']), abs(area['y_max'] - point['y']), abs(area['y_min'] - point['y']), abs(area['z_max'] - point['z']), abs(area['z_min'] - point['z'])])

    if ((area['x_max'] + area['x_min']) / 2 - point['x'])**2 + ((area['y_max'] + area['y_min']) / 2 - point['y'])**2 + ((area['z_max'] + area['z_min']) / 2 - point['z'])**2 > (maxr + point['r'] + 1)**2:  
        return False

    return True

def partition(area):
    mid_x = math.floor((area['x_max'] + area['x_min']) / 2)
    mid_y = math.floor((area['y_max'] + area['y_min']) / 2)
    mid_z = math.floor((area['z_max'] + area['z_min']) / 2)

    partitions = []
    for x in [(area['x_min'], mid_x), (mid_x + 1, area['x_max'])]:
        if x[1] < x[0]:
            continue
        for y in [(area['y_min'], mid_y), (mid_y + 1, area['y_max'])]:
            if y[1] < y[0]:
                continue
            for z in [(area['z_min'], mid_z), (mid_z + 1, area['z_max'])]:
                if z[1] < z[0]:
                    continue
                partitions.append({'x_min': x[0], 'x_max': x[1], 'y_min': y[0], 'y_max': y[1], 'z_min': z[0], 'z_max': z[1]})
    return partitions

def score(input, area):
    return len(list(filter(lambda p: intersects(area, p), input)))

def score_point(input, x, y, z):
    return {'x': x, 'y': y, 'z': z, 'score': len(list(filter(lambda p: distance(p, {'x': x, 'y': y, 'z': z}) <= p['r'], input)))}

origo = {'x': 0, 'y': 0, 'z': 0}
closest_distance = sys.maxsize
    
def dfs(input, areascore):
    area = areascore['area']
    min_score = areascore['score']
    if area['x_min'] == area['x_max'] and area['y_min'] == area['y_max'] and area['z_min'] == area['z_max']:
        current_score = score_point(input, area['x_min'], area['y_min'], area['z_min'])
        global closest_distance
        dst = distance(origo, current_score)
        if dst < closest_distance:
            closest_distance = dst
            print('Score %i, distance %i' % (current_score['score'], dst))
        return current_score

    scores = list(map(lambda p: {'area': p, 'score': score(input, p)}, partition(area)))
    scores.sort(key = lambda s: s['score'])
    best_point = dfs(input, scores.pop())
    scores = list(filter(lambda s: s['score'] > best_point['score'] and s['score'] >= min_score, scores))
    while scores:
        dfs_point = dfs(input, {'area': scores.pop()['area'], 'score': max(best_point['score'], min_score)})
        if dfs_point['score'] > best_point['score'] or (dfs_point['score'] == best_point['score'] and distance(origo, dfs_point) < distance(origo, best_point)):
            best_point = dfs_point
            scores = list(filter(lambda s: s['score'] > best_point['score'], scores))
    return best_point


def part2(input):
    x_min = sys.maxsize
    y_min = sys.maxsize
    z_min = sys.maxsize
    x_max = -sys.maxsize
    y_max = -sys.maxsize
    z_max = -sys.maxsize
    for point in input:
        x_min = min(point['x'], x_min)
        y_min = min(point['y'], x_min)
        z_min = min(point['z'], x_min)
        x_max = max(point['x'], x_max)
        y_max = max(point['y'], x_max)
        z_max = max(point['z'], x_max)

    area = {'x_min': x_min, 'y_min': y_min, 'z_min': z_min, 'x_max': x_max, 'y_max': y_max, 'z_max': z_max} 
    point = dfs(input, {'area': area, 'score': 0})
    print('Point overlapping most areas, closest to origin, is (%i, %i, %i) with score %i and distance %i' % (point['x'], point['y'], point['z'], point['score'], distance(origo, point)))


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
