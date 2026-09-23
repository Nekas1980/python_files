# Soma dos primeiros N números naturais.

def soma(N):
    soma_total = 0
    for i in range(1, N + 1):
        soma_total += i
    return soma_total


if __name__ == "__main__":
    try:
        N = int(input("Digite um número inteiro positivo: "))
        if N < 0:
            print("Por favor, digite um número inteiro positivo.")
        else:
            resultado = soma(N)
            print(f"A soma dos primeiros {N} números naturais é: {resultado}")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
