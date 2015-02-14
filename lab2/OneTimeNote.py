__author__ = 'Olexandr'


class OneTimeNote:
    def __init__(self, key):
        self.key = key

    def encode(self, word, bits=True):
        if bits:
            return self.bit_to_string(self.xor_bits(word, self.key))
        else:
            return self.bit_to_string(self.xor_bits(self.string_to_bin(word), self.key))

    def decode(self, word, bits=True):
        return self.encode(word, bits)

    @staticmethod
    def bit_to_string(bs):
        # Переводить бінарний рядок у текстовий (ASCII)
        assert len(bs) % 8 == 0
        s = ''
        for i in range(0, len(bs), 8):
            s += chr(int(bs[i:i + 8], 2))
        return s

    @staticmethod
    def string_to_bin(s):
        # Переводить текстовий рядок у бінарний (ASCII)
        def char_to_8bit(c):
            # Переводить символ у 8-бітний бінарний рядок (ASCII)
            return bin(ord(c))[2:].zfill(8)

        bs = ''
        for i in range(len(s)):
            bs += char_to_8bit(s[i])
        return bs

    @staticmethod
    def xor_bits(bs1, bs2):
        # Побітове додавання двох текстових бінарних рядків.
        # Якщо bs1<bs2, то залишок bs2 ігнорується
        bs = ''
        for i in range(len(bs1)):
            if bs1[i] == bs2[i]:
                bs += '0'
            else:
                bs += '1'
        return bs