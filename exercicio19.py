valores = []

def coletarNumeros():
    maior= 0
    menor=0
    flag = False
    for i in range(5):
        num = int(input('Informe o {}º número: '.format(i+1)))
        valores.append(num)

        if(flag == False):
            maior = num
            menor = num
            flag = True

        if (num > maior):
            maior = num

        if (num < menor):
            menor = num

    print('O maior valor é: {}, e o menor valor é: {}'.format(maior, menor))

coletarNumeros()