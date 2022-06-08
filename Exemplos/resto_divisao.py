a = int(input("Digite valor de a: "))
b = int(input("Digite valor de b: "))
#retorna o resto de uma divisao'
c = a % b
if a == 0 and b == 0:
    print("Divisão impossível")
else:
    print("O valor da divisão é {0:.2f}".format(float(c)))