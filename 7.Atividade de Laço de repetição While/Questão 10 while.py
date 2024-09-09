import os
os.system("cls || clear")

total_calorias = 2000
soma_calorias = 0

while True:
    calorias_consumidas = int(input("Digite a quantidade de calorias consumidas: "))
    soma_calorias = soma_calorias + calorias_consumidas
    if soma_calorias > 200:
        print("As calorias foram excedidas!")
        break
    else:
        print(f"Calorias que faltam {total_calorias + soma_calorias}")






