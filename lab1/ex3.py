__author__ = 'Olexandr'


class VigenereCipher:
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, word):
        key_line = self.make_key_line(len(word))
        new_word = []
        for w, k in zip(word, key_line):
            new_index = (self.alphabet.index(w) + self.alphabet.index(k)) % len(self.alphabet)
            new_word.append(self.alphabet[new_index])
        return "".join(new_word)

    def decode(self, word):
        key_line = self.make_key_line(len(word))
        new_word = []
        for w, k in zip(word, key_line):
            new_index = (self.alphabet.index(w) - self.alphabet.index(k)) % len(self.alphabet)
            new_word.append(self.alphabet[new_index])
        return "".join(new_word)

    def make_key_line(self, length):
        a, b = divmod(length, len(self.key))
        return self.key * a + self.key[:b]


def main():
    key = "MATHTERM"
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    encoded = "ZOGPGZVDFIUSXQRFDIQ"
    decoded = "NONINVERTIBLEMATRIX"
    vigenere = VigenereCipher(key, alphabet)
    print(encoded + " = " + vigenere.decode(encoded))
    print(decoded + " = " + vigenere.encode(decoded))


if __name__ == '__main__':
    main()