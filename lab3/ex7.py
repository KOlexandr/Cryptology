__author__ = 'Olexandr'


class DiffiGelman:
    def __init__(self, p, g, a, b):
        self.p = p
        self.g = g
        self.a = a
        self.b = b

    def secret_key(self):
        return self.fast_pow(self.g, self.a * self.b, self.p)

    @staticmethod
    def fast_pow(a, b, n):
        # функція піднесення a до степеня b за модулем n
        # a,b,n – числа у десятковій системі числення
        # z – це результат функції (число у десятковій системі числення)
        def dec_to_bin(x):
            # функція, що переводить x в двійкову систему числення
            # результат - це бінарний текстовий рядок; напр., dec_to_bin(11)=’1011’
            return bin(x)[2:]
        b_2 = dec_to_bin(b)  # представляємо b в двійковій системі
        l = len(b_2)
        z = [1]
        for i in range(1, l + 1):
            if b_2[i-1] == '0':
                z.append(z[i-1] * z[i-1])
            else:
                z.append((z[i-1] * z[i-1] * a) % n)

        return z[len(z)-1]


def main():
    dg = DiffiGelman(4715958727385315387660737, 5, 10611587, 31081541)
    print("secret key = " + str(dg.secret_key()))


if __name__ == '__main__':
    main()
