print("Esse é o programa de controle de calorias")
caloria_total = 0.0
contadora = 1
quant_alimento = int(input("Por favor informe quantos alimentos você ingeriu hoje: "))
if quant_alimento == 1:
    caloria = float(input("Quantas calorias você ingeriu desse alimento? "))
    caloria_total = caloria + caloria_total
else:
    while contadora <= quant_alimento:
        caloria = float(input("Quantas calorias você ingeriu do alimento {}? ".format(contadora)))
        contadora = contadora + 1
        caloria_total = caloria + caloria_total
print("Você ingeriu um total de {} kcal".format(caloria_total))