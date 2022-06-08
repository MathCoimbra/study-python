a = int(input("Digite valor de a: "))
b = int(input("Digite valor de b: "))
#divisão inteira = se o valor da divisão for uma fração (decimal) irá trazer somente o valor inteiro
c = a // b
if a == 0 and b == 0:
    print("Divisão impossível")
else:
    print("O valor da divisão é {0:.2f}".format(float(c)))