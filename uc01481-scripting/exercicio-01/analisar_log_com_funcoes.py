def analisar_log(caminho_ficheiro):
    """Analisa um ficheiro de log e devolve totais de linhas, erros e warnings."""

    # Abre o ficheiro e garante que é fechado automaticamente no final.
    with open(caminho_ficheiro, "r", encoding="utf-8") as ficheiro:
        # Guarda todas as linhas numa lista.
        linhas = ficheiro.readlines()

    # Conta o total de linhas.
    total_linhas = len(linhas)

    # sum() soma 1 por cada linha onde a condição é verdadeira.
    total_erros = sum(1 for linha in linhas if "ERROR" in linha)
    total_warnings = sum(1 for linha in linhas if "WARNING" in linha)

    # Devolve três valores para quem chamou a função.
    return total_linhas, total_erros, total_warnings


def main():
    # Recebe o caminho e remove espaços no início/fim.
    caminho_ficheiro = input("Indica o caminho para o ficheiro .log: ").strip()

    try:
        # Chama a função e distribui os três valores devolvidos.
        total_linhas, total_erros, total_warnings = analisar_log(caminho_ficheiro)

        # Apresenta o relatório.
        print(f"Total de linhas: {total_linhas}")
        print(f"Linhas com ERROR: {total_erros}")
        print(f"Linhas com WARNING: {total_warnings}")

    except FileNotFoundError:
        print("Erro: o ficheiro indicado não existe.")

    except OSError as erro:
        print(f"Erro ao abrir ou ler o ficheiro: {erro}")


# Só chama main() quando este ficheiro é executado diretamente.
if __name__ == "__main__":
    main()
