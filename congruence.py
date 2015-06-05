#!/usr/bin/env python3

__author__ = 'zml'
from ch6_3 import gxy
import re
import argparse

CONGRUENCY_REGEX = re.compile(r'([\d\-]+)?\s*(?:\*\s*)?x\s*=\s*([\d\-]+)\s*(?:mod|%)\s*([\d\-]+)\s*$')


def gxy_neg(a, b):
    g, x, y = gxy(a, b)
    return g, x, -y


def congruencies(a, c, m):
    """
    Congruency of the form a*x {congruent to} b mod c
    :return: yielding solutions to the congruency
    """
    g, x, y = gxy_neg(a, m)
    if c % g != 0: # If g does not divide c, then we don't get a fancy solution
        return []

    x0 = (c * x) / g
    return [x0 + (k * m/g) for k in range(0, g)]


def parse_congruency(congr):
    match = CONGRUENCY_REGEX.match(congr)
    if not match:
        raise argparse.ArgumentTypeError("Invalid result %s. Input must be of the form ax=cmodm" % congr)
    if match.group(1):
        a = int(match.group(1))
    else:
        a = 1
    c = int(match.group(2))
    m = int(match.group(3))
    return (a, c, m)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('congruence', type=parse_congruency, help="The congruency to solve")
    p_args = parser.parse_args()

    a, c, m = p_args.congruence
    cong = congruencies(a, c, m)
    print("# of results:", len(cong))
    for res in cong:
        print("x=%d mod %d" % (res % m, m))

    return 0


if __name__ == "__main__":
    import sys
    # inp = input("Provide congruency of ax=cmodm: ")
    print(sys.argv)
    sys.exit(main())
