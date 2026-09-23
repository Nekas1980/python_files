# Exercício 23 — Nota de combustível
# O enunciado só fixa "baixo" para valores inferiores a 30 €.
# Nesta solução: <30 baixo; 30-60 médio; >60 elevado.
DESCONTO_CARTAO_POR_LITRO = 0.10

litros = float(input("Litros abastecidos: "))
preco_litro = float(input("Preço por litro (€): "))
tem_cartao = input("Usa cartão com desconto? (sim/não): ").strip().lower() == "sim"

total_bruto = litros * preco_litro
desconto = litros * DESCONTO_CARTAO_POR_LITRO if tem_cartao else 0.0
total_final = max(0.0, total_bruto - desconto)

if total_final < 30:
    classificacao = "baixo"
elif total_final <= 60:
    classificacao = "médio"
else:
    classificacao = "elevado"

print(f"Total bruto: {total_bruto:.2f} €")
print(f"Desconto em cartão: {desconto:.2f} €")
print(f"Total a pagar: {total_final:.2f} €")
print(f"Gasto classificado como: {classificacao}.")
