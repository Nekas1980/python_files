# Exercício 19 — Validar e classificar um triângulo
a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

valido = a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a
if not valido:
    print("Os valores não formam um triângulo válido.")
elif a == b == c:
    print("Triângulo equilátero.")
elif a == b or a == c or b == c:
    print("Triângulo isósceles.")
else:
    print("Triângulo escaleno.")
