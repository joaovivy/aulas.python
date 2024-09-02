import os
os.system ("cls || clear")

soma = 0
media = 0

for i in range(3):
    notas = float(input("Digite uma nota: "))
    soma = soma + notas

media = soma / 3

print(f"Média: {media}")

if media >= 7:
    print(f"Aprovado.")
else:
    if media < 4:
            print(f"Reprovado.")
    else:
            print("Recuperação.")
         
    