import os
os.system("cls || clear")

def calcular_imc(altura, peso):
    calculo = peso / altura ** 2
    return calculo

def verificar_classificacao(imc):
    if imc < 18.5:
        return "Abaixo do peso."
    elif imc < 24.9:
        return "Peso normal."
    elif imc < 29.9:
        return "Sobrepeso."
    elif imc < 34.9:
        return "Obesidade grau I."
    elif imc < 39.9:
        return "Obesidade grau II."
    else:
        return "Obesidade grau III."
    
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = calcular_imc(altura, peso)
classificacao = verificar_classificacao(imc)

print("=== RESULTADO ===")
print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao}")