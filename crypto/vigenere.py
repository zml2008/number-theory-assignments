__author__ = 'zml'

from congruence import congruencies

ALPHA_PREFIX=65

def envigenere(string, key):
    key_bytes = [i - ALPHA_PREFIX for i in key.upper().encode()]
    arr = string.upper().encode()
    return bytes([((arr[i] - ALPHA_PREFIX + key_bytes[i % len(key_bytes)]) % 26) + ALPHA_PREFIX for i in range(0, len(string))]).decode()

def devigenere(string, key):
    key_bytes = [i - ALPHA_PREFIX for i in key.upper().encode()]
    arr = string.upper().encode()
    return bytes([((arr[i] - ALPHA_PREFIX - key_bytes[i % len(key_bytes)]) % 26) + ALPHA_PREFIX for i in range(0, len(string))]).decode()
