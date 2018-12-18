import sys


def part1(constraints):
    steps = ['A']
    for char in [ chr(i) for i in range(ord('B'), ord('Z') + 1)]:
        has_inserted = False
        for i in range(len(steps)):
            if (char, steps[i]) in constraints:
                steps.insert(i, char)
                has_inserted = True 
                break
        if not has_inserted:
            steps.append(char)

    print(''.join(steps))

def main():
    constraints = set()
    for line in sys.stdin:
        constraints.add((line[5], line[36]))
    part1(constraints)


if __name__ == '__main__':
    main()
