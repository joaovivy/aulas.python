import os
os.system("cls || clear")

numero_inicial = float(input("Digite o número inicial: "))
fator = float(input("Digite o fator: "))

produto = numero_inicial
contagem_multiplicacoes = 0

while produto <= 100:
    produto *= fator
    contagem_multiplicacoes +=1

print(f"Produto final: {produto}")
print(f"Número de multiplicações realizadas: {contagem_multiplicacoes}")