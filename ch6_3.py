#!/usr/bin/env python3
__author__ = 'zml'


def gxy(start_a, start_b):
    gcd, remainder = start_a, start_b
    x, y_calc = 1, 0

    while remainder != 0:
        quotient, temp_rem = divmod(gcd, remainder)
        s = x - quotient * y_calc
        x, gcd = y_calc, remainder
        y_calc, remainder = s, temp_rem
    return gcd, x, (gcd - start_a * x) / start_b


def gxy_ascending(a, b):
    """
    Get all values of ax+by=gcd(a, b) with increasing u values
    """
    return __gxy_all(a, b, 1)


def gxy_descending(a, b):
    """
    Get all values of ax+by=gcd(a, b) with decreasing u values
    """
    return __gxy_all(a, b, -1)


def __gxy_all(start_a, start_b, incr):
    g, x, y = gxy(start_a, start_b)
    k = 0
    while True:
        yield g, x + k * start_b, y + k * start_a
        k += incr

if __name__ == "__main__":
    a, b = [int(s.strip()) for s in input("6.3: Provide 2 numbers to calculate the GCD of: ").split(",")]
    print(gxy(a, b))

