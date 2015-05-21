__author__ = 'zml'
from ch17_6 import solve
from ch16_2 import successive_square
from ch16_4 import probably_prime
from collections import namedtuple
from fractions import gcd
import math
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

        p = cls.__rand_prime(rng, keysize // 2)
        q = cls.__rand_prime(rng, keysize // 2)
        k = cls.rel_prime_num(rng, (p - 1) * (q - 1), 32)
        return cls(PublicKey(p * q, k), PrivateKey(p, q))

    @staticmethod
    def rel_prime_num(rng, against, len):
        ret = against
        while gcd(ret, against) != 1:
            ret = rng.getrandbits(32)
        return ret


    @staticmethod
    def __rand_prime(rng, len):
        ret = 2
        while not probably_prime(ret):
            ret = rng.getrandbits(len)
        return ret

    @classmethod
    def from_file(cls, path):
        pass

    @property
    def private(self):
        return self.__private

    @property
    def public(self):
        return self.__public

    def decrypt(self, inp):
        if self.__private is None:
            raise KeyException("No private key, cannot encrypt!")
        return [solve(self.__public.k, i, self.__public.m, factors=[self.__private.p, self.__private.q]) for i in inp]

    def encrypt(self, inp):
        print(self.__public.k)
        print(self.__public.m)

        return [successive_square(i, self.__public.k, self.__public.m) for i in inp]


class StringCodec(object):
    def encode(self, key, inp):
        return inp.encode()

    def decode(self, key, inp):
        return inp.decode()

class TextbookCodec(object):
    def encode(self, key, inp):
        inp = [i - 54 for i in inp.upper().encode()]
        if key.private:
            chunked = [0]
            pairs = math.ceil(math.log10(key.public.m)) // 2
            count = 0
            for i in inp:
                if count == pairs:
                    chunked.append(0)
                    count = 0
                count += 1
                chunked[-1] = chunked[-1] * 100 + i
            return chunked
        return inp

    def decode(self, key, inp):
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
            single = []#.clear()

        print(split)
        return bytes([i + 54 for i in split]).decode()


def annotate_keys(args, func):
    pass

def decrypt_textbook_cb(args):
    keypair = KeyPair(PublicKey(m=args.p*args.q, k=args.k), PrivateKey(p=args.p, q=args.q))
    #print(TextbookCodec().decode(keypair, keypair.decrypt([1462650632049224168747551860187478964, 2778703796312483352601150489152774249,
    # 1306528860293963680734987464418675979, 308829833051744270798743419251435671, 4596053780976559406683144310229292193])))
    codec = TextbookCodec()
    print("Decoded: %s" % codec.decode(keypair, keypair.decrypt(args.numbers)))

def encrypt_textbook_cb(args):
    keypair = KeyPair(PublicKey(m=args.p*args.q, k=args.k), PrivateKey(p=args.p, q=args.q))
    codec = TextbookCodec()
    print(codec.encode(keypair, "".join(args.message)))
    print("Encoded: %s" % keypair.encrypt(codec.encode(keypair, "".join(args.message))))

def gen_key_cb(args):
    keypair = KeyPair.random_key(args.len)
    print("p=%d, q=%d, k=%d" % (keypair.private.p, keypair.private.q, keypair.public.k))



if __name__ == "__main__":
    #ch18_1_test()
    #decode_josh()
    #exit()
    import argparse
    parser = argparse.ArgumentParser(description="Encryption program")

    def add_key_args(subcommand):
        subcommand.add_argument("--pubkey")
        subcommand.add_argument("--privkey")

    subs = parser.add_subparsers()
    gen_keys = subs.add_parser("gen-key", aliases=["gk"])
    gen_keys.add_argument("len", type=int)
    gen_keys.set_defaults(func=gen_key_cb)

    decrypt_textbook = subs.add_parser("decrypt-textbook", aliases=["dt"], description="Decrypt using textbook algorithm")
    decrypt_textbook.add_argument("k", type=int)
    decrypt_textbook.add_argument("p", type=int)
    decrypt_textbook.add_argument("q", type=int)
    decrypt_textbook.add_argument("numbers", nargs="+", type=int)
    decrypt_textbook.set_defaults(func=decrypt_textbook_cb)

    encrypt_textbook = subs.add_parser("encrypt-textbook", aliases=["et"], description="Encrypt using textbook algorithm")
    encrypt_textbook.add_argument("k", type=int)
    encrypt_textbook.add_argument("p", type=int)
    encrypt_textbook.add_argument("q", type=int)
    encrypt_textbook.add_argument("message", nargs="+")
    encrypt_textbook.set_defaults(func=encrypt_textbook_cb)

    args = parser.parse_args()
    if not hasattr(args, "func"):
        print("A subcommand must be specified!")
        parser.print_help()
        exit(1)
    args.func(args)

# key: m=p*q, k,
# break up message into dicits less than m
#  use seggessive squaring to compute a_n^k modm these large numbers form b1, b2, br

# decode:
# compute phi(m) (we know the factorization
# solve with roots --
