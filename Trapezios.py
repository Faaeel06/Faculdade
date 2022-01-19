import math


def analise_Trapezios():
    funcao = input('f(x) = ')
    x0 = float(input('Limite inferior = '))
    xMax = float(input('Limite superior = '))
    altura = float(input('Passo(h) = '))
    integral = 0
    x = x0
    integral += eval(funcao)
    x += altura
    while x < xMax:
        integral += 2 * eval(funcao)
        x += altura
    x = xMax
    integral += eval(funcao)
    integral *= (altura / 2)
    print(f'Integral = {integral}')


def methodo_Simpson():
    funcao_2 = input('f(x) = ')
    x0_2 = float(input('Limite inferior = '))
    xMax_2 = float(input('Limite superior = '))
    altura_2 = float(input('Passo(h) = '))
    integral_2 = 0
    x_2 = x0_2
    integral_2 += eval(funcao_2)
    x_2 += altura_2
    indice = 1
    while x_2 < xMax_2:
        if indice % 2 != 0:
            integral_2 += 4 * eval(funcao_2)
        else:
            integral_2 += 2 * eval(funcao_2)
        indice += 1
        x_2 += altura_2
    x_2 = xMax_2
    integral_2 += eval(funcao_2)
    integral_2 *= (altura_2 / 3)
    print(f'Integral = {integral_2}')


passos = int(input('Digite quantos passos: '))


def trapz(f, a, b, n):
    h = (b - a) / n
    soma = 0
    for k in range(1, n):
        soma += f(a + k * h)
    soma *= 2
    soma += (f(a) + f(b))
    soma *= (h / 2)
    return soma


def f(x):
    return math.exp(-x ** 2)


a, b = 0, 1

n = passos

r = trapz(f, a, b, n)
print(r)
