import os

os.system("cls || clear")

# Entrada
QUANTIDADE_NUMEROS = 5
lista_numeros = []

print("\n=== Solicitando dados ===")
for i in range(QUANTIDADE_NUMEROS):
    numero = float(input("Digite um número: "))
    lista_numeros.append(numero)

# Processando.
maior_numero = max(lista_numeros)
menor_numero = min(lista_numeros)

# Saída.
print("\n=== Exibindo resultados ===")
for i, numero in enumerate (lista_numeros):
    print(f"{i+1}ª número: {numero}")

print(f"\nMenor número: {menor_numero}")
print(f"\nMaior número: {maior_numero}")