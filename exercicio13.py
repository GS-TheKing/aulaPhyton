def fatorial ():
    num =0
    num = int(input('informe um número: '))
    m = num
    for i in range (num-1, 0, -1):
        m = m * i
    print('o resultado da fatoração é: {}'.format(m))

