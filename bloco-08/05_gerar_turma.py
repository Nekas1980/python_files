import os  # Biblioteca necessária para verificar se o ficheiro já existe

def gerar_tabela_turma():
    print("=======================================")
    print("      REGISTO DE NOTAS DA TURMA        ")
    print("=======================================")

    nomes = []
    notas = []

    # 1. Recolha de dados no 'while'
    while True:
        nome = input("\nNome do aluno (ou 'sair' para gravar): ").strip()
        if nome.lower() == "sair":
            break

        nota = input(f"Nota do(a) {nome}: ").strip()
        nomes.append(nome)
        notas.append(nota)

    if len(nomes) == 0:
        print("Nenhum aluno adicionado nesta sessão.")
        return

    # 2. Uso do 'try/except' com inteligência de Append
    try:
        ficheiro_ja_existe = os.path.exists("turma.txt")

        with open("turma.txt", "a", encoding="utf-8") as ficheiro:
            tam_nome = 20
            tam_nota = 6

            if not ficheiro_ja_existe:
                cabecalho = "Nome".ljust(tam_nome) + " | " + "Nota".ljust(tam_nota) + "\n"
                separador = "-" * (tam_nome + tam_nota + 3) + "\n"
                ficheiro.write(cabecalho)
                ficheiro.write(separador)

            for i in range(len(nomes)):
                linha_tabela = nomes[i].ljust(tam_nome) + " | " + notas[i].ljust(tam_nota) + "\n"
                ficheiro.write(linha_tabela)

        print("\n✓ Sucesso! Os novos alunos foram acrescentados a 'turma.txt'.")

        print("\n Conteudo Actualizado")
        with open("turma.txt", "r", encoding="utf-8") as f_read:
            for linha in f_read:
                print(linha, end="")
        print("===========================================")

    except Exception as e:
        print(f"Ocorreu um erro ao gravar o ficheiro: {e}")

if __name__ == "__main__":
    gerar_tabela_turma()
