from lab2.OneTimeNote import OneTimeNote

BITS_IN_BYTE = 8

__author__ = 'Olexandr'


def main():
    c1 = '01111100101101111010000010100000111000011111001111000110100111000111111000000011' \
         '10110010101110001110010010011100010011110010100110111100111011101001101101000011' \
         '01001111010011110010101111110010011110110001000001011000100110010111001011111000' \
         '00000101011110110111001000001000011011100100010100110010101000001000000000001111' \
         '11011010001110011001010101111110010011101000111000110010000010010101010010100101'
    c2 = '01101001111111111010011011101000111011011111010111011010110110010011011100000100' \
         '11111010101111101110010010010111010001010010100110111110111101011101101001011110' \
         '01011100010110000110010011101000011101000101010100011001100001110011110111100011' \
         '00010100001010000010011000010111011011100101110101111001101101101000011100011010' \
         '10000011011101011000100001111000010000001000111001100001010010000001100111100000'
    c3 = '01110011111100101011010110101101111100101011101011011000110010010110001101010000' \
         '11111101101100011110110011010000010000110110011110101001111101001101011100010000' \
         '01001111010100100010100111110011011011100100001001010110100111010111001011100110' \
         '00011001011010010010011001011111011100100100101100101100111001011001000000011010' \
         '10010100011101011001100001111111000001011101101001111101010011010001010111111100'

    k = ['-', '\x97', '-', 'È', '-', '\x9a', '-', '¼', '\x17', 'p', '\x92', '-', '-', 'ð', '-', 'G', '-', '-', '»', '0', '-', '-', 'D', '-', '-', '0', '9', '-', '\x1d', '-', '-', '\x08', 'R', '\x7f', '-', '-', 'Y', 'Å', '-', '-', 'ú', '\x19', '-', '-', '%', 'ú', '\x12', ')', 't', '\x85']
    message_len = len(c1)
    found_chars = 5
    c1_end = c1[message_len - found_chars * BITS_IN_BYTE:message_len]
    c2_end = c2[message_len - found_chars * BITS_IN_BYTE:message_len]
    c3_end = c3[message_len - found_chars * BITS_IN_BYTE:message_len]
    found = OneTimeNote.string_to_bin(" " * found_chars)
    end_key = OneTimeNote.xor_bits(c1_end, found)

    print(OneTimeNote.bit_to_string(end_key))
    print("c2 end = " + OneTimeNote.bit_to_string(OneTimeNote.xor_bits(c2_end, end_key)))
    print("c3 end = " + OneTimeNote.bit_to_string(OneTimeNote.xor_bits(c3_end, end_key)))
    print("1-2 ->")
    print(list(OneTimeNote.bit_to_string(OneTimeNote.xor_bits(c1, c2))))
    print("1-3 ->")
    print(list(OneTimeNote.bit_to_string(OneTimeNote.xor_bits(c1, c3))))
    print("2-3 ->")
    print(list(OneTimeNote.bit_to_string(OneTimeNote.xor_bits(c2, c3))))

    key_p = OneTimeNote.string_to_bin(''.join(k))
    print(OneTimeNote.bit_to_string(OneTimeNote.xor_bits(c2, key_p)))
    print(OneTimeNote.bit_to_string(OneTimeNote.xor_bits(c3, key_p)))
    print(len(k))

if __name__ == '__main__':
    main()