import matplotlib.pyplot as plt


def t_student():
    x_1 = float(input("Média da amostra: "))
    u_1 = float(input("Média da população: "))
    s = float(input("Desvio padrão da amostra: "))
    n = int(input("tamanho da amostra: "))
    list = []
    x_list = []
    for i in range(0, n):
        t = n + i * ((x_1 * i) - x_1) - n
        # t_1 = (((x_1 ** i) - u_1)/(s/float(n) ** 0.5))
        x_list.append(n + i)
        list.append(t)
        # list.append(t_1)
    amostra = plt.plot(list, x_list)
    plt.show()


t_student()

