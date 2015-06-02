from ch17_6 import solve

__author__ = 'zml'

from ch18_enc import TextbookCodec, KeyPair, PublicKey, PrivateKey
from ch16_2 import successive_square

class SimpleAwfulCodec(TextbookCodec):
    ALPHHA_PREFIX = 65

__codec = SimpleAwfulCodec()

def expotentiate(text, p, e):
    return [successive_square(c, e, p) for c in __codec.encode(KeyPair(PublicKey(m=p, k=e), None), text)]

def dexponentiate(text, p, e):
    return __codec.decode(None, [solve(e, i, p) for i in text])
