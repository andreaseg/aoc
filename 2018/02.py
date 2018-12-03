import sys
from functools import reduce

def part1(stdin):
    doubles = 0
    triples = 0

    for line in stdin:
        alphabet = 27 * [0]
        for char in line.rstrip():
            alphabet[ord(char) - ord('a')] += 1
        line_triples = 0
        line_doubles = 0
        for num in alphabet:
            if num >= 3:
                line_triples = 1
            elif num == 2:
                line_doubles = 1
        doubles += line_doubles
        triples += line_triples
    print("Checksum: " + str(doubles) + " * " + str(triples) + " = " + str(doubles * triples))

def checksum(line):
    return reduce(lambda l, r: l + ord(r), line, 0)

def matchlines(line1, line2):
    if len(line1) != len(line2):
        return False
    distance = 0
    for i in range(0, len(line1)):
        if line1[i] != line2[i]:
            distance += 1
    return distance <= 1

def part2(stdin):
    lines = [(line.rstrip(), checksum(line.rstrip())) for line in stdin]
    lines.sort(key=lambda tup: tup[1])
    for i in range(0, len(lines) - 1):
        for j in range(i+1, len(lines)):
            if lines[j][1] > lines[i][1] + 26:
                break
            if matchlines(lines[i][0], lines[j][0]):
                print(lines[i][0] + "\n" + lines[j][0])
                result = ""
                for chi in range(0, len(lines[i][0])):
                    if lines[i][0][chi] == lines[j][0][chi]:
                        result += lines[i][0][chi]
                print(result)
                return

def main():
    stdin = sys.stdin.readlines()
    print("Part 1")
    part1(stdin)
    print("\nPart 2")
    part2(stdin)

if __name__ == '__main__':
    main()
