from gmpy2 import isqrt
from math import floor, sqrt

__author__ = 'Olexandr'


def is_square(num):
    x = int(isqrt(num))
    return x ** 2 == num


# q = p + 2*d; n + d^2 = (p + d)^2
# t^2 > 0 if t^2 - n is square
# t^2 + d^2 - 2*d^2 = n
# t**2 - d^2 = n -> sqrt(t^2 - n) = d
def find_p_q(n):
    t = int(isqrt(n)) + 1
    possible_sqr = t ** 2 - n
    while not is_square(possible_sqr):
        t += 1
    d = int(isqrt(possible_sqr))
    return int(t - d), int(t + d)


def main():
    n = 2155521117027243630973823963847695675142648931978141801990016117470096232504563101608940380959903957
    p, q = find_p_q(n)
    print("p = " + str(p) + ", q = " + str(q) + ", n = " + str(n) + ", p*q = " + str(p*q))


if __name__ == '__main__':
    main()