import os
os.system("cls || clear")

def verificar_idade():
    calculo  = 2024 - nascimento
    return calculo

nascimento = int(input("Digite o ano que você nasceu: "))

idade = verificar_idade()

print(f"Idade: {idade}")