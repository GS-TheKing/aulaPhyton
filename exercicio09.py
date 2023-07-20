#09 Faça o mesmo que antes, mas para se digitar 0
def somarNumeros():
     soma=0
     num = 1
     while (num !=0):
        num = int(input('Informe um número:'))
        soma +=num
     return 'a soma dos números é{}'.format(soma)