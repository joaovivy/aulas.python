import os
os.system("cls || clear") # Limpa o terminal.

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

if primeiro_numero > segundo_numero:
    maior = primeiro_numero
    menor = segundo_numero
else:
    maior = segundo_numero
    menor = primeiro_numero

print(f"Maior valor {maior} ")
print(f"Menor valor {menor}")