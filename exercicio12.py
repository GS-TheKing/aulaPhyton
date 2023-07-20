def exibirValores():
    num=0
    c= 0
    s= 0
    for i in range(1, 21):
        num = int(input('informe um número: '))
        if (num > 0):
            s +=num

        if (num < 0):
            c += 1

    print('A soma dos números positivos é: {} e a quantidade dos números negativos é: {}'.format(s,c))






