print('Olá esse programa calcula a média da metade de cada sala e exibe qual foi a maior nota')
contador = 1
totalimpar = 0
totalpar = 0

for x in range(1,5):

    if contador / 2 % 1:
        print("Você está digitando notas dos alunos impares ")
        ntimpar = float(input("Por favor, insira a nota do aluno de número {}: ".format(contador)))
        totalimpar = totalimpar + ntimpar

    else:
        print("Você está digitando notas dos alunos pares ")
        ntpar = float(input("Por favor, insira a nota do aluno de número {}: ".format(contador)))
        totalpar = totalpar + ntpar

    contador += 1

mediapar = totalpar / 2
mediaimpar = totalimpar / 2

print("A média dos alunos pares é {}".format(float(mediapar)))
print("A média dos alunos impares é {}".format(float(mediaimpar)))

if mediapar > mediaimpar:
    print("A maior nota é dos alunos pares")
else:
    print("A maior nota é dos alunos impares")