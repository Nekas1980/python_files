# Exercício 9 — Números primos até N
n = int(input("Listar números primos até: "))
primos = []

for numero in range(2, n + 1):
    primo = True
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            primo = False
            break
    if primo:
        primos.append(numero)

print(primos)
