# Exercício 18 — Calculadora de nota final
# Escala assumida: 0 a 20 valores.
# <10 Reprovado; 10-11,9 Suficiente; 12-13,9 Bom; 14-17,9 Muito Bom; 18-20 Excelente.
teste = float(input("Nota do teste (0-20): "))
trabalho = float(input("Nota do trabalho (0-20): "))
media = (teste + trabalho) / 2

if not (0 <= teste <= 20 and 0 <= trabalho <= 20):
    print("As notas devem estar entre 0 e 20.")
elif media < 10:
    classificacao = "Reprovado"
elif media < 12:
    classificacao = "Suficiente"
elif media < 14:
    classificacao = "Bom"
elif media < 18:
    classificacao = "Muito Bom"
else:
    classificacao = "Excelente"

if 0 <= teste <= 20 and 0 <= trabalho <= 20:
    print(f"Média: {media:.2f} — {classificacao}")
