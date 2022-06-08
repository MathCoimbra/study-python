cmpista = int(input("Digite o cumprimento da pista: "))
nrvoltas = int(input("Digite o número de voltas: "))
nrreabastecimento = int(input("Digite o número de reabastecimentos desejado: "))
consumo = int(input("Digite o consumo de combustível (KM/L): "))
voltaparada1 = nrvoltas/nrreabastecimento
reabastecimento1 = voltaparada1*(cmpista)
print("Total de combustivel até o primeiro estabelecimento: {} ".format(reabastecimento1) + " litros")