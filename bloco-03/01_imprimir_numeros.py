# Imprimir números de 1 a x usando um ciclo for.

def imprimir_numeros():
    try:
        x = int(input("Digite um número: "))
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
        return

    if x < 1:
        print("Digite um número maior ou igual a 1.")
        return

    for i in range(1, x + 1):
        print(i)


if __name__ == "__main__":
    imprimir_numeros()
