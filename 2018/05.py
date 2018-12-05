import sys

def part1():
    input_string = []
    while True:
        char = sys.stdin.read(1)
        if not char:
            break
        elif not input_string:
            input_string = [char[0]]
        elif chr_match(input_string[-1], char[0]):
            del input_string[-1]
        else:
            input_string.append(char[0])
    print("Length of polymer %i" % (len(input_string) - 1))
    return input_string

def chr_match(left: chr, right: chr):
    return abs(ord(left) - ord(right)) == 32

def part2(input_string):
    min_length = sys.maxsize
    for char in range(ord('a'), ord('z') + 1):
        lower = chr(char)
        upper = chr(char - 32)
        new_string = []
        for i in input_string:
            if i == lower or i == upper:
                continue
            elif not new_string:
                new_string = [i]
            elif chr_match(new_string[-1], i):
                del new_string[-1]
            else:
                new_string.append(i)
        min_length = min(min_length, len(new_string) - 1)
    print("Length of polymer %i" % min_length)


def main():
    print("Part 1")
    polymer = part1()
    print("Part 2")
    part2(polymer)

if __name__ == '__main__':
    main()
