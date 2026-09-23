# Exercício 17 — Simulador de semáforo
cor = input("Cor do semáforo (vermelho/amarelo/verde): ").strip().lower()
if cor == "vermelho":
    print("Pare.")
elif cor == "amarelo":
    print("Atenção: prepare-se para parar.")
elif cor == "verde":
    print("Avance.")
else:
    print("Cor não reconhecida.")
