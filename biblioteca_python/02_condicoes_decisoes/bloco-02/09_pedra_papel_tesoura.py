# Exercício 9 — Pedra, papel, tesoura
import random

opcoes = ["pedra", "papel", "tesoura"]
jogador = input("Escolha pedra, papel ou tesoura: ").strip().lower()

if jogador not in opcoes:
    print("Jogada inválida.")
else:
    computador = random.choice(opcoes)
    print(f"Computador: {computador}")
    if jogador == computador:
        print("Empate.")
    elif (
        (jogador == "pedra" and computador == "tesoura")
        or (jogador == "papel" and computador == "pedra")
        or (jogador == "tesoura" and computador == "papel")
    ):
        print("Ganhou!")
    else:
        print("O computador ganhou.")
