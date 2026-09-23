# Exercício 14 — Conversor bidirecional euros ↔ libras
# Taxa de estudo fixa e fácil de alterar.
LIBRAS_POR_EURO = 0.86
print("1 - Euros para libras")
print("2 - Libras para euros")
opcao = input("Escolha a direção da conversão: ").strip()
valor = float(input("Valor a converter: "))
if opcao == "1":
    convertido = valor * LIBRAS_POR_EURO
    print(f"{valor:.2f} € equivalem a {convertido:.2f} £.")
elif opcao == "2":
    convertido = valor / LIBRAS_POR_EURO
    print(f"{valor:.2f} £ equivalem a {convertido:.2f} €.")
else:
    print("Opção inválida.")
