# Exercício 8 — Cálculo do IMC
peso = float(input("Peso em kg: "))
altura = float(input("Altura em metros: "))

if altura <= 0:
    print("A altura deve ser superior a zero.")
else:
    imc = peso / (altura ** 2)
    print(f"IMC: {imc:.2f}")
