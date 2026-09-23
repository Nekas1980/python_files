# Exercício 20 — Simulador de caixa multibanco
saldo = float(input("Saldo disponível (€): "))
levantamento = float(input("Valor a levantar (€): "))

if levantamento <= 0:
    print("O valor a levantar deve ser superior a zero.")
elif levantamento > saldo:
    print("Operação recusada: saldo insuficiente.")
else:
    saldo_final = saldo - levantamento
    print("Operação autorizada.")
    print(f"Saldo restante: {saldo_final:.2f} €")
