def votos():

    totalEleitores = int(input('Informe o número total de eleitores: '))
    while (totalEleitores <0):
        totalEleitores = int(input('Informe o número total de eleitores: '))
        print('ERRO!!, DIGITE UM NÚMERO DE ELEITORES MAIOR QUE 0.')

    votosBrancos = int(input('Informe o número de votos brancos: '))
    while (votosBrancos < 0):
        votosBrancos = int(input('Informe o número de votos brancos: '))
        print('ERRO!!, DIGITE UM NÚMERO DE VOTOS BRANCOS MAIOR QUE 0.')

    votosNulos = int(input('Informe o número de votos nulos: '))
    while (votosNulos < 0):
        votosNulos = int(input('Informe o número de votos nulos: '))
        print('ERRO!!, DIGITE UM NÚMERO DE VOTOS BRANCOS MAIOR QUE 0.')

    votosValidos = int(input('Informe o número de votos valídos: '))
    while (votosValidos < 0):
        votosValidos = int(input('Informe o número de votos valídos: '))
        print('ERRO!!, DIGITE UM NÚMERO DE VOTOS VALIDOS MAIOR QUE 0.')

    if (votosValidos + votosNulos + votosBrancos) > totalEleitores:
        print('ERRO!!. VOTOS PASSARAM O TOTAL')


    porcentagemBrancos= (votosBrancos *100) / totalEleitores

    porcentagemNulos= (votosNulos *100) / totalEleitores

    porcentagemValidos= (votosValidos *100) / totalEleitores

    print('A porcentagem de votos nulos é: {}% '.format(porcentagemNulos))
    print('A porcentagem de votos válidos é: {}% '.format(porcentagemValidos))
    print('A porcentagem de votos brancos é: {}%'.format(porcentagemBrancos))

