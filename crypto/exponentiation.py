from ch17_6 import solve

__author__ = 'zml'

from ch18_enc import TextbookCodec, KeyPair, PublicKey
from ch16_2 import successive_square

class SimpleAwfulCodec(TextbookCodec):
    ALPHHA_PREFIX = 65

__codec = SimpleAwfulCodec()

def expotentiate(text, p, e):
    return [successive_square(c, e, p) for c in __codec.encode(KeyPair(PublicKey(m=p, k=e), None), text)]

def dexponentiate(text, p, e):
    return __codec.decode(None, [solve(e, i, p) for i in text])


class SharedKeyCalculation(object):
    def __init__(self, p, x, e):
        self.p = p
        self.x = x
        self.e = e

    def calculate_yi(self):
        return successive_square(self.x, self.e, self.p)

    def calculate_shared(self, y_other):
        return successive_square(y_other, self.e, self.p)

def calculate_shared_key(x, p, e1, e2):
    one = SharedKeyCalculation(p, x, e1)
    two = SharedKeyCalculation(p, x, e2)
    return one.calculate_shared(two.calculate_yi())
