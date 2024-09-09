import os
os.system("cls || clear")

quantidade_notas = 3
soma = 0

def verificar_media(primeira_nota, segunda_nota, terceira_nota):
    media = (primeira_nota + segunda_nota + terceira_nota) / 3
    return media

for i in range(3):
    nota = float(input("Digite a primeira_nota: "))
    soma = soma + nota
    media = soma / 3

print(f"Média: {media}")

