import os

os.system("cls || clear")

# Entrada.
QUANTIDADE_NOTAS = 3
lista_notas = []

for i in range(QUANTIDADE_NOTAS):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota)

# Saída.
for i, nota in enumerate (lista_notas):
    print(f"{i+1}ª nota: {nota}")
