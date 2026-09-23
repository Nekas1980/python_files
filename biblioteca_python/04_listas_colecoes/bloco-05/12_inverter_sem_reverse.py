# Exercício 12 — Inverter uma lista sem usar .reverse()
lista = [1, 2, 3, 4, 5]
invertida = []
for indice in range(len(lista) - 1, -1, -1):
    invertida.append(lista[indice])
print(invertida)
