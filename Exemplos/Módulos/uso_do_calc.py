#importação do módulo calc.py
import calc
#solicitando valores ao usuário
valor1 = input("Digite um valor: ")
valor2 = input("Digite outro valor: ")
#armazenando a soma NomeDoModulo.NomeDaFuncao
soma = calc.somar(valor1, valor2)
#exibindo a soma
print("A soma é {}".format(soma))