import sys

def main():
    doubles = 0
    triples = 0
    
    for line in sys.stdin:
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



if __name__ == '__main__':
    main()
