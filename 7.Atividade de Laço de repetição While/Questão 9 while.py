import os
os.system("cls || clear")

contador = 0
impares = 0

while impares <= 200:
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 != 0:
        impares += numero
        contador += 1

    print(f"Número digitado: {impares}")
       