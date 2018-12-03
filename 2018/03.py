import sys
import re
from typing import Tuple

def part1(claims):
    fabric = [[0] * 1000 for i in range(1000)]
    for claim in claims:
        for x in range(claim.pos[0], claim.pos[0] + claim.size[0]):
            for y in range(claim.pos[1], claim.pos[1] + claim.size[1]):
                fabric[x][y] += 1
    invalid_area = 0
    for line in fabric:
        for cell in line:
            if cell > 1:
                invalid_area += 1
    print("Invalid fabric area " + str(invalid_area))
    return fabric

def part2(fabric, claims):
    for claim in claims:
        overlaps = False
        for x in range(claim.pos[0], claim.pos[0] + claim.size[0]):
            for y in range(claim.pos[1], claim.pos[1] + claim.size[1]):
                if fabric[x][y] > 1:
                    overlaps = True
        if not overlaps:
            print("Non-overlapping claim " + str(claim))
            return

class Claim:
    def __init__(self, claim_id: int, pos: Tuple[int, int], size: Tuple[int, int]):
        self.claim_id = claim_id
        self.pos = pos
        self.size = size

    def __repr__(self):
        return "<Claim id: %i>" % self.claim_id

    def __str__(self):
        return "Claim (id: %i, pos: (%i,%i), size(%i,%i))" %(self.claim_id, self.pos[0], self.pos[1], self.size[0], self.size[1])

RE_PARSE = re.compile(r'#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)')

def parse_input(raw_line):
    result = RE_PARSE.match(raw_line)
    claim_id = int(result.group(1))
    pos = (int(result.group(2)), int(result.group(3)))
    size = (int(result.group(4)), int(result.group(5)))
    return Claim(claim_id, pos, size)


def main():
    claims = [parse_input(line) for line in sys.stdin]
    print("Part 1")
    fabric = part1(claims)
    print("Part 2")
    part2(fabric, claims)

if __name__ == '__main__':
    main()
