from lab1.inverse import inverse_x

__author__ = 'Olexandr'


class AffineCipherI:
    def __init__(self, a, s, alphabet):
        self.a = a
        self.s = s
        self.a_1 = inverse_x(a, len(alphabet))
        self.s_1 = (-self.a_1 * s) % len(alphabet)
        self.alphabet = alphabet

    def encode(self, word):
        new_word = []
        for w in word:
            new_letter_idx = (self.a * self.alphabet.index(w) + self.s) % len(self.alphabet)
            new_word.append(self.alphabet[new_letter_idx])
        return "".join(new_word)

    def decode(self, word):
        new_word = []
        for w in word:
            new_letter_idx = (self.a_1 * self.alphabet.index(w) + self.s_1) % len(self.alphabet)
            new_word.append(self.alphabet[new_letter_idx])
        return "".join(new_word)


def main():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    encoded = "LIHXTCJQOTGWDI"
    decoded = "CLOSEDINTERVAL"
    affine = AffineCipherI(17, 3, alphabet)
    print(encoded + " = " + affine.decode(encoded))
    print(decoded + " = " + affine.encode(decoded))


if __name__ == '__main__':
    main()