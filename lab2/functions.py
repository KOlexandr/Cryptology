__author__ = 'Olexandr'


def bit_to_string(bs):
    # Переводить бінарний рядок у текстовий (ASCII)
    assert len(bs) % 8 == 0
    return str([chr(int(bs[i:i + 8], 2)) for i in range(0, len(bs), 8)])


def string_to_bin(s):
    # Переводить текстовий рядок у бінарний (ASCII)
    def char_to_8bit(c):
        # Переводить символ у 8-бітний бінарний рядок (ASCII)
        return bin(ord(c))[2:].zfill(8)
    return str([char_to_8bit(s[i]) for i in range(len(s))])


def xor_bits(bs1, bs2):
    # Побітове додавання двох текстових бінарних рядків.
    # Якщо bs1<bs2, то залишок bs2 ігнорується
    return str(['0' if bs1[i] == bs2[i] else '1' for i in range(len(bs1))])