# Algoritmo para informar a categoria do usuário através da idade e nível de risco
idade = int(input("Qual a sua idade ? "))
nv_risco = str(input("Qual o seu nível de risco ?"
"B - Baixo risco, M - Médio risco ou A - Alto risco "))
if 17 <= idade <= 20 and nv_risco == "B":
    print("Sua categoria é 1")
elif 17 <= idade <= 20 and nv_risco == "M" or 21 <= idade <= 24 and nv_risco == "B":
    print("Sua categoria é 2")
elif 17 <= idade <= 20 and nv_risco == "A" or 21 <= idade <= 24 and nv_risco == "M" or 25 <= idade <= 34 and nv_risco == "B":
    print("Sua categoria é 3")
elif 21 <= idade <= 24 and nv_risco == "A" or 25 <= idade <= 34 and nv_risco == "M" or 35 <= idade <= 64 and nv_risco == "B":
    print("Sua categoria é 4")
elif 25 <= idade <= 34 and nv_risco == "A" or 35 <= idade <= 64 and nv_risco == "M":
    print("Sua categoria é 5")
elif 35 <= idade <= 64 and nv_risco == "A":
    print("Sua categoria é 6")
elif 65 <= idade <= 70 and nv_risco == "B":
    print("Sua categoria é 7")
elif 65 <= idade <= 70 and nv_risco == "M":
    print("Sua categoria é 8")
else:
    print("Sua categoria é 9")
