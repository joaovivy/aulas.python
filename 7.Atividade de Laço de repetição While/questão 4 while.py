import os
os.system("cls || clear")

gasto_total = 0

orcamento = int(input("Digite seu orçamento: "))

while True:
    gasto_diario = int(input("Digite seu gasto diário: "))
    gasto_total = gasto_total + gasto_diario

    if gasto_total > orcamento:
        print(f"O gasto é maior que o orçamento.")
        break
    else:
        print(f"Total: {orcamento - gasto_total}")