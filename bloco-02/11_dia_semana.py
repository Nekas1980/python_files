# Exercício 11 — Número de 1 a 7 para dia da semana
dias = {
    1: "segunda-feira",
    2: "terça-feira",
    3: "quarta-feira",
    4: "quinta-feira",
    5: "sexta-feira",
    6: "sábado",
    7: "domingo",
}
numero = int(input("Introduza um número de 1 a 7: "))
if numero in dias:
    print(dias[numero])
else:
    print("Número inválido.")
