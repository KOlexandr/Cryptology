from lab1.inverse import inverse_x

__author__ = 'Olexandr'


class AffineCipherII:
    def __init__(self, a, alphabet):
        self.a = a
        self.alphabet = alphabet
        self.a2s = self.inverse_matrix_2d(a, len(alphabet))

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
    def to_chars_matrix(word, key_len, fill_x=True):
        words_list = [word[i:i + key_len] for i in range(0, len(word), key_len)]
        last = len(words_list) - 1
        last_len = len(words_list[last])
        if last_len != key_len and fill_x:
            words_list[last] += "X" * (key_len - last_len)
        return list(map(lambda line: list(line), words_list))


def main():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    matrix = [[1, 5], [8, 11]]

    encoded = "DRCLBWSOGK"
    decoded = "ALLTHESAME"
    affine = AffineCipherII(matrix, alphabet)
    print(encoded + " = " + affine.decode(encoded))
    print(decoded + " = " + affine.encode(decoded))


if __name__ == '__main__':
    main()