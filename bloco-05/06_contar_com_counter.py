# Exercício 6 — Contar elementos usando collections.Counter
from collections import Counter

frutas = ["maçã", "banana", "maçã", "laranja", "maçã", "uva"]
contagens = Counter(frutas)
procurar = input("Elemento a contar: ").strip()
print(f"{procurar!r} aparece {contagens[procurar]} vez(es).")
