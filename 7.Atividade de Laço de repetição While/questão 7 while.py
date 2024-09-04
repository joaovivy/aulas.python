import os
os.system("cls || clear")

senha_1 = 0
senha_2 = 0

while True:
    senha_1 = int(input("Crie uma senha: "))
    senha_2 = int(input("Confirme a senha: "))
    if senha_1 == senha_2:
        print("Senha criada com sucesso!")
        break
    else:
        print("As senhas não coincidem!")

