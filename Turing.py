class Turing:

    def __init__(self, inicial, decremento):
        self.incial = inicial
        self.decremento = decremento

    def alg_turing(self, inicial, decremento):
        v = 1
        self.incial = v
        self.decremento = max(0, v - 1)

        while True:
            if v != 0:
                incremento = v + 1

            return v


if __name__ == '__main__':
    Turing.alg_turing()
