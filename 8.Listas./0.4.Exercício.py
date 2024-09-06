import os
os.system("cls || clear")

def verificar_numero(numero):
    if numero % 2 == 0:
        print(f"O número é par")
    else:
        print(f"O número é ímpar")

numero = int(input("Digite um número: "))

numero = verificar_numero(numero)