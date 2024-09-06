import os
os.system("cls || clear")

def soma(n1, n2):
    calculo = n1 +n2
    resultado = print(f"{n1} + {n2} = {calculo}")
    return calculo

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

resultado = soma(numero1, numero2)


def subtracao(n1, n2):
    calculo = n1 - n2
    resultado = print(f"{n1} - {n2} = {calculo}")
    return calculo

numero1 = int(input("Digite o primeiro número "))
numero2 = int(input("Digite o segundo número: "))

resultado = subtracao(numero1, numero2)


def divisao(n1, n2):
    calculo = n1 / n2
    resultado = print(f"{n1} / {n2} = {calculo}")
    return calculo

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

resultado = divisao(numero1, numero2)


def multiplicacao(n1, n2):
    calculo = n1 * n2
    resultado = print(f"{n1} x {n2} = {calculo}")
    return calculo

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

resultado = multiplicacao(numero1, numero2)