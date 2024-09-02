import os
os.system("cls || clear")

soma = 0
pares = 0
impares = 0

for i in range(5):
    numero = int(input("Digite um número ímpar: "))

    if numero % 2 == 0:
        print(f"Esse número é par")
        break
    else:
        soma = soma + numero
        impares = impares + 1
        print(f"Soma {soma}")