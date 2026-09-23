# Define uma função chamada world_function.
def world_function():
    print("Hello, world!")


# Define a função principal do programa.
def main():
    # Esta instrução é executada quando main() é chamada.
    print("Hello")

    # Chama a função definida anteriormente.
    world_function()


# __name__ é uma variável especial do Python.
# Quando este ficheiro é executado diretamente,
# o valor de __name__ é "__main__".
if __name__ == "__main__":
    # Inicia o programa chamando a função principal.
    main()
