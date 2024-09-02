import os
os.system("cls || clear")

contagem_negativos = 0

while True:
    numero = int(input("Digite um número: "))
    if numero >= 0:
        break

    contagem_negativos +=1

print(f"Quantidade de números negativos inseridos: {contagem_negativos}")
