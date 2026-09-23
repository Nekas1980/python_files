# Exercício 5 — Contar quantas vezes um elemento aparece numa lista
frutas = ["maçã", "banana", "maçã", "laranja", "maçã", "uva"]
procurar = input("Elemento a contar: ").strip()
contador = 0
for fruta in frutas:
    if fruta == procurar:
        contador += 1
print(f"{procurar!r} aparece {contador} vez(es).")
