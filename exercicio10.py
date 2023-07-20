def somarZero():
    soma=0
    num = 1
    i = 0
    while (num != 0):
        num = int(input('Informe um número:'))
        if (num !=0):
            if (num % 2 == 0):
                soma += num
                i    +=1

    return 'A média dos números pares é:{}'.format(soma/i)

