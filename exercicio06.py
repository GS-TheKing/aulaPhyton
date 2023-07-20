#6 faça um algoritmo que escreva na tela
#os números de um número inicial a um
#número final. Os números incial e final
#devem ser informados pelo usuário;
def inicialFinal(num, num2):
    if (num > num2):
        for i in range(num, num2-1, -1):
            print(i)

    else:
        for i in range(num, num2+1):
            print(i)