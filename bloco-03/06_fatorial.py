# Exercício 6 — Fatorial de um número
n = int(input("Introduza um número inteiro não negativo: "))
if n < 0:
    print("O fatorial não está definido para números negativos.")
else:
    fatorial = 1
    for numero in range(1, n + 1):
        fatorial *= numero
    print(f"{n}! = {fatorial}")
