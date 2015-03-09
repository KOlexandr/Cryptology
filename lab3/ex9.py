from gmpy2 import powmod, invert
from lab3.ex8 import find_p_q

__author__ = 'Olexandr'


class RSA:
    def __init__(self, n, e):
        self.e = e
        self.n = n
        self.p, self.q = find_p_q(n)
        self.d = self.find_d()

    def encode(self, word):
        return int(powmod(self.string_to_dec(word), self.e, self.n))

    def decode(self, word):
        return self.dec_to_string(int(powmod(word, self.d, self.n)))

    def phi(self):
        return self.n - self.p - self.q + 1

    def find_d(self):
        return int(invert(self.e, self.phi()))

    @staticmethod
    def string_to_dec(s):
        # Переводить текстовий рядок у десяткове число
        def char_to_8bit(c):
            # Переводить символ у 8-бітний бінарний рядок (ASCII)
            return bin(ord(c))[2:].zfill(8)

        bs = ''
        for i in range(len(s)):
            bs += char_to_8bit(s[i])
        return int(bs, 2)

    @staticmethod
    def dec_to_string(ds):
        # Переводить десяткове число у текстовий рядок
        bs = bin(ds)[2:]
        bs = bs.zfill(len(bs) + (8 - (len(bs) % 8)))
        s = ''
        for i in range(0, len(bs), 8):
            s += chr(int(bs[i:i + 8], 2))
        return s


def main():
    m = "Winter is coming"
    c = 1369617520343736604681509545987401107472610213155449180224072143018640110640406921298600588205501186
    n = 2155521117027243630973823963847695675142648931978141801990016117470096232504563101608940380959903957
    e = 65537
    rsa = RSA(n, e)
    print(str(c) + " = " + str(rsa.decode(c)))
    print(m + " = " + str(rsa.encode(m)))


if __name__ == '__main__':
    main()
