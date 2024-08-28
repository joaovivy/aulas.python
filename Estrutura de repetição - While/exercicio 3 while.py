import os
os.system("cls || clear")

login = "João"
senha = 1234
contador = 3

while True:
    login = input("Digite seu login: ")
    senha = int("Digite sua senha: ")

    if login == "João" and senha == 1234:
        print("Bme-vindo!")
        break
    else:
        print("Login ou senha inválidos.")
        print(f"Tentativa: {contador}")
        if contador == 3:
            break

print("=== FIM ===")