#08 Escrever um algoritmo que leia 10
#números inteiros e, ao final, apresente a
# soma de todos os números inteiros
def dezNumeros():
    n1 = 0
    for i in range(1,11):
        num = int(input('Digite o {}° número: '.format(i)))
        n1 += num
    return ' O resultado é:{} '.format(n1)



