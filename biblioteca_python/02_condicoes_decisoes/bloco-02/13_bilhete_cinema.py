# Exercício 13 — Bilhete de cinema com descontos
PRECO_BASE = 8.50
idade = int(input("Idade: "))
estudante = input("É estudante? (sim/não): ").strip().lower() == "sim"

if idade < 12:
    desconto = 0.50
elif idade >= 65:
    desconto = 0.40
elif estudante:
    desconto = 0.25
else:
    desconto = 0.0

valor_desconto = PRECO_BASE * desconto
preco_final = PRECO_BASE - valor_desconto
print(f"Preço base: {PRECO_BASE:.2f} €")
print(f"Desconto: {valor_desconto:.2f} € ({desconto * 100:.0f}%)")
print(f"Preço final: {preco_final:.2f} €")
