from lab2.OneTimeNote import OneTimeNote

__author__ = 'Olexandr'


def main():
    key = '110111000100000000010000000110110100101101001011010110011100111100010001' + \
          '110001111110011101011110001000110011101111000001011001000010100100111111'
    encoded = '100100010010111101110100011011100010011100101010001010111110111101110000' + \
              '101101011000111000101010010010110101011010100100000100000100000001011100'
    decoded = 'Modular arithmetic'
    note = OneTimeNote(key)
    print(OneTimeNote.bit_to_string(encoded) + " = " + note.decode(encoded))
    print(decoded + " = " + note.encode(decoded, False))


if __name__ == '__main__':
    main()