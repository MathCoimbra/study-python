numero = int(input("De qual número você quer a tabuada ? "))
#variável contadora
contadora = 1
#enquanto a variável for menor ou igual a 10
while contadora <= 10:
    #mostre o valor escolhido pelo usuário vezes a variável contadora
    print("{} x {} = {}".format(numero, contadora, numero * contadora))
    #adicionar incremento abaixo para que o valor da variável mude a cada volta do loop formando assim a tabuada
    contadora = contadora + 1