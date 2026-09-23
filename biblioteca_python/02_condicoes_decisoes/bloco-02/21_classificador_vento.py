# Exercício 21 — Classificador de vento (escala simplificada)
# Limites adotados: <1 Calmo | 1-19 Brisa | 20-61 Vento forte | >=62 Tempestade
velocidade = float(input("Velocidade do vento (km/h): "))
if velocidade < 0:
    print("A velocidade não pode ser negativa.")
elif velocidade < 1:
    print("Calmo")
elif velocidade < 20:
    print("Brisa")
elif velocidade < 62:
    print("Vento forte")
else:
    print("Tempestade")
