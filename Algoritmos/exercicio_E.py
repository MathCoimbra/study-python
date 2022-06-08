# Algoritmo para verificar se os ambos números são pares, ímpares ou demais casos
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
if n1 % 2 == 0 and n2 % 2 == 0:
    print("Pares")
elif n1 % 2 == 1 and n2 % 2 == 1:
    print("Ímpares")
else:
    print("Outro")