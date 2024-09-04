import os
os.system("cls || clear")

nota = 0

while True:
    nota = float(input("Digite uma nota: "))
    if nota < 0:
        print("A nota deve ser maior que 0.")
        break
    else:
        media =+ nota
        print(f"Média: {media}")