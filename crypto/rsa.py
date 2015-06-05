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

def sign(text, e_from, n_from, e_to, n_to):
    pair_encode = KeyPair(PublicKey(m=min(n_from, n_to), k=-1), None)
    nums = __codec.encode(pair_encode, text)
    return [successive_square(solve(e_from, i, n_from), e_to, n_to) for i in nums]

def unsign(nums, e_from, n_from, e_to, n_to):
    dec = [successive_square(solve(e_to, i, n_to), e_from, n_from) for i in nums]
    return __codec.decode(None, dec)
