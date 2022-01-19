import math

A = 2
b = 1
maxinter = 2


def gaussJacobi(A, b, maxinter, eps) -> object:
    n = len(b)
    sol = True
    x = b.copy()

    for i in list(range(1, n + 1, 1)):
        if math.fabs(A[i - 1][i - 1]) > 0.0:
            x[i - 1] = b[i - 1] / A[i - 1][i - 1]
        else:
            sol = False
            break

        if sol:
            print("Interação 0")
            print(f"x = {x}")

    list(x)

    print(f"x = {x}")

    xk.copy()

    inter = 2
    eps = 0.009

    while inter < maxinter:
        inter += 1
        for i in list(range(1, n + 1, 1)):
            s = 0
            for j in list(range(1, n + 1, 1)):
                if (i - 1) != (j - 1):
                    s = s + A[i - 1][j - 1] * x[j - 1]

        A = [10, 3, -2, 2]
        b = x

    x = gaussJacobi()

    xk[i - 1] = (1 / A[i - 1][i - 1]) * (b[i - 1] - s)

    list(x)
