# Exercício 8 — Criar uma nova lista apenas com números pares
lista = [1, 2, 3, 4, 5, 6]
pares = []
for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)
