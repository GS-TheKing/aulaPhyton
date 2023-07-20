from exercicio04 import somarInteiro
from exercicio05 import tabuada
from exercicio05 import coletarPositivo
from exercicio06 import inicialFinal
from exercicio07 import impar100200
from exercicio08 import dezNumeros
from exercicio09 import somarNumeros
from exercicio10 import somarZero
from exercicio11 import inteiroMaiorMenor
from exercicio12 import exibirValores
from exercicio13 import fatorial
from exercicio14 import mediaTime
from exercicio15 import miss
from vetores import preencherVetor
from vetores import consultarVetor
from vetores import apagarPosicao
from exercicio16 import votos
from exercicio17 import custoCarro
from exercicio18 import anosDias
from exercicio19 import coletarNumeros


def mostrarMenu():
    print('\n\n\nEscolha uma das opções abaixo' + '\n0. SAIR' +
    '\n1. Exercício 01'
    '\n2. Exercício 02' +
    '\n3. Exercício 03' +
    '\n4. Exercício 04' +
    '\n5. Exercício 05' +
    '\n6. Exercício 06' +
    '\n7. Exercício 07' +
    '\n8. Exercício 08' +
    '\n9. Exercício 09' +
    '\n10. Exercício 10' +
    '\n11. Exercício 11' +
    '\n12. Exercício 12' +
    '\n13. Exercício 13' +
    '\n14. Exercício 14' +
    '\n15. Exercício 15' +
    '\n16. Exercício 16' +
    '\n17. Exercício 17' +
    '\n18. Exercício 18' +
    '\n19. Exercício 19' +
    '\n20. Exercício 20' +
    '\n21. Preencher Vetor' +
    '\n22. Consultar vetor' +
    '\n23. Apagar Posição vetor')


def operacao():
    #Chamar o Método de cima
    opcao = 1
    while(opcao !=0):
        mostrarMenu()
        #Coletar a opção do usuário
        opcao = int(input('Digite aqui o número da opção escolhida: '))
        #Executo a ação
        if(opcao==0):
            #Instruções do Exercício01
            print('Obrigado!')
        elif(opcao==1):
            return
        elif(opcao==2):
            return
        elif(opcao==3):
            return
        elif(opcao==4):
            # Utilizar o exercício04
            print('\nExercício04')
            print(somarInteiro())
        elif (opcao == 5):
            # Exercício05
            print('\n tabuada')
            num= int(input('Informe um número'))
            n = coletarPositivo()
            tabuada(num, n)
        elif (opcao == 6):
            # Exercicio06
            print('\n inicalFinal')
            num= int(input('informe o início'))
            num2= int(input('Informe o fim'))
            inicialFinal(num, num2)
        elif (opcao == 7):
            #exercício07
            print(impar100200())
        elif (opcao == 8):
            # Exercício08
            print(dezNumeros())
        elif (opcao == 9):
            # Exercício09
            print (somarNumeros())
        elif (opcao == 10):
            # exercício10
            print(somarZero())
        elif (opcao == 11):
            # exercicio11
            print(inteiroMaiorMenor())
        elif (opcao == 12):
            #exercício12
            exibirValores()
        elif (opcao == 13):
           #exercício13
           fatorial()
        elif (opcao == 14):
           mediaTime()
        elif (opcao == 15):
            miss()
        elif (opcao == 16):
            votos()
        elif (opcao == 17):
            custoCarro()
        elif (opcao == 18):
            anosDias()
        elif (opcao == 19):
           coletarNumeros()
        elif (opcao == 20):
            return
        elif (opcao == 21):
            num= int(input(' Informe o tamanho do vetor: '))
            preencherVetor(num)
        elif (opcao == 22):
            num= int(input(' Informe o tamanho do vetor: '))
            consultarVetor(num)
        elif (opcao == 23):
            posicao= int(input(' Informe o a posição que deseja apagar: '))
            apagarPosicao(posicao-1)

        else:
            print('Opção Escolhida não é válida, digite novamente!')
    return