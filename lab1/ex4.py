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
        mapping.sort(key=lambda t: t[0])
        fmap = list(map(lambda t: t[1], mapping))

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
        matrix = self.to_chars_matrix(word, m_len, False)

        mapping = list(map(lambda char: (self.alphabet.index(char), self.key.index(char)), self.key))
        mapping.sort(key=lambda t: t[0])
        for i in range(len(mapping)):
            mapping[i] = (i, mapping[i][1])
        mapping.sort(key=lambda t: t[1])
        fmap = list(map(lambda t: t[0], mapping))

        return "".join(map("".join, self.transposed([matrix[val] for val in fmap])))

    def to_key_chars_matrix(self, word):
        return self.to_chars_matrix(word, len(self.key))

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
    key = "PERMUT"
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    encoded = "AANELIHXCHORYMTMYTOXELEX"
    decoded = "CAYLEYHAMILTONTHEOREM"
    bypass = MatrixCodeBypass(key, alphabet)
    print(encoded + " = " + bypass.decode(encoded))
    print(decoded + " = " + bypass.encode(decoded))


if __name__ == '__main__':
    main()