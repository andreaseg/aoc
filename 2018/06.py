import sys
import re
from collections import deque

def pretty_print_coord(tup):
    if tup[0] == 0 and tup[1] == 0:
        return '.'
    elif tup[1] == 0:
        return chr(tup[0] + 64)
    else:
        return chr(tup[0] + 96)

def part1(coords):
    width = max(coords, key = lambda tup: tup[0])[0] + 1
    height = max(coords, key = lambda tup: tup[1])[1] + 1
    places = [[(0, sys.maxsize) for x in range(height)] for y in range(width)]
    current_id = 0
    for start_coord in coords:
        dq = deque([start_coord])
        no_revisit = set()
        current_id += 1
        places[start_coord[0]][start_coord[1]] = (current_id, 0)
        while dq:
            coord = dq.popleft()
            distance = places[coord[0]][coord[1]][1]
            new_coords = []
            if coord[0] > 0:
                new_coords.append((coord[0] - 1, coord[1]))
            if coord[1] > 0:
                new_coords.append((coord[0], coord[1] - 1))
            if coord[0] < width - 1:
                new_coords.append((coord[0] + 1, coord[1]))
            if coord[1] < height - 1:
                new_coords.append((coord[0], coord[1] + 1))
            for new_coord in new_coords:
                (new_id, new_distance) = places[new_coord[0]][new_coord[1]]
                if new_distance == distance + 1 and current_id != new_id and new_coord not in no_revisit:
                    places[new_coord[0]][new_coord[1]] = (0, distance + 1)
                    no_revisit.add(new_coord)
                    dq.append(new_coord)
                elif new_distance > distance + 1:
                    places[new_coord[0]][new_coord[1]] = (current_id, distance + 1)
                    dq.append(new_coord)
    #for row in places:
    #    print(' '.join(map(pretty_print_coord, row)))

    areas = [0] * (current_id + 1)
    for row in places:
        for (pos_id, distance) in row:
            areas[pos_id] += 1

    for x in range(width):
        areas[places[x][0][0]] = 0
        areas[places[x][height - 1][0]] = 0
    for y in range(height):
        areas[places[0][y][0]] = 0
        areas[places[width - 1][y][0]] = 0
    areas[0] = 0

    print("Largest area is %i" % max(areas))


def main():
    co_reg = re.compile(r'(\d+),\s(\d+)')
    coords = []
    for line in sys.stdin:
        matches = co_reg.match(line)
        x = int(matches.group(1))
        y = int(matches.group(2))
        coords.append((x, y))
    part1(coords)

if __name__ == '__main__':
    main()
