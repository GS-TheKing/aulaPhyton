def miss():
    num = -1
    candidata =''
    nVencedora =''
    notaVencedora = 0

    for i in range(1,17):
        candidata =input('informe o nome da {}° candidata'.format(i))
        num = int(input('Informe a nota da candidata: '))

        while((num < 0) or (num > 10)):
            num = int(input('Informe a nota da candidata: '))
            print ('Erro digite um número entre 0 e 10')

        if (num > notaVencedora):
            notaVencedora = num
            nVencedora= candidata

    print('O nome da vencedora é {}, e a nota dela foi {}'.format(nVencedora, notaVencedora))





