""""
Escreva um algoritmo que solicite duas notas para um aluno.
Casi seja menor que 0 ou maior que 10, mostre a pergunta novamente.
Calcule e mostre a média aritmética do aluno.
"""

import os
os.system("cls || clear")

soma = 0

for i in range(2):
    while True:
        nota = float(input(f"Digite {i+1}ª nota: "))
    
        if nota >= 0 and nota <= 10:
            break

    soma += nota

media = soma / 2

print(f"Média {media}")