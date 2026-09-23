# Exercício 11 — Conversor de euros para dólares
# Taxa fixa indicada no enunciado: 1 € = 1,08 $
TAXA_EUR_USD = 1.08
euros = float(input("Valor em euros: "))
dolares = euros * TAXA_EUR_USD
print(f"{euros:.2f} € equivalem a {dolares:.2f} $.")
