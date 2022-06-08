# Algoritmo para verificar se os números são positivos (Azul) e se são ímpares (Laranja) ou em demais casos (Roxo)
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
if n1 > 0 and n2 > 0:
    print("Azul")
if n1 % 2 == 1 and n2 % 2 == 1:
    print("Laranja")
else:
    print("Roxo")