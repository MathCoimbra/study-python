print("Esse é o algoritmo da sorte de Fibonnaci")
numero = int(input("Por favor informe um número inteiro: "))
elemento1 = 0
elemento2 = 0
while(elemento1 <= numero):
    elemento1 = elemento1 + elemento2
    elemento2 = elemento1 - elemento2
    if(elemento1 == 0):
        elemento1 = elemento1 + 1
if elemento1 and elemento2 != numero:
    print("Ação falhou...")
else:
    print("Ação bem sucedida!!")