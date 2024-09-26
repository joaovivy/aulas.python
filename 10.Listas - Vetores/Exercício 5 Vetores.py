import os

os.system("cls || clear")

lista_numeros = []
pares = 0
impares = 0

print(f"\n=== Solicitando dados ===")
for i in range(6):
    numero = int(input("Digite um número: "))
    lista_numeros.append(numero)

# Processamento.
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

# Saída.
print(f"\n=== Exibindo resultados ===")
for i, numero in enumerate(lista_numeros):
    print(f"{i+1}ª número: {numero}")

print(f"\nPares: {pares}")
print(f"\nímpares: {impares}")