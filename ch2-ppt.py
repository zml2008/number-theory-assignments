__author__ = 'zml'

from util import gathering_input, factors
from multiprocessing import Pool
import os
import itertools

def a(s, t):
    return s * t

def b(s, t):
    return ((s * s) - (t * t))/2


def c(s, t):
    return ((s * s) + (t * t))/2


def _input_func(s):
    rets = []
    for t in range(1, s, 2):
        if len((factors(s) & factors(t)) - {1}) == 0:
            rets.append((a(s, t), b(s, t), c(s, t)))
    return rets

@gathering_input("Maximum s value: ")
def generate_ppts(max_s):
    pool = Pool(os.cpu_count() * 2 + 1)
    values = sorted(itertools.chain(*pool.map(_input_func, list(range(1, max_s, 2)))))
    print(len(values), "pythagorean triples: ")
    for triple in values:
        print("%d² + %d² = %d²" % triple)

if __name__ == "__main__":
    generate_ppts()

