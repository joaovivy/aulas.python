import os

os.system("cls || clear")

# Entrada.
lista_notas = []

for i in range(2):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota)

# Saída.
for nota in lista_notas:
    print(f"Nota: {nota}")