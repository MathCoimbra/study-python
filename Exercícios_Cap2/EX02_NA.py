print("Algoritmo de auxílio a programa de descontos progressivos na compra de pacotes de viagens!")
print(" ")
VB = float(input("Qual o valor da viagem? "))
categoria = str(input("Qual categoria? "))
quant_viajante = int(input("Quantos viajantes moram na mesma casa? "))
print("Valor bruto: {}R$".format(int(VB)))
if categoria == "Econômica" and quant_viajante == 2:
    print("Desconto: 3%")
    print("Valor líquido da viagem: {0:.2f}R$".format(VB * 0.97))
    print("Valor médio por viajante: {0:.2f}R$".format(VB * 0.97 / quant_viajante))
elif categoria == "Econômica" and quant_viajante == 3:
    print("Desconto: 4%")
    print("Valor líquido da viagem: {0:.2f}R$".format(VB * 0.96))
    print("Valor média por viajante: {0:.2f}R$".format(VB * 0.96 / quant_viajante))
elif categoria == "Econômica" and quant_viajante >= 4:
    print("Desconto: 5%")
    print("Valor líquido da viagem: {0:.2f}R$".format(VB * 0.95))
    print("Valor médio por viajante: {0:.2f}R$".format(VB * 0.95 / quant_viajante))
elif categoria == "Executiva" and quant_viajante == 2:
    print("Desconto: 5%")
    print("Valor líquido da viagem: {0:.2f}R$".format(VB * 0.95))
    print("Valor médio por viajante: {0:.2f}R$".format(VB * 0.95 / quant_viajante))
elif categoria == "Executiva" and quant_viajante == 3:
    print("Desconto: 7%")
    print("Valor líquido da viagem: {0:.2f}R$".format(VB * 0.93))
    print("Valor média por viajante: {0:.2f}R$".format(VB * 0.93 / quant_viajante))
elif categoria == "Executiva" and quant_viajante >= 4:
    print("Desconto: 8%")
    print("Valor líquido da viagem: {0:.2f}R$".format(VB * 0.92))
    print("Valor médio por viajante: {0:.2f}R$".format(VB * 0.92 / quant_viajante))
elif categoria == "Primeira classe" and quant_viajante == 2:
    print("Desconto: 10%")
    print("Valor líquido da viagem: {0:.2f}R$".format(VB * 0.9))
    print("Valor médio por viajante: {0:.2f}R$".format(VB * 0.9 / quant_viajante))
elif categoria == "Primeira classe" and quant_viajante == 3:
    print("Desconto: 15%")
    print("Valor líquido da viagem: {0:.2f}R$".format(VB * 0.85))
    print("Valor média por viajante: {0:.2f}R$".format(VB * 0.85 / quant_viajante))
elif categoria == "Primeira classe" and quant_viajante >= 4:
    print("Desconto: 20%")
    print("Valor líquido da viagem: {0:.2f}R$".format(VB * 0.8))
    print("Valor médio por viajante: {0:.2f}R$".format(VB * 0.8 / quant_viajante))