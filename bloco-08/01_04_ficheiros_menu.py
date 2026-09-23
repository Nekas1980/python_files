def somar(*args):
    return sum(args)


def ler_ficheiro(ficheiro):
    try:
        with open(ficheiro, "r", encoding="utf-8") as f:
            linhas = f.readlines()
            for linha in linhas:
                print(linha, end="")
            print(f"\nNúmero de linhas: {len(linhas)}")
            conteudo = "".join(linhas)
            print(conteudo.upper())
            print(conteudo.lower())
            return conteudo
    except FileNotFoundError:
        print("Não encontro o ficheiro")
    except Exception as e:
        print(f"Erro: {e}")


def criar_ficheiro():
    with open("mensagem.txt", "w", encoding="utf-8") as f:
        f.write("Olá mundo!\nBem-vindo ao CET!\nEu gosto de Python")
    print("Ficheiro 'mensagem.txt' criado com sucesso.")


def reverter_palavras(conteudo):
    palavras = conteudo.split()
    resultado = [palavra[::-1] for palavra in palavras]
    return " ".join(resultado)


def escrever_num_ficheiro():
    ficheiro = "notas.txt"
    frase = input("Escreve as tuas notas: ")
    with open(ficheiro, "a", encoding="utf-8") as f:
        f.write(frase + "\n")
    print(f"Frase guardada em '{ficheiro}'.")


def menu():
    while True:
        print("\nMenu - Ficheiros:")
        print("1. Ler ficheiro")
        print("2. Criar ficheiro")
        print("3. Reverter palavras")
        print("4. Escrever num ficheiro")
        print("5. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            ler_ficheiro("mensagem.txt")
        elif opcao == "2":
            criar_ficheiro()
        elif opcao == "3":
            conteudo = ler_ficheiro("mensagem.txt")
            if conteudo:
                print(reverter_palavras(conteudo))
        elif opcao == "4":
            escrever_num_ficheiro()
        elif opcao == "5":
            print("A sair...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
