import os
os.system("cls || clear") # Limpa o terminal.

# Solicitando dados.
login = input("Digite o seu login: ")
senha = input("Digite sua senha: ")

# Verificar.
if login == "HELLO" and senha == "12345":
    print("Bem_vindo!")
else:
    print("Login ou senha inválidos. ")