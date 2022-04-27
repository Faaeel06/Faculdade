#  Importando bibliotecas
import math
from time import sleep


def bissec():
    print("\nMÉTODO DE BISSECÇÃO")
    #  Chamando variáveis // Definindo parâmetros de intervalo e erro
    a = float(input('Digite o valor de A: '))
    b = float(input('Digite o valor de B: '))
    e = 10 ** (-5)
    xi = 0

    # Definindo a função
    def f(x):
        resp = math.exp(-x) - x
        return resp

    #  Teorema de Bolzano
    if f(a) * f(b) < 0:
        while math.fabs(b - a) / 2 > e:
            xi = (a + b) / 2
            if f(xi) == 0:
                print(f"Raiz:{xi}")
                break
            else:
                if f(a) * f(xi) < 0:
                    b = xi
                else:
                    a = xi
        print(f"Valor da raiz: {xi}")
    else:
        print('Inválido')


def f_pos():
    print("\nMÉTODO DA FALSA POSIÇÃO")
    #  Chamando variáveis // Definindo parâmetros de intervalo e erro
    a = float(input('Digite o valor de A: '))
    b = float(input('Digite o valor de B: '))
    l = float(input('Digite o valor da amplitude final: '))

    def f(x):
        result = math.exp(-x) - x
        return result

    c = b - a

    x0 = (a * f(b) - b * f(a)) / (f(b) - f(a))

    while c > l or math.fabs(f(x0)):
        if f(a) * f(x0) < 0:
            b = x0
        elif f(a) * f(x0) > 0:
            a = x0
        else:
            break
        c = b - a
        x0 = (a * f(b) - b * f(a)) / (f(b) - f(a))

    print(f'Raiz: {x0}\n'
          f'f({x0}) = {f(x0)}')


def meth_Newton():
    print("\nMÉTODO DE NEWTON")
    #  Chamando variáveis // Definindo parâmetros de intervalo
    X0 = float(input('Digite o valor da Aproximação inicial: '))
    tol = 10 ** (-5)
    N0 = float(input('Digite o número máximo de Iterações: '))
    i = 1

    def f(x):
        func = math.exp(-x) - x
        return func

    def df(x):
        h = 0.000001
        deriv = (f(x + h) - (f(x))) / h
        return deriv

    while math.fabs(f(X0)) > tol:
        x = X0 - f(X0) / df(X0)
        X0 = x
        i += 1
        if i >= N0:
            print('Raiz não encontrada.')
            break

    if i < N0:
        print(f'Raiz: {X0}\n'
              f'Iterações: {i}\n'
              f'f({X0:.2f} )= {f(X0):.2f}')


def secc():
    print("\nMÉTODO DAS SECANTES")
    #  Chamando variáveis // Definindo parâmetros de intervalo
    xn = 0
    x = []
    i = 1
    n = 1
    tol = 10 ** (-5)
    N0 = float(input('Digite o número máximo de Iterações: '))
    a = float(input('Digite o valor da A: '))
    b = float(input('Digite o valor da B: '))

    x.append(a)
    x.append(b)

    def f(x):
        value = math.exp(-x) - x
        return value

    while math.fabs(f(xn)) > tol:

        xn = x[n] - (x[n] - x[n - 1]) / (f(x[n]) - f(x[n - 1])) * f(x[n])
        x.append(xn)
        n = n + 1
        i = i + 1

        if i >= N0:
            break

    print(f'Raiz: {xn:.5f}\n'
          f'Iterações: {i}\n'
          f'f({xn:.2f} )= {f(xn):.2f}')


bissec()
sleep(0.5)
f_pos()
sleep(0.5)
meth_Newton()
sleep(0.5)
secc()
