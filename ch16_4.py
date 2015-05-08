__author__ = 'zml'

import random
from ch16_2 import successive_square

def ten_rands(min_num, max):
    rng = random.SystemRandom()
    return rng.sample(range(min_num, max + 1), min(abs(max - min_num), 10))

def probably_prime(n):
    for a in ten_rands(2, n - 1):
        if successive_square(a, n - 1, n) != 1:
            return False
    return True

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Check if a given number is probably prime")
    parser.add_argument("n", type=int)
    args = parser.parse_args()
    if probably_prime(args.n):
        print("Input %d is probably prime" % args.n)
    else:
        print("Input %d is composite" % args.n)

