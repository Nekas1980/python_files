# Exercício 7 — Árvore/triângulo centrado de asteriscos
n = int(input("Número de linhas: "))
for linha in range(n):
    espacos = n - linha - 1
    asteriscos = 2 * linha + 1
    print(" " * espacos + "*" * asteriscos)
