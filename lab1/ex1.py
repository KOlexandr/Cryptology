__author__ = 'Olexandr'


class FourSquare:
    def __init__(self, top_left, top_right, bottom_left, bottom_right):
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right

    def encode(self, word):
        new_word = []
        for (i, j) in zip(word[0::2], word[1::2]):
            (fi, fj), (si, sj) = self.find_bigram_position(i, j, self.top_left, self.bottom_right)
            new_word.append(self.top_right[fi][fj])
            new_word.append(self.bottom_left[si][sj])
        return "".join(new_word)

    def decode(self, word):
        new_word = []
        for (i, j) in zip(word[0::2], word[1::2]):
            (fi, fj), (si, sj) = self.find_bigram_position(i, j, self.top_right, self.bottom_left)
            new_word.append(self.top_left[fi][fj])
            new_word.append(self.bottom_right[si][sj])
        return "".join(new_word)

    @staticmethod
    def find_bigram_position(f, s, top, bottom):
        ti, tj = FourSquare.find_character(f, top)
        bi, bj = FourSquare.find_character(s, bottom)
        return (ti, bj), (bi, tj)

    @staticmethod
    def find_character(character, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == character:
                    return i, j
        return -1, -1


def main():
    top_left = [
        ['a', 'b', 'c', 'd', 'e'],
        ['f', 'g', 'h', 'i', 'k'],
        ['l', 'm', 'n', 'o', 'p'],
        ['q', 'r', 's', 't', 'u'],
        ['v', 'w', 'x', 'y', 'z']
    ]
    top_right = [
        ['S', 'U', 'N', 'A', 'E'],
        ['G', 'I', 'Y', 'O', 'K'],
        ['H', 'W', 'R', 'Q', 'B'],
        ['L', 'C', 'T', 'P', 'F'],
        ['M', 'Z', 'D', 'X', 'V']
    ]
    bottom_left = [
        ['I', 'Z', 'D', 'N', 'S'],
        ['P', 'L', 'U', 'B', 'W'],
        ['V', 'H', 'E', 'O', 'F'],
        ['T', 'R', 'K', 'A', 'Q'],
        ['X', 'Y', 'C', 'M', 'G']
    ]
    bottom_right = [
        ['a', 'b', 'c', 'd', 'e'],
        ['f', 'g', 'h', 'i', 'k'],
        ['l', 'm', 'n', 'o', 'p'],
        ['q', 'r', 's', 't', 'u'],
        ['v', 'w', 'x', 'y', 'z']
    ]

    encoded = "SGSVLSFN"
    decoded = "evaluate"
    four_square = FourSquare(top_left, top_right, bottom_left, bottom_right)
    print(encoded + " = " + four_square.decode(encoded))
    print(decoded + " = " + four_square.encode(decoded))


if __name__ == '__main__':
    main()