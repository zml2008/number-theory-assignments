#!/usr/bin/env python3
__author__ = 'zml'

def gcd(a, b):
    low = min(a, b)
    high = max(a, b)
    while low != 0:
        high, low = low, high % low
    return high

def lcm(a, b):
    return (a * b) / gcd(a, b)

def another_lcm(a, b):
    low = min(a, b)
    high = max(a, b)
    while low != 0:
        high, low = (a*b)/low, high % low
    return high

if __name__ == "__main__":
    print(lcm(20, 30))
    print(another_lcm(20, 30))
    print(gcd(36, 132))
    print(gcd(12345, 67890))