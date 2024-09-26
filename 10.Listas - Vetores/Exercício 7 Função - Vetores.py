import os
os.system("cls || clear")

QUANTIDADE_NUMEROS = 5
lista_de_numeros = []

def verificando_numeros(lista_de_numeros):
    lista_atualizada = []

    for numero in lista_de_numeros:

        if numero < 0:
            numero = 0
        lista_atualizada.append(numero)

    return lista_atualizada

print("=== Solicitando dados ===")
for i in range(QUANTIDADE_NUMEROS):
    numero = int(input("Digite um número: "))

    lista_de_numeros.append(numero)

lista_de_numeros = verificando_numeros(lista_de_numeros)

print("\n=== Exibindo dados ===")
for cada_numero in lista_de_numeros:
    print(cada_numero)