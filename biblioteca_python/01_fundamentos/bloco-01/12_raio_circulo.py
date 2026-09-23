# Exercício 12 — Calcular o raio a partir da área de um círculo
import math
area = float(input("Área do círculo: "))
if area < 0:
    print("A área não pode ser negativa.")
else:
    raio = math.sqrt(area / math.pi)
    print(f"Raio: {raio:.4f}")
