import os
from dataclasses import dataclass

os.system("cls || clear")

# Estrutura de dados.
@dataclass
class Cliente:
    nome: str
    sobrenome: str
    idade: int
    peso: float
    altura: float

QUANTIDADE_CLIENTES = 4

lista_de_clientes = []

print("\n=== Solicitando dados dos clientes ===")
for i in range(QUANTIDADE_CLIENTES):
    cliente = Cliente(
        nome = input("Digite o seu nome: "),
        sobrenome = input("Digite o seu sobrenome: "),
        idade = int(input("Digite sua idade: ")),
        peso = float(input("Digite o seu peso: ")),
        altura = float(input("Digite sua altura: "))
        )
    lista_de_clientes.append(cliente)

print("\n=== Exibindo dados dos clientes ===")
for cliente in lista_de_clientes:
    print(f"Nome: {cliente.nome}")
    print(f"Sobrenome: {cliente.sobrenome}")
    print(f"Idade: {cliente.idade}")
    print(f"Peso: {cliente.peso}")
    print(f"Altura: {cliente.altura}")

# Salvar em um arquivo chamado: carteira_de_clientes.txt
nome_do_arquivo = "carteira_de_clientes.txt"

# Fazer leitura de dados do arquivo carteira_de_clientes.txt e mostre no terminal.
with open(nome_do_arquivo, "a") as arquivo_clientes:
    for cliente in lista_de_clientes:
        arquivo_clientes.write(f"{cliente.nome}, {cliente.sobrenomne}, {cliente.idade}, {cliente.peso}, {cliente.altura}\n")

print("\n=== Dados salvos com sucesso! ===")

lista_de_clientes = []

print("\n=== Acessando dados de um arquivo! ===")
with open(nome_do_arquivo, "a")
