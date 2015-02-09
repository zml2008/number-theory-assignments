#!/usr/bin/env python3
__author__ = 'zml'

MAX_ITERS = 50000
def fivefivealgo(n):
    res = []
    for _ in range(MAX_ITERS):
        try:
            res.index(n)
            break
        except ValueError:
            pass
        res.append(n)

        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
    return res

if __name__ == "__main__":
    for i in range(1, 100 + 1):
        algo = fivefivealgo(i)
        print("%d: end=%d, len=%d" % (i, algo[-1], len(algo)))
    print(fivefivealgo(12))
