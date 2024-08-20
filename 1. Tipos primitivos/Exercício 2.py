import os
os.system("cls || clear") # Limpa o terminal.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
soma = numero1 + numero2
produto = numero1 + numero2
media = soma / 2

if numero1 < numero2:
    menor_valor = numero1
    maior_valor = numero2
else:
    menor_valor = numero1
    maior_valor = numero2

print(f"Média {media}. ")
print(f"Soma {soma}. ")
print(f"Produto {produto}. ")
print(f"Menor valor {menor_valor}. ")
print(f"Maior valor {maior_valor}. ")
