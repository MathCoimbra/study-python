print("Esse é um programa de gerenciamento de votação para a escolha de qual dia útil ocorrerá as lives.")
seg = input("Quantos votos para segunda-feira? ")
ter = input("Quantos para terça-feira? ")
qua = input("Quarta-feira, quantos votos? ")
qui = input("Quantos para quinta-feira? ")
sex = input("E para sexta-feira? ")
if seg > ter and seg > qua and seg > qui and seg > sex:
    print("O dia escolhido foi segunda-feira")
elif ter > seg and ter > qua and ter > qui and ter > sex:
    print("O dia escolhido foi terça-feira")
elif qua > seg and qua > ter and qua > qui and qua > sex:
    print("O dia escolhido foi quarta-feira")
elif qui > seg and qui > ter and qui > qua and qui > sex:
    print("O dia escolhido foi quinta-feira")
elif sex > seg and sex > ter and sex > qua and sex > qui:
    print("O dia escolhido foi sexta-feira")
else:
    print("Houve um empate na votação")