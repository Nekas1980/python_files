# Exercício 5 — Verificar se um ano é bissexto
ano = int(input("Introduza um ano: "))
if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print("É bissexto.")
else:
    print("Não é bissexto.")
