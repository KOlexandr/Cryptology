from gmpy2 import powmod

__author__ = 'Olexandr'


def primitive_root(p):
    return [n for n in range(1, p) if len(set([int(powmod(n, power, p)) for power in range(p - 1)])) == p - 1]


def main():
    numbers = [11, 13]
    for val in numbers:
        print(str(val) + " : " + ", ".join(map(str, primitive_root(val))))


if __name__ == '__main__':
    main()