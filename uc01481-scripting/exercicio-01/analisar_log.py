# Pede ao utilizador o caminho para o ficheiro de log.
# strip() remove espaços acidentais no início e no fim.
caminho_ficheiro = input("Indica o caminho para o ficheiro .log: ").strip()

# O try protege as operações que podem falhar ao abrir o ficheiro.
try:
    # Abre o ficheiro apenas para leitura.
    # encoding="utf-8" define a codificação do texto.
    with open(caminho_ficheiro, "r", encoding="utf-8") as ficheiro:
        # readlines() lê todas as linhas e devolve uma lista.
        linhas = ficheiro.readlines()

    # len() devolve o número de elementos da lista.
    total_linhas = len(linhas)

    # Começamos os contadores em zero.
    total_erros = 0
    total_warnings = 0

    # Percorre cada linha existente na lista linhas.
    for linha in linhas:
        # Verifica se a palavra ERROR aparece na linha.
        if "ERROR" in linha:
            total_erros += 1

        # Verifica se a palavra WARNING aparece na linha.
        if "WARNING" in linha:
            total_warnings += 1

    # Mostra os resultados finais.
    print(f"Total de linhas: {total_linhas}")
    print(f"Linhas com ERROR: {total_erros}")
    print(f"Linhas com WARNING: {total_warnings}")

# Executado se o caminho indicado não existir.
except FileNotFoundError:
    print("Erro: o ficheiro indicado não existe.")

# Executado se ocorrer outro problema relacionado com abertura/leitura.
except OSError as erro:
    print(f"Erro ao abrir ou ler o ficheiro: {erro}")
