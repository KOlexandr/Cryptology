from math import floor, sqrt

__author__ = 'Olexandr'


def is_square(num):
    x = sqrt(num)
    return x == floor(x)


# q = p + 2*d; n + d^2 = (p + d)^2
# t^2 > 0 if t^2 - n is square
# t^2 + d^2 - 2*d^2 = n
# t**2 - d^2 = n -> sqrt(t^2 - n) = d
def find_p_q(n):
    t = floor(sqrt(n)) + 1
    while not is_square(t**2 - n):
        t += 1
    d = sqrt(t**2 - n)
    return int(t - d), int(t + d)


def main():
    n = 3028190057
    p, q = find_p_q(n)
    print("p = " + str(p) + ", q = " + str(q) + ", n = " + str(n) + ", p*q = " + str(p*q))


if __name__ == '__main__':
    main()