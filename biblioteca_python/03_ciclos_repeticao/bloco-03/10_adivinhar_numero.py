# Exercício 10 — Adivinhar o número em 3 tentativas
import random

segredo = random.randint(0, 10)
acertou = False

for tentativa in range(1, 4):
    palpite = int(input(f"Tentativa {tentativa}/3 — número de 0 a 10: "))
    if palpite == segredo:
        print("Acertou!")
        acertou = True
        break
    elif palpite < segredo:
        print("O número secreto é maior.")
    else:
        print("O número secreto é menor.")

if not acertou:
    print(f"Esgotou as tentativas. O número era {segredo}.")
