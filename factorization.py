#!/usr/bin/env python3

__author__ = 'zml'

import math


def is_prime(num):
    for i in range(2, math.ceil(math.sqrt(num)) + 1):
        if num % i == 0 and num != i:
            return False
    return True


def primes(start=1, primelimit=100):
    finals = 0
    last = start
    while finals < primelimit:
        last += 1
        if is_prime(last):
            yield last
            finals += 1


def prime_factorization(num):
    last_prime = 1
    while not is_prime(num):
        for i in primes(last_prime):
            if i == 1:
                continue
            while num % i == 0:
                yield i
                num //= i
            last_prime = i

    if not is_prime(num):
        print("Not actually prime!")

    if num != 1:
        yield num


if __name__ == "__main__":
    n = int(input("Prime factorization of integer n="))
    print("n=%d" % n, list(prime_factorization(n)))
