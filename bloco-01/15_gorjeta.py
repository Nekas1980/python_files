# Exercício 15 — Calculadora de gorjeta
conta = float(input("Valor da conta (€): "))
percentagem = float(input("Percentagem de gorjeta (%): "))
gorjeta = conta * percentagem / 100
total = conta + gorjeta
print(f"Gorjeta: {gorjeta:.2f} €")
print(f"Total a pagar: {total:.2f} €")
