from gmpy2 import powmod

__author__ = 'Olexandr'


def bit_to_string(bs):
    # Переводить бінарний рядок у текстовий (ASCII)
    assert len(bs) % 8 == 0
    s = ''
    for i in range(0, len(bs), 8):
        s += chr(int(bs[i:i + 8], 2))
    return s


def string_to_bin(s):
    # Переводить текстовий рядок у бінарний (ASCII)
    def char_to_8bit(c):
        # Переводить символ у 8-бітний бінарний рядок (ASCII)
        return bin(ord(c))[2:].zfill(8)

    bs = ''
    for i in range(len(s)):
        bs += char_to_8bit(s[i])
    return bs


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


def is_text(text):
    # Перевіряє чи не містить даний рядок заборонених символів,
    # тобто чи не містить рядок символів крім літер англ. алфавіту, цифр і пробілу
    import string

    valid_chars = set(c for c in string.printable[:62])
    valid_chars.add(' ')
    return all(d in valid_chars for d in text)


def dec_to_bin(b):
    # Переводить число у відповідний бінарний рядок
    return bin(b)[2:]


def encrypt(plaintext, key):
    # Функція шифрування повідомлення; plaintext – текст; key – десяткове число.
    return xor_bits(string_to_bin(plaintext), dec_to_bin(key))


def decrypt(ciphertext, key):
    # Функція дешифрування повідомлення; ciphertext – бінарний рядок; key – десяткове число.
    return bit_to_string(xor_bits(ciphertext, dec_to_bin(key)))


def secret_key(p, a, g_b):
    return int(powmod(g_b, a, p))


def find_secret_key(p, g_b, ciphertext):
    ciphertext_len = len(ciphertext)
    keys = []
    for a in range(1, 10000000):
        key = secret_key(p, a, g_b)
        if ciphertext_len <= len(dec_to_bin(key)):
            decrypted = decrypt(ciphertext, key)
            if ciphertext == encrypt(decrypted, key) and is_text(decrypted):
                keys.append((a, key))
    return keys


def main():
    ciphertext = "101001101001000010110010000001000001010100000110000101101111101001011011"
    p, g = 4715958727385315387660737, 5
    g_b = 3193533191571883174254626
    keys = find_secret_key(p, g_b, ciphertext)
    for a, key in keys:
        print(ciphertext + " (a = " + str(a) + ", key = " + key + ") = " + decrypt(ciphertext, key))


if __name__ == '__main__':
    main()
