__author__ = 'zml'

from congruence import congruencies, parse_congruency


def solve(*congrs):
    """

    :type congrs: list
    This contains an algorithm for solving an arbitrary number of concurrent congruencies, like so:
    1. initialize p_m to 1 and p_c to 0. define congrs to be a list of 3-tuples (a, c, m) representing a{congr}cmodm
    2. set i = 0
    3. set a, c = a * p_m, c - p_c
    4. set soln to the one solution to the congruency of (a, c, m)
    5. set c to soln % m
    6. if i is the length of congrs - 1, return p_m * c + p_c (stop here)
    7. set p_c = p_c + (p_m * c) # update the multipliers
    8. set p_m = p_m * m
    9. increment i by 1 and go to step 2

    :param args: a series of congruencies in string form
    :return: the x value that solves every input congruence
    """
    if len(congrs) == 0:
        raise BaseException("No input values provided!")

    p_m, p_c = 1, 0
    for i in range(len(congrs)):
        a, c, m = congrs[i]
        a *= p_m
        c -= p_c
        solns = list(congruencies(a, c, m))
        if len(solns) != 1:
            raise BaseException("Invalid length of solutions -- expected 1 but got %d" % len(solns))
        c = solns[0] % m
        if i == len(congrs) - 1:
            return p_m * c + p_c
        p_c += p_m * c
        p_m *= m


def main(args):
    congrs = [parse_congruency(arg) for arg in args]
    ret = solve(*congrs)
    print("Solution is x=%d" % ret)

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
