import os
os.system("cls || clear")

codigo = "PROMO2024"
contador = 3

while True:
    codigo = input("Digite o código: ")

    if codigo == "PROMO2024":
        print("Código aceito!")
        break
    else:
        print("Código inválido!")
        print(f"Tentativas: {contador}")
        if contador == 3:
            break

print("=== FIM ===")