# Exercício 14 — Remover números negativos de uma lista
numeros = [5, -3, 8, -1, 0, 12, -7]
sem_negativos = []
for numero in numeros:
    if numero >= 0:
        sem_negativos.append(numero)
print(sem_negativos)
