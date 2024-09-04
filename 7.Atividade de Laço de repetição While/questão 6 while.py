import os
os.system("cls || clear")

notas = 0

while True:
    nota = float(input("Digite uma nota: "))

    if nota < 0:
        break
    notas.append(nota)
    print("Entrada inválida. Por favor, insira um número.")

    if notas:
        media = sum(notas) / len(notas)
        print(f"A média das notas é: {media:.2f}")
    else:
        print("Nenhuma nota foi inserida.")

