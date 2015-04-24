#!/usr/bin/env python3

__author__ = 'zml'

import math


def is_prime(num):
    if num % 2 == 0 and num != 2:
        return False
    for i in range(1, math.ceil(math.sqrt(num)) + 1, 2):
        if i == 1:
            continue
        if num % i == 0 and num != i:
            return False
    return True


def primes(start=1, primelimit=100):
    finals = 0
    if start == 1:
        yield 2
        finals = 1
    last = start
    while finals < primelimit:
        last += 2
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
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("number", metavar="n", type=int, help="The number to get the prime factorization of")
    args = parser.parse_args()
    print("n=%d" % args.number, list(prime_factorization(args.number)))
