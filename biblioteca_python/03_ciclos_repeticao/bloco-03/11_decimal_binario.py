# Exercício 11 — Converter decimal para binário por divisões sucessivas
numero = int(input("Número decimal não negativo: "))

if numero < 0:
    print("Introduza um número não negativo.")
elif numero == 0:
    print("Binário: 0")
else:
    quociente = numero
    restos = []
    for _ in range(numero):
        restos.append(str(quociente % 2))
        quociente //= 2
        if quociente == 0:
            break
    binario = "".join(reversed(restos))
    print(f"Binário: {binario}")
