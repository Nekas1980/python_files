# Exercício 10 — Entrada na discoteca usando a data de nascimento
from datetime import date, datetime

texto = input("Data de nascimento (DD/MM/AAAA): ").strip()

try:
    nascimento = datetime.strptime(texto, "%d/%m/%Y").date()
    hoje = date.today()
    idade = hoje.year - nascimento.year
    if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
        idade -= 1
    if idade >= 18:
        print(f"Idade: {idade}. Pode entrar na discoteca.")
    else:
        print(f"Idade: {idade}. Não pode entrar na discoteca.")
except ValueError:
    print("Data inválida. Use o formato DD/MM/AAAA.")
