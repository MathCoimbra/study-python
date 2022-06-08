print("Olá esse é o sorteio do console a ser sorteado para a equipe vencedora")
contador = 1
ps = 0
xbx = 0
nin = 0

for x in range(1,6):

    print("Escolha abaixo qual o console que o {}° membro escolheu:".format(contador))
    print("1 - Playstation")
    print("2 - Xbox")
    print("3 - Nintendo")
    op = int(input("Informe sua opção: "))

    contador += 1

    if op == 1:
        ps += 1
    elif op == 2:
        xbx += 1
    elif op == 3:
        nin += 1

if ps > xbx and ps > nin:
    print("O console escolhido foi o Playstation com {} votos".format(ps))
elif xbx > ps and xbx > nin:
    print("O console escolhido foi o Xbox com {} votos".format(xbx))
elif nin > ps and nin > xbx:
    print("O console escolhido foi o Nintendo com {} votos".format(nin))
else:
    print("Houve um empate na votação dos consoles")



