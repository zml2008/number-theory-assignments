
from .shift import *
ALPHA_PREFIX=65

def enceasar(string):
    return enshift(string, 1, 3)
    #return bytes([((i - ALPHA_PREFIX + 3) % 26) + ALPHA_PREFIX for i in string.encode()]).decode()

def deceasar(string):
    return deshift(string, 1, 3)
    #return bytes([((i - ALPHA_PREFIX - 3) % 26) + ALPHA_PREFIX for i in string.encode()]).decode()
