import os

os.system("cls || clear")

lista_numeros = []
QUANTIDADE_NUMEROS = 10
negativos = 0
positivos = 0
soma = 0

print("\n=== Solicitando dados ===")
for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1}º número: "))
    lista_numeros.append(numero)

# Processamento.
    if numero < 0:
        negativos += 1
    else:
        positivos += 1
        soma += numero 

# Saída.
print("\n=== Exibindo resultados ===")
for i, numero in enumerate(lista_numeros):
    print(f"{i+1}ª número: {numero}")

print(f"\nNegativos: {negativos}")
print(f"\nPositivos: {positivos}")
print(f"\nSoma dos números positivos: {soma}")