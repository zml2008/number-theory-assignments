#!/usr/bin/env python3

__author__ = 'zml'
from ch6_3 import gxy
import re

CONGRUENCY_REGEX = re.compile(r'(\d+)x=(\d+)(?:mod|%)(\d+)')


def congruencies(a, c, m):
    """
    Congruency of the form a*x {congruent to} b mod c
    :return: yielding solutions to the congruency
    """
    g, x, y = gxy(a, m)
    if c % g != 0: # If g does not divide c, then we don't get a fancy solution
        return

    x0 = (c * x) / g
    for k in range(0, g):
        yield x0 + (k * m/g)


def main(args):
    if len(args) < 1:
        print("No argument specified. First arg must be of form ax=cmodm")
        return 1

    match = CONGRUENCY_REGEX.match(args[0])
    if not match:
        print("Invalid result %s. Input must be of the form ax=cmodm" % args[0])
        return 1
    a = int(match.group(1))
    c = int(match.group(2))
    m = int(match.group(3))

    for res in congruencies(a, c, m):
        print("x=%d mod %d" % (res % m, m))

    return 0


if __name__ == "__main__":
    import sys
    inp = input("Provide congruency of ax=cmodm: ")
    sys.exit(main([inp]))
