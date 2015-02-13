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

        mapping = list(map(lambda char: (self.alphabet.index(char), self.key.index(char)), self.key))
        mapping.sort(key=lambda t: t[0])
        for i in range(len(mapping)):
            mapping[i] = (i, mapping[i][1])
        mapping.sort(key=lambda t: t[1])
        fmap = list(map(lambda t: t[0], mapping))

        (i, j) = divmod(len(word), len(self.key))
        m_len = i + 1 if j != 0 else i
        matrix = [list(word[i:i + m_len]) for i in range(0, len(word), m_len)]
        if len(word) % len(self.key) != 0:
            exp_max = int(len(word) / len(self.key)) + 1
            exp_min = int(len(word) / len(self.key))
            letters = self.key[:len(word) % len(self.key) - 1:-1]
            tmp_word = ''
            for l in sorted(self.key):
                if l in letters:
                    count = exp_min
                    tmp_word += word[:count] + 'X'
                else:
                    count = exp_max
                    tmp_word += word[:count]
                word = word[count:]
            return self.decode(tmp_word)
        else:
            sort_m = [matrix[val] for val in fmap]
            return self.join2d(self.transposed(sort_m))

    def to_key_chars_matrix(self, word):
        key_len = len(self.key)
        words_list = [word[i:i + key_len] for i in range(0, len(word), key_len)]
        last = len(words_list) - 1
        last_len = len(words_list[last])
        if last_len != key_len:
            words_list[last] += "X" * (key_len - last_len)
        return list(map(lambda line: list(line), words_list))

    @staticmethod
    def transposed(lists):
        if not lists:
            return []
        return list(map(lambda *row: list(row), *lists))

    @staticmethod
    def join2d(lists):
        return "".join(map("".join, lists))

    @staticmethod
    def fix_length(matrix, diff):
        key_len, m_len = len(matrix), len(matrix[0])
        md = MatrixCodeBypass.join2d(matrix[key_len - diff::])
        return matrix[0:key_len - diff] + [list(md[i:i + m_len - 1]) + ["X"] for i in range(0, len(md), m_len - 1)]


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