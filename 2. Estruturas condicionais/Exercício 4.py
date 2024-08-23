import os
os.system("cls || clear")

# Solicitando dados.
idade = int(input("Digite sua idade: "))

# Verificando.
if idade <= 18 or idade >= 65:
    print("Não é obrigado a votar.")
else:
    print("É obrigado a votar.")