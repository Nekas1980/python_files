import re  # Importamos a biblioteca de Expressões Regulares (Regex)

# 1. Uso do 'def' para estruturar a tua função de validação
def validar_email_utilizador():
    print("=======================================")
    print("       VALIDADOR DE EMAIL (REGEX)      ")
    print("=======================================")

    padrao_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    while True:
        email_input = input("\nIntroduz um email para validar (ou 'sair'): ").strip()

        if email_input.lower() == "sair":
            print("Programa encerrado.")
            break

        ão segura
        try:
            if re.match(padrao_email, email_input):
                print("---------------------------------------")
                print(f" O email '{email_input}' é VÁLIDO!")
                print("---------------------------------------")
                break
            else:
                print("Erro: Estrutura de email inválida! Garante que tem '@' e '.' (ex: teste@dominio.com).")

        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            break

if __name__ == "__main__":
    email = input("Introduz um email para validar: ")
    validar_email_utilizador()
