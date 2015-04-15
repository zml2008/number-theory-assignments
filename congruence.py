#!/usr/bin/env python3

__author__ = 'zml'
from ch6_3 import gxy
import re

CONGRUENCY_REGEX = re.compile(r'(\d+)?\s*(?:\*\s*)?x\s*=\s*(\d+)\s*(?:mod|%)\s*(\d+)\s*$')


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
        raise "Invalid result %s. Input must be of the form ax=cmodm" % congr
    if match.group(1):
        a = int(match.group(1))
    else:
        a = 1
    c = int(match.group(2))
    m = int(match.group(3))
    return (a, c, m)


def main(args):
    if len(args) < 1:
        print("No argument specified. First arg must be of form ax=cmodm")
        return 1


    a, c, m = parse_congruency(args[0])
    cong = congruencies(a, c, m)
    print("# of results:", len(cong))
    for res in cong:
        print("x=%d mod %d" % (res % m, m))

    return 0


if __name__ == "__main__":
    import sys
    inp = input("Provide congruency of ax=cmodm: ")
    sys.exit(main([inp]))
