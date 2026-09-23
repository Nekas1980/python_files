# O bloco try contém código que pode provocar uma exceção.
try:
    # A variável x não foi definida de propósito.
    # Ao tentar utilizá-la, Python gera NameError.
    print(x)

# Este bloco trata especificamente o erro NameError.
except NameError:
    print("A variável x não está definida")

# Este bloco apanha outros tipos de exceção não tratados acima.
except Exception as erro:
    # Mostra uma mensagem e também o detalhe técnico do erro.
    print(f"Algo correu mal: {erro}")
