def anosDias():
    anos= 1
    meses= 1
    dias= 1
    anosParaDias= 0
    mesesDias = 0

    anos= int(input('Informe os anos: '))
    while (anos < 0):
        anos= int(input('Informe os anos: '))
        print('ERRO!!, DIGITE UM VALOR MAIOR QUE 0 .')

    meses = int(input('Informe os meses: '))
    while (meses < 0):
        meses = int(input('Informe os meses: '))
        print('ERRO!!, DIGITE UM VALOR MAIOR QUE 0 .')


    dias= int(input('Informe os dias: '))
    while (dias <0):
        dias= int(input('Informe os dias: '))
        print('ERRO!, DIGITE UM VALOR MAIOR QUE 0 .')

    anosParaDias= anos *365
    mesesDias= meses *30

    resultado= dias + anosParaDias + mesesDias

    print('O valor em dias é de :{}'.format(resultado))

