#!/usr/bin/env python3

__author__ = 'zml'

def successive_square(a, k, m):
    """
    Solve a successive square problem of the form a^k mod m
    """
    b = 1
    while k >= 1:
        if k % 2 == 1:
            b = (a*b) % m
        a = (a * a) % m
        k //= 2
    return b

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Calculate the value of a^k mod m")
    parser.add_argument("a", type=int)
    parser.add_argument("k", type=int)
    parser.add_argument("m", type=int)
    args = parser.parse_args()

    print("%d^%d mod %d=%d" % (args.a, args.k, args.m, successive_square(args.a, args.k, args.m)))
