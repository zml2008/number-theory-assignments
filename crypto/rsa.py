from ch16_2 import successive_square
from ch17_6 import solve
from ch18_enc import KeyPair, PublicKey

__author__ = 'zml'

from .exponentiation import SimpleAwfulCodec

__codec = SimpleAwfulCodec()

def enrsa(text, e, n):
    return [successive_square(c, e, n) for c in __codec.encode(KeyPair(PublicKey(m=n, k=e), None), text)]
    pass

def dersa(nums, e, n):
    return __codec.decode(None, [solve(e, i, n) for i in nums])
    pass
