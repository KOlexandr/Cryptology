from lab3.inverse import extended_euclidean_algorithm

__author__ = 'Olexandr'


def sqrt(p, q, x):
    x1, x2 = x % p, x % q
    y1 = (x1 ** ((p - 3) / 4 + 1)) % p
    y2 = (x2 ** ((q - 3) / 4 + 1)) % q

    de, xe, ye = extended_euclidean_algorithm(p, q)
    n = int(p * q)
    y = int((y1 * q * ye + y2 * p * xe) % n)
    ys = int((-y1 * q * ye + y2 * p * xe) % n)
    return y, ys, n - y, n - ys


def sqr(p, q, x):
    return (x * x) % (p * q)


def main():
    p, q, x = 11, 19, 191
    y = 20
    print("sqrt(" + str(x) + ") mod (" + str(p * q) + ") = " + str(sqrt(p, q, x)))
    print("sqr(" + str(y) + ") mod (" + str(p * q) + ") = " + str(sqr(p, q, y)))


if __name__ == '__main__':
    main()