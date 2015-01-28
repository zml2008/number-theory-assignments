def a(s, t):
    return s * t


def b(s, t):
    return ((s * s) - (t * t))/2


def c(s, t):
    return ((s * s) + (t * t))/2

def no_shared_factors(s, t):
    for i in range(2, min(s, t) + 1):
        if s % i == 0 and t % i == 0:
            return False
    return True

def print_ppts():
    max_s = int(input("Maximum s value: "))
    count = 0
    for s in range (1, max_s + 1, 2):
        for t in range(1, s, 2):
            if no_shared_factors(s, t):
                count += 1
                print((s, t, a(s, t), b(s, t), c(s, t)))
    print("Total number of PPTs:", count)

if __name__ == "__main__":
    print_ppts()
