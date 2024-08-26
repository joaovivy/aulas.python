import os
import time

os.system("cls || clear")

print("Laço de repetição - For")
for i in range(10,0,-1):
    print(f"Conteúdo da variável i + {i}")
    time.sleep(1) # Vai esperar os segundos.

print("=== FIM ===")