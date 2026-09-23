# Exercício 16 — Velocidade média
distancia = float(input("Distância percorrida (km): "))
tempo = float(input("Tempo gasto (horas): "))
if tempo <= 0:
    print("O tempo deve ser superior a zero.")
else:
    velocidade_media = distancia / tempo
    print(f"Velocidade média: {velocidade_media:.2f} km/h")
