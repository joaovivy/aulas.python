import os
os.system("cls || clear") # Limpa o terminal.

# Solicitando dados.
nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade: "))
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media < 7:
    resultado = "REPROVADO"
else:
    resultado = "APROVADO"

print(f"Nome {nome}. ")
print(f"Idade {idade} anos. ")
print(f"Média {media}. ")
print(f"Resultado {resultado}. ")


