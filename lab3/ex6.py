from lab3.inverse import inverse_x

__author__ = 'Olexandr'


class ElGamal:
    def __init__(self, p, g, a, alphabet):
        self.p = p
        self.g = g
        self.a = a
        self.h = (g ** a) % p
        self.alphabet = alphabet
        self.block_len = len(str(self.p))
        self.char_len = len(str(len(self.alphabet)))

    def decode(self, encoded):
        encoded = "".join(map(lambda c: str(self.decode_one(c)).zfill(self.block_len), encoded))
        codes = [int(encoded[i:i + self.char_len]) for i in range(0, len(encoded), self.char_len)]
        return "".join(map(lambda code: self.alphabet[code], codes))

    def decode_one(self, c):
        return (c[1] * inverse_x(c[0] ** self.a, self.p)) % self.p


def main():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encoded = [(1062, 814), (3034, 1172)]
    eg = ElGamal(4519, 37, 23, alphabet)
    print(str(encoded) + " = " + eg.decode(encoded))


if __name__ == '__main__':
    main()
