from lab1.ex4 import MatrixCodeBypass

__author__ = 'Olexandr'


class ADFGVXCipher:
    def __init__(self, matrix, encoder_decoder):
        self.key = list("ADFGVX")
        self.matrix = matrix
        self.encoder_decoder = encoder_decoder

    def encode(self, word):
        if not word or len(word) == 0:
            return ""
        return self.encoder_decoder.encode("".join([self.find_bigram(w) for w in word]))

    def decode(self, word):
        if not word or len(word) == 0:
            return ""
        decoded = self.encoder_decoder.decode(word)
        new_word = []
        for (row, col) in zip(decoded[0::2], decoded[1::2]):
            new_word.append(self.matrix[self.key.index(row)][self.key.index(col)])
        return "".join(new_word)

    def find_bigram(self, character):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == character:
                    return self.key[i] + self.key[j]
        return ""


def main():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    key = "GERMAN"
    matrix = [
        ['R', 'X', 'J', 'O', '0', '9'],
        ['V', 'H', 'E', 'G', '5', 'Y'],
        ['S', 'N', 'W', 'T', 'L', 'I'],
        ['D', 'Z', '1', '3', 'F', '7'],
        ['4', 'Q', 'P', 'M', 'A', 'B'],
        ['2', '8', 'C', 'U', '6', 'K']
    ]

    '''key = "GARDEN"
    matrix = [
        ['C', 'O', '8', 'X', 'F', '4'],
        ['M', 'K', '3', 'A', 'Z', '9'],
        ['N', 'W', 'L', '0', 'J', 'D'],
        ['5', 'S', 'I', 'Y', 'H', 'U'],
        ['P', '1', 'V', 'B', '6', 'R'],
        ['E', 'Q', '7', 'T', '2', 'G']
    ]'''

    encoder_decoder = MatrixCodeBypass(key, alphabet)

    # encoded = "XGGDGFAXDAFVFGDDFGXAFAVFFXXAXFDVAXGVFDXDAVGAGXAA"
    encoded = "FDVDAFAAAADFAFFAFGDFVFDGXF"
    # decoded = "DONTPUTITOFFTILLTOMORROW"
    decoded = "ESLSCERUQS8GSC9"
    cipher = ADFGVXCipher(matrix, encoder_decoder)
    print(encoded + " = " + cipher.decode(encoded))
    print(decoded + " = " + cipher.encode(decoded))


if __name__ == '__main__':
    main()