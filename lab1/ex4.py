from numpy.core.multiarray import zeros

__author__ = 'Olexandr'


class MatrixCodeBypass:
    def __init__(self, key, alphabet):
        self.key = list(key)
        self.alphabet = alphabet

    def encode(self, word):
        if not word or len(word) == 0:
            return ""

        matrix = self.to_key_chars_matrix(word)
        mapping = list(map(lambda char: (self.alphabet.index(char), self.key.index(char)), self.key))
        fmap = list(map(lambda t: t[1], sorted(mapping, key=lambda t: t[0])))

        new_word = []
        for val in fmap:
            for i in range(len(matrix)):
                new_word.append(matrix[i][val])
        return "".join(new_word)

    def decode(self, word):
        if not word or len(word) == 0:
            return ""
        (i, j) = divmod(len(word), len(self.key))
        m_len = i + 1 if j != 0 else i
        matrix = self.to_chars_matrix(word, m_len)

        mapping = list(map(lambda char: (self.alphabet.index(char), self.key.index(char)), self.key))
        mapping.sort(key=lambda t: t[0])
        for i in range(len(mapping)):
            mapping[i] = (i, mapping[i][1])
        mapping.sort(key=lambda t: t[1])
        fmap = list(map(lambda t: t[0], mapping))

        return self.join2d(self.transposed([matrix[val] for val in fmap]))

    def to_key_chars_matrix(self, word):
        key_len = len(self.key)
        words_list = [word[i:i + key_len] for i in range(0, len(word), key_len)]
        last = len(words_list) - 1
        last_len = len(words_list[last])
        if last_len != key_len:
            words_list[last] += "X" * (key_len - last_len)
        return list(map(lambda line: list(line), words_list))

    @staticmethod
    def to_chars_matrix(word, key_len):
        words_list = [word[i:i + key_len] for i in range(0, len(word), key_len)]
        return list(map(lambda line: list(line), words_list))

    @staticmethod
    def transposed(lists):
        if not lists:
            return []
        transposed = list(map(lambda row: list(map(lambda x: 'X', row)), zeros((len(lists[0]), len(lists)))))
        for i in range(len(lists)):
            for j in range(len(lists[i])):
                transposed[j][i] = lists[i][j]
        return transposed

    @staticmethod
    def join2d(lists):
        return "".join(map("".join, lists))


def main():
    key = "PERMUT"
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    encoded = "AANELIHXCHORYMTMYTOXELEX"
    decoded = "CAYLEYHAMILTONTHEOREM"
    bypass = MatrixCodeBypass(key, alphabet)
    print(encoded + " = " + bypass.decode(encoded))
    print(decoded + " = " + bypass.encode(decoded))


if __name__ == '__main__':
    main()