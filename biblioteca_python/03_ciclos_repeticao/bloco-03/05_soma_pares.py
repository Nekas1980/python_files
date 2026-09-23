# Exercício 5 — Soma dos números pares até N
n = int(input("Introduza N: "))
soma = 0
for numero in range(2, n + 1, 2):
    soma += numero
print(f"Soma dos pares até {n}: {soma}")
