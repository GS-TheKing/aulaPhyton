def inteiroMaiorMenor():
    num =1
    i = 0
    menor = 0
    maior = 0
    while (num !=0):
        num = int(input('Informe um número: '))
        if(i == 0):
            maior= num
            menor= num

        if(num > maior):
            maior = num

        if(num < menor):
            menor = num

        i = 1
    print ('O maior número digitado foi {}, menor número foi {}.'.format(maior, menor))

