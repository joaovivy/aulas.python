import os
os.system("cls || clear")


QUANTIDADE_NUMEROS = 3
lista_pares_positivos = []

# Entrada.
print("\n=== Solicitando dados ===")
for i in range(QUANTIDADE_NUMEROS):
    while True:
        numero = int(input("Digite um número: "))

        # Verificando se o número é par ou positivo.
        if numero % 2 == 0 and numero > 0:
            lista_pares_positivos.append(numero)
            break
        else:
            print("Número inválido. \nTente novamente.")

# Saída.
print("\n=== Exibindo resultados ===")
for numero in lista_pares_positivos:
    print(numero)