#!/usr/bin/env python3
__author__ = 'zml'

import fractions
def gcd(a, b):
    low = min(a, b)
    high = max(a, b)
    while low != 0:
        high, low = low, high % low
    return high


if __name__ == "__main__":
    print(gcd(36, 132))
    print(gcd(12345, 67890))