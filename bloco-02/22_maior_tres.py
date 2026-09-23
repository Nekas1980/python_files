# Exercício 22 — Maior de três números sem usar max()
a = float(input("Primeiro número: "))
b = float(input("Segundo número: "))
c = float(input("Terceiro número: "))
maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c
print(f"O maior número é {maior:g}.")
