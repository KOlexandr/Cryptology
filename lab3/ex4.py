from gmpy2 import powmod
from lab3.ex3 import sqr
from lab3.inverse import extended_euclidean_algorithm

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
        blocks = [int(word[i:i + self.block_len]) for i in range(0, len(word), self.block_len)]
        x = [set(map(lambda val: str(val).zfill(self.block_len), self.sqrt(self.p, self.q, block))) for block in blocks]
        possible = []
        sub_words = [self.decode_one(val) for val in x]
        for w in sub_words:
            if len(possible) == 0:
                possible = w
            else:
                tmp = []
                for wi in w:
                    for pos in possible:
                        tmp.append(pos + wi)
                possible = tmp
        return list(map(lambda v: "".join(v), possible))

    def decode_one(self, x):
        sub_words = []
        for val in x:
            char_codes = [int(val[i:i + self.char_len]) for i in range(0, self.block_len, self.char_len)]
            if len(list(filter(lambda code: code < len(self.alphabet), char_codes))) == 2:
                sub_words.append("".join(map(lambda code: self.alphabet[code], char_codes)))
        return sub_words

    def encode(self, word):
        code_str = "".join(map(lambda char: str(self.alphabet.index(char)).zfill(self.char_len), list(word)))
        blocks = [int(code_str[i:i + self.block_len]) for i in range(0, len(code_str), self.block_len)]
        return "".join(map(lambda block: str(sqr(self.p, self.q, int(block))).zfill(self.block_len), blocks))

    @staticmethod
    def sqrt_complex(p, x):
        if (p - 3) % 4 == 0:
            y = Rabin.sqrt_v1(p, x)
        elif (p - 5) % 8 == 0:
            y = Rabin.sqrt_v2(p, x)
        else:
            y = None
        return y

    @staticmethod
    def sqrt(p, q, x):
        x1, x2 = x % p, x % q
        y1 = Rabin.sqrt_complex(p, x1)
        y2 = Rabin.sqrt_complex(q, x2)

        de, u, v = extended_euclidean_algorithm(p, q)
        pairs = [(y1, y2), (-y1, y2), (y1, -y2), (-y1, -y2)]
        return [(pair[1] * p * u + pair[0] * q * v) % (q * p) for pair in pairs]

    @staticmethod
    def sqrt_v1(p, x):
        m = int((p - 3) / 4)
        y = int(powmod(x, m + 1, p))
        return y % p

    @staticmethod
    def sqrt_v2(p, x):
        m = int((p - 5) / 8)
        if powmod(x, 2 * m + 1, p) == 1:
            y = int(powmod(x, m + 1, p))
        else:
            y = int(powmod(x, m + 1, p) * powmod(2, 2 * m + 1, p))
        return y % p


def main():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    encoded = "21672351"
    # encoded = "1497"
    decoded = "NEXT"
    rabin = Rabin(67, 71, alphabet)
    # rabin = Rabin(53, 67, alphabet)

    print(encoded + " = " + str(rabin.decode(encoded)))
    print(decoded + " = " + rabin.encode(decoded))


if __name__ == '__main__':
    main()