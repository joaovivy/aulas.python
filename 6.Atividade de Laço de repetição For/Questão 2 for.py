import os
os.system("cls || clear")

numero = int(input("Digite um número para a tabuada: "))

print(f"\nTabuada da soma do número: {numero}") 
for i in range(1,6):
      print(f"{numero} + {i} = {numero + i} ")    