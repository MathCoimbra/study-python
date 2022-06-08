print("Algoritmo de verificação dos batimentos cardíacos!")
print(" ")
BPM = int(input("Informe o número de batimentos por minuto (frequência cardíaca): "))
idade = int(input("Quantos anos você tem? "))
if idade <= 2 and 120 <= BPM <= 140 or 8 <= idade <= 17 and 80 <= BPM <= 100 or 18 <= idade <= 59 and 70 <= BPM <= 80 or 60 <= idade <= 100 and 50 <= BPM <= 60:
    print("Seus batimentos encontram-se DENTRO da faixa adequada")
elif idade <= 2 and BPM < 120 or 8 <= idade <= 17 and BPM < 80 or 18 <= idade <= 59 and BPM < 70 or 60 <= idade <= 100 and BPM < 50:
    print("Seus batimentos encontram-se ABAIXO da faixa adequada")
elif idade <= 2 and BPM > 140 or 8 <= idade <= 17 and BPM > 100 or 18 <= idade <= 59 and BPM > 80 or 60 <= idade <= 100 and BPM > 60:
    print("Seus batimentos encontram-se ACIMA da faixa adequada")
