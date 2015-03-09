from gmpy2 import powmod
from lab3.ex3 import sqr, sqrt
from lab3.inverse import inverse_x

__author__ = 'Olexandr'


class Rabin:
    def __init__(self, p, q, alphabet):
        self.p = p
        self.q = q
        self.n = p * q
        self.alphabet = alphabet
        self.block_len = 4
        self.char_len = len(str(len(alphabet)))

    def decode(self, word):
        words = []
        blocks = [int(word[i:i + self.block_len]) for i in range(0, len(word), self.block_len)]
        for block in blocks:
            q11, q12 = self.sqrt_v1(self.q, block)
            q21, q22 = self.sqrt_v2(self.q, block)

            p11, p12 = self.sqrt_v1(self.p, block)
            p21, p22 = self.sqrt_v2(self.p, block)
            q = 0
            # x1, x2, x3, x4 = sqrt(self.p, self.q, int(block))
            # words.append((block, self.decode_one(x1)))
            # words.append((block, self.decode_one(x2)))
            # words.append((block, self.decode_one(x3)))
            # words.append((block, self.decode_one(x4)))
        return str(words)

    def decode_one(self, x):
        chars = [int(str(x).zfill(self.block_len)[i:i + self.char_len]) for i in range(0, self.block_len, self.char_len)]
        if len(list(filter(lambda code: code < len(self.alphabet), chars))) == 2:
            return "".join(map(lambda code: self.alphabet[code], chars))
        else:
            return ""

    def encode(self, word):
        code_str = "".join(map(lambda char: str(self.alphabet.index(char)).zfill(self.char_len), list(word)))
        blocks = [int(code_str[i:i + self.block_len]) for i in range(0, len(code_str), self.block_len)]
        return "".join(map(lambda block: str(sqr(int(block), 2, self.n)).zfill(self.block_len), blocks))

    @staticmethod
    def sqrt_v1(p, x):
        m = p - 3 * inverse_x(4, p)
        y = int(powmod(x, m + 1, p))
        return y, p - y

    @staticmethod
    def sqrt_v2(p, x):
        m = p - 5 * inverse_x(8, p)
        q = powmod(x, 2 * m + 1, p)
        y = (int(powmod(x, m + 1, p)) * int(powmod(2, 2*m + 1, p))) % p
        return y, p - y


def main():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # encoded = "21672351"
    encoded = "1497"
    decoded = ""
    # rabin = Rabin(67, 71, alphabet)
    rabin = Rabin(53, 67, alphabet)
    print(encoded + " = " + rabin.decode(encoded))
    print(decoded + " = " + rabin.encode(decoded))


if __name__ == '__main__':
    main()