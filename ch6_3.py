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

if __name__ == "__main__":
    a, b = [int(s.strip()) for s in input("6.3: Provide 2 numbers to calculate the GCD of: ").split(",")]
    print(gxy(a, b))

