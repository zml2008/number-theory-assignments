#!/usr/bin/env python3

__author__ = 'zml'

def valid(x, y, z):
    return (x * x * x) + (y * y * y) == (z * z)

def calculate_triples(end=1225):
    valid_vals = []
    for c in range(1, end):
        num = 0
        for b in range(1, c): # Must not have both values be 0 -- div by 0!!!
            for a in range(1, b + 1):
                #ret = (x * z, y * z, z * z)
                ret = (a, b, c)
                # Possibly: (x, x * n, x^2)

                checks = (valid(*ret))# z/(x+y) == (y**2)-num)
                #if checks[0] != checks[1]:
                #    pass
                    #print("MISMATCH: ", (x, y, z), ret, checks, z/(x+y))
                if checks:
                    print("VALID: ", ret, checks)
                    valid_vals.append(ret)
                    num += 1

    for triple in filter(is_primitive, valid_vals):
        print("%d³+%d³=%d²" % triple)


def is_primitive(triple):
    for n in range(2, max(triple)):
        if triple[0] % (n ** 3) == 0 and triple[1] % (n ** 3) == 0 and triple[0] % (n ** 2) == 0:
            return False
    return True

if __name__ == "__main__":
    calculate_triples()
