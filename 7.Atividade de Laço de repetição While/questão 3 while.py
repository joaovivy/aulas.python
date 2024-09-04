import os
os.system("cls || clear")

contador = 0
numero = int(input("Digite um número: "))
soma = 0

while True:
    fator = int(input("Digite o fator:"))
    produto = fator * numero
    soma += produto
    if produto < 100:
        print(f"Produto: {produto}")
        print(f"Soma dos produtos: {soma}")
        contador += 1
        if soma >= 100:
            print(f"O produto ultrapassou 100")
            break
    print(f"Número de ultiplicações realizadas: {contador}")