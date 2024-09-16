"""
Crie um algoritmo que aceite apenas 6 valores inteiros, positivos e pares, sem seguida,
mostre na tela os valores lidos na ordem inversa.

Caso seja informado um número diferente dos critérios apresentados acima,
repita a pergunta para o usuário
"""

import os
import time
os.system("cls || clear")

QUANTIDADE_NUMEROS = 4
lista_pares_positivos = []

# Funções.
def verificando_pares(lista_pares_positivos):
    lista_par = []

    for i in range(QUANTIDADE_NUMEROS):
        while True:
            numero = int(input(f"Digite o {i+1}º número: "))

            # Verificando se o número é par e positivo.
            if numero % 2 == 0 and numero > 0:
                lista_pares_positivos.append(numero)
                break
            else:
                print("Número inválido, tente novamente.")

        return lista_pares_positivos
    
resultado = verificando_pares(lista_pares_positivos)

# Saída.
print("\n=== Exibindo resultados ===")
for i, numero in enumerate(reversed(lista_pares_positivos)):
    print(f"{len(lista_pares_positivos) -i}º = {len(lista_pares_positivos)} - {i} º - {numero}")
    time.sleep(2)