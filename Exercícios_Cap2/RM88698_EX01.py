print("Olá esse programa calcula o seu IMC, por gentileza preencher os dados abaixo;")
peso = float((input("Informe o seu peso: ")))
altura = float((input("Informe a sua altura: ")))
IMC = float(peso) / float(altura * altura)
print("Seu IMC é {0:.2f}".format(IMC))
#ERRO CORRIGIDO foi colocado o igual em "if IMC <(=) 16:" no que resultou na categoria errada quando o IMC
# era igual a 16
if IMC < 16:
    print("Sua categoria é Baixo peso Grau III")
elif 16 <= IMC <= 16.99:
    print("Sua categoria é Baixo peso Grau II")
elif 17 <= IMC <= 18.49:
    print("Sua categoria é Baixo peso Grau I")
elif 18.50 <= IMC <= 24.99:
    print("Sua categoria é Peso Ideal")
elif 25 <= IMC <= 29.99:
    print("Sua categoria é Sobrepeso")
elif 30 <= IMC <= 34.99:
    print("Sua categoria é Obesidade Grau I")
elif 35 <= IMC <= 39.99:
    print("Sua categoria é Obesidade Grau II")
elif 40 <= IMC:
    print("Sua categoria é Obesidade Grau III")
