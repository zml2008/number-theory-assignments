#!/usr/bin/env python3

__author__ = 'zml'

from factorization import prime_factorization, is_prime
from congruence import parse_congruency
import argparse

def infinitely_many_primes(congruency):
    """
    Check if infinitely many primes are congruent to the given congruency
    :param congruency:
    :return:
    """
    pass

def prime_or_in_list(num, list):
    if is_prime(num):
        return True

    num_index = list.index(num)
    if num_index == -1:
        raise BaseException("Invalid input! Number must be in the given list")
    for i in prime_factorization(num):
        try:
            list.index(i, 0, num_index)
            return True
        except ValueError:
            pass
    return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("congruency", type=parse_congruency, help="The congruence to find matching primes for")
    parser.add_argument("max", type=int, help="The maximum number to test")
    args = parser.parse_args()

    _, c, m = args.congruency
    modulars = list(range(c, args.max, m))
    primeys = list(filter(lambda n: prime_or_in_list(n, modulars), modulars))
    # print("Modulars (#: %d): %s, primeys (#: %d): %s" % (len(modulars), modulars, len(primeys), primeys))
    print("Eucilid's applies: %s" % (len(modulars) == len(primeys)))


