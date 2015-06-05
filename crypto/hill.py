from ch6_3 import gxy

__author__ = 'zml'

from fractions import gcd
from numpy import matrix, linalg, identity
from decimal import Decimal

ALPHA_PREFIX=65

# From http://stackoverflow.com/questions/4287721/easiest-way-to-perform-modular-matrix-inversion-with-python
def inversemodp(a, p):
    a = a % p
    if a == 0:
        print("a is 0 mod p")
        return 0
    _, x, y = gxy(p, a % p)
    return y % p


def inversematrix(A, q):
    Ainv = identity(A.shape[0])
    #Aflat = A.flat
    n = A.shape[0]
    for i in range(0, n):
        factor = inversemodp(A[i, i], q)
        A[i] = A[i] * factor % q
        Ainv[i] = Ainv[i] * factor % q
        for j in range(0, n):
            if i != j:
                factor = A[j, i]
                A[j] = (A[j] - factor * A[i]) % q
                Ainv[j] = (Ainv[j] - factor * Ainv[i]) % q
                # print A, Ainv
                # print i, j, factor
    return Ainv

ONES = Decimal(1)

def int_det(A):
    return int(Decimal(linalg.det(A)).quantize(ONES))

def enhill(string, key):
    if key.shape[0] != key.shape[1]:
        raise BaseException("Non-square key!")
    if gcd(int_det(key), 26) != 1:
        raise BaseException("Matrix determinant is not relatively prime to 26")
    while len(string) % key.shape[0] != 0:
        string += "X"

    ret = []
    inp = string.upper().encode()
    print(inp)
    for i in range(0, len(string), key.shape[0]):
        ret.extend((key * matrix([[c - ALPHA_PREFIX] for c in inp[i:i + key.shape[0]]])).flat)

    print(ret)

    return bytes([(i % 26) + ALPHA_PREFIX for i in ret]).decode()


def dehill(string, key):
    if key.shape[0] != key.shape[1]:
        raise BaseException("Non-square key!")
    if gcd(int_det(key), 26) != 1:
        raise BaseException("Matrix determinant is not relatively prime to 26")
    if len(string) % key.shape[0] != 0:
        raise BaseException("String is not modular to block length")

    # key = key.getI()
    key = inversematrix(key, 26)

    ret = []
    inp = string.upper().encode()
    for i in range(0, len(string), key.shape[0]):
        ret.extend((key.dot(matrix([[c - ALPHA_PREFIX] for c in inp[i: i + key.shape[0]]]))).flat)

    print(ret)
    return bytes([int( i % 26) + ALPHA_PREFIX for i in ret]).decode()

def fixed_chars(key):
    ret = []
    for i in range(ALPHA_PREFIX, ALPHA_PREFIX + 26):
        for j in range(ALPHA_PREFIX, ALPHA_PREFIX + 26):
            test_str = "%c%c" % (i, j)
            if enhill(test_str, key) == test_str:
                ret.append(test_str)
                #print(test_str, " is left fixed!")
    return ret
