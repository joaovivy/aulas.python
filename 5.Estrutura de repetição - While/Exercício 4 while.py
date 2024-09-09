import os
os.system("cls || clear")

soma = 0
contador = 0

while True:
    nota = float(input("Digite uma nota: "))
    contador += 1
    soma += nota

    resposta = input("Deseja inserir mais uma nota? ").upper()
    # resposta = resposta.upper() # Converter em maiúsculo.

    if resposta == "N":
        break

media = soma / contador
print(f"Média {media}")

if contador == 0:
    print("A nota não foi repetida")
else:
    print(f"A nota foi repetida {contador} vezes.")

media = soma / contador
print(f"Média {media}")