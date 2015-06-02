
from congruence import congruencies

ALPHA_PREFIX=65

ENGLISH_FREQUENCIES = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

def enshift(string, a, k):
    return bytes([((a * (i - ALPHA_PREFIX) + k)% 26) + ALPHA_PREFIX for i in string.upper().encode()]).decode()

def deshift(string, a, k):
    return bytes([(int(congruencies(a, i - ALPHA_PREFIX - k, 26)[0] % 26)) + ALPHA_PREFIX for i in string.upper().encode()]).decode()

def frequencies(string):
    ret = {}
    for i in string:
        ret[i] = ret.get(i, 0) + 1
    return ret

def fixed_chars(a, k):
    ret = []
    for i in range (0, 26):
        #print("checking", chr(i + ALPHA_PREFIX))
        if (((a * i) + k) % 26) == i:
            ret.append(chr(i + ALPHA_PREFIX))
    return ret

def guess_frequencies(string):
    freqs = list(frequencies(string).items())
    freqs.sort(key=lambda ent: ent[1], reverse=True)
    print(freqs)

    freqs = [k for k, v in freqs]
    mapped = [(freqs[i], ENGLISH_FREQUENCIES[i]) for i in range(0, min(len(freqs), len(ENGLISH_FREQUENCIES)))]
    print(freqs)
    print(mapped)

