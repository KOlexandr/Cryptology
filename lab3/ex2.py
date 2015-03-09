from lab3.inverse import inverse_x

__author__ = 'Olexandr'


class RSA:
    def __init__(self, p, q, e, alphabet):
        self.p = p
        self.q = q
        self.e = e
        self.n = p*q
        self.d = self.find_d()
        self.alphabet = alphabet
        self.block_len = len(str(self.n))
        self.char_len = len(str(len(self.alphabet)))

    def encode(self, word):
        codes_line = "".join(map(lambda char: str(self.alphabet.index(char)).zfill(self.char_len), list(word)))
        codes = [int(codes_line[i:i + self.block_len]) for i in range(0, len(codes_line), self.block_len)]
        return "".join(map(lambda code: str((code**self.e) % self.n).zfill(self.block_len), codes))

    def decode(self, word):
        char_codes = [int(word[i:i + self.block_len]) for i in range(0, len(word), self.block_len)]
        codes = "".join(map(lambda code: str((code**self.d) % self.n), char_codes))
        new_char_codes = [int(codes[i:i + self.char_len]) for i in range(0, len(codes), self.char_len)]
        return "".join(map(lambda code: self.alphabet[code], new_char_codes))

    def phi(self):
        return self.n - self.p - self.q + 1

    def find_d(self):
        return inverse_x(self.e, self.phi())


def main():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encoded = "036612260255"
    decoded = "RIVEST"
    rsa = RSA(53, 61, 23, alphabet)
    print(encoded + " = " + rsa.decode(encoded))
    print(decoded + " = " + rsa.encode(decoded))


if __name__ == '__main__':
    main()
