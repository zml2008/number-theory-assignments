#!/usr/bin/env python3

__author__ = 'zml'

def valid(x, y, z):
    return (x * x * x) + (y * y * y) == (z * z)

def calculate_triples(end=10):
    for x in range(1, end):
        for y in range(1, end): # Must not have both values be 0 -- div by 0!!!
            for z in range(1, end):
                ret = (x * z, y * z, z * z)
                # Possibly: (x, x * n, x^2)
                checks = (valid(*ret), z % (x+y) == 0)
                if checks[0] != checks[1]:
                    print("MISMATCH: ", (x, y, z), ret, checks, z/(x+y))
                if checks[0]:
                    print("VALID: ", (x, y, z), ret, checks, z / (x+y))

if __name__ == "__main__":
    calculate_triples()
