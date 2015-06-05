#!/usr/bin/env python
__author__ = 'zml'

from fractions import gcd
from ch11_4 import euler_phi
from ch6_3 import gxy_ascending
from ch16_2 import successive_square

def solve(k, b, m, factors=None):
    #print("solve(k=%d,b=%d,m=%d" % (k, b, m))
    #if gcd(b, m) != 1:
    #    raise BaseException("B and m not relatively prime")
    phi = euler_phi(m, factors)

    if gcd(phi, k) != 1:
        raise BaseException("phi and k not relatively prime")

    for g, u, v in gxy_ascending(k, phi):
        if u >= 0:
            return successive_square(b, u, m)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Solve an equation of the form x^k = b mod m")
    parser.add_argument("k", type=int)
    parser.add_argument("b", type=int)
    parser.add_argument("m", type=int)
    args = parser.parse_args()

    print("x=%d" % solve(args.k, args.b, args.m))

