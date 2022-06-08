print("Esse é o programa de controle financeiro para crianças")
valor_total = 0.0
contadora = 1
quant_transacao = int(input("Por favor informe quantas transações você realizou: "))
while contadora <= quant_transacao:
    valor = float(input("Quanto você gastou com a {}° transação? ".format(contadora)))
    contadora = contadora + 1
    valor_total = valor_total + valor
    media = valor_total/quant_transacao
print("Você gastou um total de {}R$".format(valor_total))
print("Sua média de cada transação é de {:.2f}R$".format(media))