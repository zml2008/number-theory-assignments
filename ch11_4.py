__author__ = 'zml'

import factorization
import functools
import itertools

def euler_phi(num, factors=None):
    vals = {}

    if factors is None:
        factors = factorization.prime_factorization(num)
    else:
        if functools.reduce(lambda a, b: a * b, factors, 1) != num:
            raise BaseException("Factors do not equal input number!")
            pass
        #if not functools.reduce(lambda a, b: a and b, [factorization.is_prime(n) for n in factors], True):
        #    print("Doing factorization?")
        #    factors = itertools.chain([factorization.prime_factorization(n) for n in factors])


    for i in factors:
        vals[i] = vals.get(i, 0) + 1

    # phi(mn) = phi(m)*phi(n)
    # phi(p) = p - 1
    # phi(p^n) = p^n - p^(n-1)

    accumulator = 1
    for p, n in vals.items():
        accumulator *= p ** n - p ** (n - 1)

    return accumulator

if __name__ == "__main__":
    arg = int(input("φ of: "))
    print("φ(%d)=%d" % (arg, euler_phi(arg)))

