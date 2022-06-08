print("Esse é o sistema de assinaturas para utilização do estúdio profissional, abaixo nos informe o "
      "seu faturamento anual e logo o tipo de assinatura que deseja; ")
faturamento = float(input("Faturamento a.a - "))
assinatura = input("Nível de assinatura (Basic, Silver, Gold ou Platinum) - ")
if assinatura == "Basic":
    print("O bônus a pagar é de {}R$ o equivalente a 30% do seu faturamento.".format(int(faturamento * 0.3)))
elif assinatura == "Silver":
    print("O bônus a pagar é de {}R$ o equivalente a 20% do seu faturamento.".format(int(faturamento * 0.2)))
elif assinatura == "Gold":
    print("O bônus a pagar é de {}R$ o equivalente a 10% do seu faturamento.".format(int(faturamento * 0.1)))
elif assinatura == "Platinum":
    print("O bônus a pagar é de {}R$ o equivalente a 5% do seu faturamento.".format(int(faturamento * 0.05)))
