import sys


def main():
    nums = [int(l) for l in sys.stdin]
    freqs = set()
    frequency = 0
    while True:
        for num in nums:
            frequency += num
            if frequency not in freqs:
                freqs.add(frequency)
            else:
                print("Frequency is "+str(frequency))
                return



if __name__ == '__main__':
    main()
