import os

os.system("cls || clear")

# Entrada.
lista_notas = []
QUANTIDADE_NOTAS = 4

print("\n=== Solicitando dados ===")
for i in range(QUANTIDADE_NOTAS):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota)

# Processamento.
soma = sum(lista_notas)
media = soma / QUANTIDADE_NOTAS

print("\n=== Exibindo resultados ===")
for i, nota in enumerate(lista_notas):
    print(f"{i+1}ª nota: {nota}")

if media >= 7:
    situacao = "Aprovado."
elif media >= 5:
    situacao = "Recuperação."
else:
    situacao = "Reprovado"
    
print(f"Média: {media}")
print(f"Resultado: {situacao}")


