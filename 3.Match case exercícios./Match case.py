import os
os.system("cls || clear") # Limpa o terminal.

print("""
1 - cadastrar usuário
2 - excluir usuário
3 - sair do sistema
      """)

opcao = int(input("Digite uma ação: "))

match(opcao):
    case 1:
        print("Opção de cadastrar o usuário.")
    case 2:
        print("Opção de excluir o usuário.")
    case 3: 
        print("Opção de sair do sistema.")
    case _:
        print("Opção inválida.")