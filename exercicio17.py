def custoCarro():
    valorCarro = 1

    valorCarro= int(input('Informe o valor do carro: '))
    while (valorCarro < 0):
        valorCarro = int(input('Informe o valor do carro: '))
        print('ERRO!!, DIGITE UM VALOR MAIOR QUE 0 .')

    valorImposto= valorCarro *0.45
    valorDistribuidora= valorCarro *0.28

    novoValor= valorCarro + valorImposto + valorDistribuidora

    print('\n o valor do imposto é de 45%')
    print('\n O valor da distribuidora é de 28%')
    print('\nO valor final do veículo ao consumidor é:{}'.format(novoValor))

