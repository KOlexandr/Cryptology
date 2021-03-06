from lab1.inverse import inverse_x

__author__ = 'Olexandr'


def gen_pseudo_random(a, c, m, x_0, n):
    # Генерує перші n членів послідовності
    # x_n+1 = a*x_n + c (mod m), починаючи з x_0
    assert n > 0  # вважаємо, що n більше 0
    pseudo_list = [x_0]
    for i in range(n):
        x_0 = (a*x_0 + c) % m
        pseudo_list += [x_0]
    return pseudo_list


x_0_6 = [2147483769, 2175910232, 4134845115, 1318263442, 1999771405, 769052060, 3994265071]

# a * 2147483769 + c (mod 2^32) = 2175910232 => a * x_0_6[0] + c (mod 2^32) = x_0_6[1]
# a * 2175910232 + c (mod 2^32) = 4134845115 => a * x_0_6[1] + c (mod 2^32) = x_0_6[2]

# c (mod 2^32) = x_0_6[1] - a * x_0_6[0]
# c (mod 2^32) = x_0_6[2] - a * x_0_6[1]

# x_0_6[1] - a * x_0_6[0] = x_0_6[2] - a * x_0_6[1]
# a * x_0_6[1] - a * x_0_6[0] = x_0_6[2] - x_0_6[1]
# a * (x_0_6[1] - x_0_6[0]) = x_0_6[2] - x_0_6[1]


mod_2_32 = 2 ** 32
q1 = (x_0_6[2] - x_0_6[1]) % mod_2_32
q2 = (x_0_6[1] - x_0_6[0]) % mod_2_32
a = (q1 * inverse_x(q2, mod_2_32)) % mod_2_32

# c (mod 2^32) = x_0_6[1] - a * x_0_6[0] => c = x_0_6[1] - a * x_0_6[0] (mod 2^32)
c = (x_0_6[1] - (a * x_0_6[0]) % mod_2_32) % mod_2_32

print(gen_pseudo_random(a, c, mod_2_32, x_0_6[0], 7))