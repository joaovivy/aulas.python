"""
Desenvolva um programa que utilize dois laços `for` (um dentro do outro) para imprimir um retângulo de 4 linhas por 6  colunas de asteriscos (`*`).
"""

import os
os.system("cls || clear")

num_linhas = 4
num_colunas = 6

# Laço para cada linha.
for i in range(num_linhas):
    # Laço para cada coluna dentro da linha.
    for i in range(num_colunas):
        # Imprime um asterisco sem pular linha.
        print('*', end='')
        print()