# Exercício 4 — Soma dos múltiplos de 3 ou 5 abaixo de X
x = int(input("Somar múltiplos de 3 ou 5 abaixo de: "))
soma = 0
for numero in range(x):
    if numero % 3 == 0 or numero % 5 == 0:
        soma += numero
print(f"Soma: {soma}")
