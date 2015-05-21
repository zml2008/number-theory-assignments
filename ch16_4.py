__author__ = 'zml'

import random
import math
from ch16_2 import successive_square

class big_range(object):
    def __init__(self, start, end, step=1):
        self.start = start
        self.cur = start
        self.end = end
        self.step = 1

    def __len__(self):
        return (self.end - self.start) // self.step

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur + self.step == self.end:
            raise StopIteration
        ret = self.cur
        self.cur += self.step
        return ret



def ten_rands(min_num, max):
    #rng = random.SystemRandom()
    return random.sample(range(min_num, max + 1), min(abs(max - min_num), 20))

def probably_prime(n):
    if n == 1 or n == 2:
        return False
    if n == 3:
        return True

    for a in ten_rands(2, int(math.sqrt(n - 1))):
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

