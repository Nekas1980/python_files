# Exercício 15 — Encontrar o maior elemento sem usar max()
numeros = [7, 3, 19, 4, 12]

if not numeros:
    print("A lista está vazia.")
else:
    maior = numeros[0]
    for numero in numeros[1:]:
        if numero > maior:
            maior = numero
    print(f"Maior elemento: {maior}")
