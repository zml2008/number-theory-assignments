__author__ = 'zml'

import math
import numpy
from util import gathering_input, factors


@gathering_input("Factorial of:")
def ex1a(num):
    print("lib func is: ", math.factorial(num))
    print("custom_factorial(%d)=%d" % (num, custom_factorial(num)))


def custom_factorial(num):
    ret = 1
    for i in range(num, 0, -1):
        ret *= i
    return ret


@gathering_input
def ex2(num):
    print(num % 120 == 0)


@gathering_input
def ex3(num):
    res = "odd"
    if num % 2 == 0:
        res = "even"

    print("%d is %s" % (num, res))


def ex4():
    num = int(input("Is number: "))
    fact = int(input("a factor of: "))
    print(num % fact)


def ex5():
    print(factors(120))


@gathering_input("Factors of: ")
def ex6(num):
    print(factors(num))


@gathering_input("Is prime: ")
def ex7(num):
    print(len(factors(num)) == 2)


def is_perfect(num):
    return sum(factors(num)[0:-1]) == num


@gathering_input("Is number perfect: ")
def ex8a(num):
    perfect = sum(factors(num)[0:-1]) == num
    print(perfect)


@gathering_input("Perfect numbers less than: ")
def ex8b(num):
    perfect_nums = filter(is_perfect, range(1, num))
    for i in perfect_nums:
        print(i)


def is_square(num):
    rooted = math.sqrt(num)
    return rooted == math.floor(rooted)


def is_triangular(num):
    rooted = (math.sqrt((8 * num) + 1) - 1)/2.0
    return rooted == math.floor(rooted)


def is_triangular_old(num):
    tri_val = 0

    for i in range(0, num):
        if tri_val >= num:
            break
        tri_val += i
    return tri_val == num


def ex9():
    num = 0
    while True:
        if is_square(num) and is_triangular(num):
            print(num)
        num += 1


def subintervals(start, end, steps):
    acc = start
    step = (end-start)/float(steps)
    while acc <= end:
        yield acc
        acc += step


def ex10():
    # Trying a different thing
    vals = numpy.linspace(2 * math.pi, 4 * math.pi, 9)
    results = numpy.column_stack((vals, numpy.cos(vals)))
    print(results)
