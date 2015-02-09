from numpy.core.multiarray import zeros
from lab1.inverse import inverse_x

__author__ = 'Olexandr'


class AffineCipherTest:
    @staticmethod
    def inverse_matrix_2d(matrix, n):
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[1][0]
        d = matrix[1][1]
        w_1 = inverse_x(a * d - b * c, n)
        return [
            [(d * w_1) % n, (-b * w_1) % n],
            [(-c * w_1) % n, (a * w_1) % n]
        ]

    @staticmethod
    def multiply(a, b, n):
        size = len(a)
        out = zeros((size, size))
        for i in range(size):
            for j in range(size):
                line_sum = 0
                for k in range(size):
                    line_sum += a[i][k] * b[k][j]
                out[i][j] = line_sum % n
        return list(map(lambda row: list(map(int, row)), out))

    @staticmethod
    def to_chars_matrix(word, key_len, fill_x=True):
        words_list = [word[i:i + key_len] for i in range(0, len(word), key_len)]
        last = len(words_list) - 1
        last_len = len(words_list[last])
        if last_len != key_len and fill_x:
            words_list[last] += "X" * (key_len - last_len)
        return list(map(lambda line: list(line), words_list))

    @staticmethod
    def encode(word, alphabet, a):
        if not word or len(word) == 0:
            return ""

        len_2d = len(alphabet)
        chars_matrix = AffineCipherTest.to_chars_matrix(word, len(a))
        x = list(map(lambda line: list(map(lambda c: alphabet.index(c), line)), chars_matrix))
        new_word = []
        for vector in x:
            new_word.append(alphabet[(a[0][0] * vector[0] + a[0][1] * vector[1]) % len_2d])
            new_word.append(alphabet[(a[1][0] * vector[0] + a[1][1] * vector[1]) % len_2d])
        return "".join(new_word)

    @staticmethod
    def decode(word, alphabet, a2s):
        if not word or len(word) == 0:
            return ""

        len_2d = len(alphabet)
        chars_matrix = AffineCipherTest.to_chars_matrix(word, len(a2s))
        x = list(map(lambda line: list(map(lambda c: alphabet.index(c), line)), chars_matrix))
        new_word = []
        for vector in x:
            new_word.append(alphabet[(a2s[0][0] * vector[0] + a2s[0][1] * vector[1]) % len_2d])
            new_word.append(alphabet[(a2s[1][0] * vector[0] + a2s[1][1] * vector[1]) % len_2d])
        return "".join(new_word)

    @staticmethod
    def verify_ith_matrix(matrix, i, j, alphabet, encoded, add):
        matrix[i][j] += add
        print(str(matrix) + " -> " + AffineCipherTest.decode(encoded, alphabet, matrix))


def main():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encoded = "HLNCNMPCMYSQ"
    decoded = "LASTEXERCISE"

    # print(list(map(lambda x: alphabet.index(x), list("CISE"))))
    # print(list(map(lambda x: alphabet.index(x), list("MYSQ"))))

    mod = 13
    r = [[2, 5], [8, 4]]
    a = [[12, 5], [11, 3]]
    d = AffineCipherTest.inverse_matrix_2d(a, mod)

    for i in range(2):
        for j in range(2):
            AffineCipherTest.verify_ith_matrix(
                AffineCipherTest.multiply(r, d, mod),
                i, j, alphabet, encoded, mod
            )

    a = [[6, 9], [25, 3]]
    print(encoded + " = " + AffineCipherTest.decode(encoded, alphabet, a))
    print(decoded + " = " + AffineCipherTest.encode(decoded, alphabet, a))

if __name__ == '__main__':
    main()