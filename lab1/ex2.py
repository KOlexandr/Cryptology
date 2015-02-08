__author__ = 'Olexandr'


class CaesarCipher:
    def __init__(self, shift, alphabet):
        self.shift = shift
        self.alphabet = alphabet

    def encode(self, word):
        new_word = []
        for i in word:
            new_index = (self.alphabet.index(i) + self.shift) % len(self.alphabet)
            new_word.append(self.alphabet[new_index])
        return "".join(new_word)

    def decode(self, word):
        new_word = []
        for i in word:
            new_index = (self.alphabet.index(i) - self.shift) % len(self.alphabet)
            new_word.append(self.alphabet[new_index])
        return "".join(new_word)


def main():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    encoded = "TXDGUDWLFSROBQRPLDO"
    decoded = "QUADRATICPOLYNOMIAL"
    caesar = CaesarCipher(3, alphabet)
    print(encoded + " = " + caesar.decode(encoded))
    print(decoded + " = " + caesar.encode(decoded))


if __name__ == '__main__':
    main()