# Exercício 8 — Verificar se uma palavra tem mais de 5 caracteres
palavra = input("Introduza uma palavra: ").strip()
if len(palavra) > 5:
    print("A palavra tem mais de 5 caracteres.")
else:
    print("A palavra tem 5 ou menos caracteres.")
