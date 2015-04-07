__author__ = 'zml'

import factorization

def euler_phi(num):
    vals = {}
    for i in factorization.prime_factorization(num):
        vals[i] = vals.get(i, 0) + 1
    print(vals)

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

