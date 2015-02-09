from numpy.core.multiarray import zeros
from lab1.inverse import inverse_x

__author__ = 'Olexandr'


class AffineCipherII:
    def __init__(self, decoded, encoded, alphabet):
        self.decoded = decoded
        self.encoded = encoded
        self.alphabet = alphabet
        self.a2s = self.find_a2s(decoded, encoded, alphabet)
        self.a = self.inverse_matrix_2d(self.a2s, len(alphabet))

    def encode(self, word):
        if not word or len(word) == 0:
            return ""

        len_2d = len(self.alphabet)
        chars_matrix = self.to_chars_matrix(word, len(self.a))
        x = list(map(lambda line: list(map(lambda c: self.alphabet.index(c), line)), chars_matrix))
        new_word = []
        for vector in x:
            new_word.append(self.alphabet[(self.a[0][0] * vector[0] + self.a[0][1] * vector[1]) % len_2d])
            new_word.append(self.alphabet[(self.a[1][0] * vector[0] + self.a[1][1] * vector[1]) % len_2d])
        return "".join(new_word)

    def decode(self, word):
        if not word or len(word) == 0:
            return ""

        len_2d = len(self.alphabet)
        chars_matrix = self.to_chars_matrix(word, len(self.a2s))
        x = list(map(lambda line: list(map(lambda c: self.alphabet.index(c), line)), chars_matrix))
        new_word = []
        for vector in x:
            new_word.append(self.alphabet[(self.a2s[0][0] * vector[0] + self.a2s[0][1] * vector[1]) % len_2d])
            new_word.append(self.alphabet[(self.a2s[1][0] * vector[0] + self.a2s[1][1] * vector[1]) % len_2d])
        return "".join(new_word)

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
    def find_a2s(decoded, encoded, alphabet):
        d = AffineCipherII.transposed(AffineCipherII.to_chars_matrix(decoded, 2))
        e = AffineCipherII.transposed(AffineCipherII.to_chars_matrix(encoded, 2))

        dcodes = list(map(lambda l: list(map(lambda x: alphabet.index(x), l)), d))
        ecodes = list(map(lambda l: list(map(lambda x: alphabet.index(x), l)), e))

        length = len(alphabet)
        return AffineCipherII.multiply_matrices(dcodes, AffineCipherII.inverse_matrix_2d(ecodes, length), length)

    @staticmethod
    def multiply_matrices(a, b, n):
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
    def transposed(lists):
        if not lists:
            return []
        return list(map(lambda *row: list(row), *lists))


def main():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    encoded = "FHYSYSZQZVAWLRCX"
    decoded = "THISISHILLCIPHER"
    affine = AffineCipherII("PHER", "LRCX", alphabet)
    print(encoded + " = " + affine.decode(encoded))
    print(decoded + " = " + affine.encode(decoded))


if __name__ == '__main__':
    main()