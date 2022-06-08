# Algoritmo para ordenar valores em ordem crescente
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = 0
# Utilizando princípio da ordenação com a variável auxiliadora "n4" onde os valores das variáveis são trocados
if n1 >= n2:
    n4 = n1
    n1 = n2
    n2 = n4
if n1 >= n3:
    n4 = n1
    n1 = n3
    n3 = n4
if n2 >= n3:
    n4 = n2
    n2 = n3
    n3 = n4
    print(n1, " ", n2, " ", n3)
