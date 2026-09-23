# Exercício 10 — Calcular a média dos elementos de uma lista
numeros = [10, 20, 30, 40, 50]
soma = 0
for numero in numeros:
    soma += numero

if numeros:
    media = soma / len(numeros)
    print(f"Média: {media:.2f}")
else:
    print("Não é possível calcular a média de uma lista vazia.")
