def mediaTime():
    num= 0
    num2= 0
    soma = 0
    num =int(input('Informe a quantidade de jogadores: '))

    for i in range(1,num+1):
        num2=float(input('Informe a altura de todos os jogadores: '))
        soma += num2
        media = soma /i
    print('A média de altura do time é: {}'.format(media))
