# Exercício 14 — Custo de envio de uma encomenda
peso = float(input("Peso da encomenda (kg): "))
if peso <= 0:
    print("O peso deve ser superior a zero.")
elif peso <= 1:
    custo = 2.50
elif peso <= 5:
    custo = 4.00
elif peso <= 20:
    custo = 7.50
else:
    custo = 15.00

if peso > 0:
    print(f"Custo de envio: {custo:.2f} €")
