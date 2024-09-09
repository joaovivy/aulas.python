import os
os.system("cls || clear") # Limpa o terminal.

print("""
1 - Domingo
2 - Segunda
3 - Terça
4 - Quarta
5 - Quinta
6 - Sexta
7 - Sábado
      """)

opcao = int(input("Digite o número do dia da semana: "))

match(opcao):
    case 1:
        print("Domingo (final de semana)")
    case 2:
        print("Segunda-feira (dia útil)")
    case 3:
         print("Terça-feira (dia útil)")
    case 4:
        print("Quarta-feira (dia útil)")
    case 5:
        print("Quinta-feira (dia útil)")
    case 6:
        print("Sexta-feira (dia útil)")
    case 7:
        print("Sábado (final de semana)")
    case _:
        print(f"Opção inválida.") 
    


    