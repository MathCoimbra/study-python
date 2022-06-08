print("Esse é um programa para descobrir a senha da máquina do servidor que foi hackeado")

qtmin = int(input("Insira a quantidade de minutos nesse momento: "))
fatmin = 1

for x in range(1, qtmin + 1):
    fatmin = fatmin * x
    print(x)

print("A senha é LIBERDADE{}".format(fatmin))