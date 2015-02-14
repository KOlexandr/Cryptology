__author__ = 'Olexandr'


def extended_euclidean_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_euclidean_algorithm(b, a % b)
        return d, y, x - int(a / b) * y


def inverse_x(x, mod):
    d, x_1, y = extended_euclidean_algorithm(x, mod)
    return x_1 if x_1 >= 0 else mod + x_1