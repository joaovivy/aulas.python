import os
os.system("cls || clear")

def calcular_media(primeira_nota, segunda_nota):
    soma = primeira_nota + segunda_nota
    media = soma / 2
    return media

def verificar_resultado(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"
    
primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))

media = calcular_media(primeira_nota, segunda_nota)
resultado = verificar_resultado

print(f"=== RESULTADO ===")
print(f"Média: {media}")
print(f"Resultado: {resultado}")