import sys
import re

class VirtualMachine:
    def __init__(self, pcri):
        self.pcri = pcri
        self.reg = [0] * 6

    def set_regs(self, value):
        self.reg = value

    def get_pc(self):
        return self.reg[self.pcri]

    def addr(self, left, right, target):
        self.reg[target] = self.reg[left] + self.reg[right]

    def addi(self, left, right, target):
        self.reg[target] = self.reg[left] + right

    def mulr(self, left, right, target):
        self.reg[target] = self.reg[left] * self.reg[right]

    def muli(self, left, right, target):
        self.reg[target] = self.reg[left] * right

    def banr(self, left, right, target):
        self.reg[target] = self.reg[left] & self.reg[right]

    def bani(self, left, right, target):
        self.reg[target] = self.reg[left] & right

    def borr(self, left, right, target):
        self.reg[target] = self.reg[left] | self.reg[right]

    def bori(self, left, right, target):
        self.reg[target] = self.reg[left] | right

    def setr(self, left, right, target):
        self.reg[target] = self.reg[left]

    def seti(self, left, right, target):
        self.reg[target] = left

    def gtir(self, left, right, target):
        self.reg[target] = 1 if left > self.reg[right] else 0

    def gtri(self, left, right, target):
        self.reg[target] = 1 if self.reg[left] > right else 0

    def gtrr(self, left, right, target):
        self.reg[target] = 1 if self.reg[left] > self.reg[right] else 0

    def eqir(self, left, right, target):
        self.reg[target] = 1 if left == self.reg[right] else 0

    def eqri(self, left, right, target):
        self.reg[target] = 1 if self.reg[left] == right else 0

    def eqrr(self, left, right, target):
        self.reg[target] = 1 if self.reg[left] == self.reg[right] else 0

    def exec_op_code(self, op_code, left, right, target):
        getattr(self, op_code)(left, right, target) 
        self.reg[self.pcri] += 1

    def run(self, input, max_iteration):
        iteration = 0
        while self.get_pc() >= 0 and self.get_pc() < len(input) and iteration < max_iteration:
            i = self.get_pc()
            op_code = input[i]['op_code']
            left = input[i]['left']
            right = input[i]['right']
            target = input[i]['target']
            print('%i: %s %i %i %i [%i,%i,%i,%i,%i,%i], PC = %i' % (iteration, op_code, left, right, target, self.reg[0], self.reg[1], self.reg[2], self.reg[3], self.reg[4], self.reg[5], i))
            self.exec_op_code(op_code, left, right, target)
            iteration += 1

def part1(pcri, input):
    vm = VirtualMachine(pcri)
    while vm.get_pc() >= 0 and vm.get_pc() < len(input):
        i = vm.get_pc()
        vm.exec_op_code(input[i]['op_code'], input[i]['left'], input[i]['right'], input[i]['target'])
    print('Value in register 0 is %i' % vm.reg[0])

def part2(pcri, input):
    vm = VirtualMachine(pcri)
    vm.reg[0] = 1
    vm.run(input, 31)
    magic_number = vm.reg[4]
    print('Magic number is %i' % magic_number)
    print('Answer is %i (sum of factors of magic number) ' % (1 + 2 + (magic_number / 2) + magic_number))

def main():
    raw_input = sys.stdin.readlines()
    pcri = int(raw_input.pop(0)[4])
    print('PC register is %i' % pcri)
    regex = re.compile(r'(\w{4})\s(\d+)\s(\d+)\s(\d+)')
    input = []
    for line in raw_input:
        m = regex.match(line)
        input.append({'op_code': m.group(1), 'left': int(m.group(2)), 'right': int(m.group(3)), 'target': int(m.group(4))})
    print('Part 1')
    part1(pcri, input)
    print('Part 2')
    part2(pcri, input)

if __name__ == '__main__':
    main()
