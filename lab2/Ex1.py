from lab1.inverse import inverse_x

__author__ = 'Olexandr'


class AffineCipher:
    def __init__(self, a, s, alphabet):
        """
        text – повідомлення;
        crypto – зашифроване повідомлення
        :param a, :param s: keys for monogram affine cipher
        :param alphabet: alphabet
        """
        self.a = a
        self.s = s
        self.a_1 = inverse_x(a, len(alphabet))
        self.s_1 = (-self.a_1 * s) % len(alphabet)
        self.alphabet = alphabet.lower()

    def encode(self, word):
        """
        :param word: input open message
        :return: encrypted input message
        """
        new_word = []
        for w in word.lower():
            new_letter_idx = (self.a * self.alphabet.index(w) + self.s) % len(self.alphabet)
            new_word.append(self.alphabet[new_letter_idx])
        return "".join(new_word)

    def decode(self, word):
        """
        :param word: input encrypted message
        :return: decrypted input message
        """
        new_word = []
        for w in word.lower():
            new_letter_idx = (self.a_1 * self.alphabet.index(w) + self.s_1) % len(self.alphabet)
            new_word.append(self.alphabet[new_letter_idx])
        return "".join(new_word)


def main():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    encoded = "LIHXTCJQOTGWDI"
    decoded = "CLOSEDINTERVAL"
    affine = AffineCipher(17, 3, alphabet)
    print(encoded + " = " + affine.decode(encoded))
    print(decoded + " = " + affine.encode(decoded))


if __name__ == '__main__':
    main()