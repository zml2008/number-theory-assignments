#!/usr/bin/env python3

def a(u, v):
    return u * u - v * v


def b(u, v):
    return 2 * v * u


def c(u, v):
    return u * u + v * v


def no_shared_factors(s, t):
    for i in range(2, min(s, t) + 1):
        if s % i == 0 and t % i == 0:
            return False
    return True


def print_ppts():
    max_u = int(input("Maximum u value: "))
    count = 0
    for u in range (1, max_u + 1):
        for v in range(1, u):
            if no_shared_factors(u, v) and (u - v) % 2 != 0:
                count += 1
                print((u, v, a(u, v), b(u, v), c(u, v)))
    print("Total number of PPTs:", count)

if __name__ == "__main__":
    print_ppts()
