import os
os.system("cls || clear")

total_horas = 0

meta_de_horas = int(input("Digite a meta de horas de estudo: "))

while True:
    horas_estudadas = int(input("Digite a quantida de de horas estudadas: "))
    total_horas = total_horas + horas_estudadas

    if total_horas >= meta_de_horas:
        print(f"As horas de estudo foram excedidas!")
        break
    else:
        print(f"Horas que faltam: {meta_de_horas -total_horas} ")