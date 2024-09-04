import os
os.system("cls || clear")

numero = 51

while True:
    numero = int(input("Digite um número: "))
    if numero >= 50 and numero % 7 == 0:
        print(f"{numero} é divisível por 7")
        break
    else:
        print(f"Esse número não é divisível por 7")