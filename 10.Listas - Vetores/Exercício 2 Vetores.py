import os

os.system("cls || clear")

# Entrada.
QUANTIDADE_NOTAS = 3
lista_notas = []

print("\n=== Solicitando dados ===")
for i in range(QUANTIDADE_NOTAS):   
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota)

# Processamento.
soma = sum(lista_notas)
media = soma / QUANTIDADE_NOTAS

# Saída.
print("\n=== Exibindo resultados ===")
for i, nota in enumerate (lista_notas):
    print(f"{i+1}ª nota: {nota}")
    
print(f"Média: {media}")