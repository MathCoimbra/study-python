print("Esse programa inverte os conteúdos de duas variáveis")
A = input("Digite o conteúdo da variável A: ")
B = input("Digite o conteúdo da variável B: ")
troca = A
A = B
B = troca
print("Agora que trocamos, a variável A contém {} e a variável B contém {}".format(A, B))