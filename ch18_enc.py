__author__ = 'zml'

from ch17_6 import solve
from collections import namedtuple
import random

PrivateKey = namedtuple("PrivateKey", ["p", "q"])
PublicKey = namedtuple("PublicKey", ["m", "k"])

class KeyException(BaseException):
    pass

class KeyPair(object):
    def __init__(self, public, private):
        self.__public = public
        self.__private = private

    @classmethod
    def random_key(cls, keysize):
        rng = random.SystemRandom()
        p = rng.getrandbits(keysize // 2)
        q = rng.getrandbits(keysize // 2)
        k = rng.getrandbits(32)
        return cls(PublicKey(p * q, k), PrivateKey(p, q))

    @classmethod
    def from_file(cls, path):
        pass

    def decrypt(self, inp):
        if self.__private is None:
            raise KeyException("No private key, cannot decrypt!")
        return [solve(self.__public.k, i, self.__public.m, factors=[self.__private.p, self.__private.q]) for i in inp]

    def encrypt(self, inp):
        return [i ** self.__public.k % self.__public.m for i in inp]


class StringCodec(object):
    # TODO actually implement
    pass

class TextbookCodec(object):
    def encode(self, inp):
        return [i - 54 for i in inp.upper().encode()]

    def decode(self, inp):
        print(inp)
        single, split = [], []
        for i in inp:
            while i > 100:
                single.append(i % 100)
                i //= 100
            if i < 10:
                raise BaseException("Non-pair-digited number!")
            single.append(i % 100)
            split.extend(single[::-1])
            single.clear()

        print(split)
        return bytes([i + 54 for i in split]).decode()


def annotate_keys(args, func):
    pass

def decrypt_textbook_cb(keypair, args):
    codec = TextbookCodec()
    print("Decoded: %s", codec.decode(keypair.decrypt(args.input)))

def ch18_1_test():
    pair = KeyPair(PublicKey(m=73*97, k=1789), PrivateKey(p=73, q=97))
    decoder = TextbookCodec()
    encoded = pair.encrypt(decoder.encode('FERMATI'))
    print(encoded)
    print(decoder.decode(pair.decrypt(encoded)))
    #print(decoder.decode(pair.decrypt([5192, 2604, 4222])))

    pair = KeyPair(PublicKey(m=123456789012345681631*7746289204980135457, k=12398737), PrivateKey(p=123456789012345681631, q=7746289204980135457))
    print(decoder.decode(pair.decrypt([821566670681253393182493050080875560504,
                                       87074173129046399720949786958511391052,
                                       552100909946781566365272088688468880029,
                                       491078995197839451033115784866534122828,172219665767314444215921020847762293421])))

if __name__ == "__main__":
    ch18_1_test()
    import argparse
    parser = argparse.ArgumentParser(description="utility to parse files")

    def add_key_args(subcommand):
        subcommand.add_argument("--pubkey")
        subcommand.add_argument("--privkey")

    subs = parser.add_subparsers()
    gen_keys = subs.add_parser(name="gen-keys")
    #add_key_args(gen_keys)

    decrypt_textbook = subs.add_parser(name="decrypt-textbook", description="Decrypt using textbook algorithm")
    decrypt_textbook.set_defaults(func=decrypt_textbook_cb)
# key: m=p*q, k,
# break up message into dicits less than m
#  use seggessive squaring to compute a_n^k modm these large numbers form b1, b2, br

# decode:
# compute phi(m) (we know the factorization
# solve with roots --
