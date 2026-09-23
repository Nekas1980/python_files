# Exercício 13 — Converter quilómetros para milhas
KM_PARA_MILHAS = 0.621371
quilometros = float(input("Distância em quilómetros: "))
milhas = quilometros * KM_PARA_MILHAS
print(f"{quilometros:g} km equivalem a {milhas:.3f} milhas.")
