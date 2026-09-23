# Exercício 9 — Converter minutos para horas e minutos
minutos_total = int(input("Introduza o total de minutos: "))
horas = minutos_total // 60
minutos = minutos_total % 60
print(f"{minutos_total} minutos equivalem a {horas} hora(s) e {minutos} minuto(s).")
