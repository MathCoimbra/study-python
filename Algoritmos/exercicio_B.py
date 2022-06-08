# Algoritmo para verificar os dois maiores valores entre três números e logo exibir a soma entre eles
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
if n1 > n2 > n3 or n2 > n1 > n3:
    print(n1 + n2)
elif n1 > n3 > n2 or n3 > n1 > n2:
    print(n1 + n3)
else:
    print(n2 + n3)