import os

os.system("cls || clear")

def calcular_media (n1, n2):
    soma = n1 + n2 
    resultado = soma / 2
    return resultado

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

media = (primeiro_numero + segundo_numero) / 2

print(f"Média: {media}")