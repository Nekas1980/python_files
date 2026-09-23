# Exercício 12 — Menu para selecionar um dos exercícios 1 a 11
import math
import random
from datetime import date, datetime

def ex1():
    valor = float(input("Valor da compra (€): "))
    print("Tem direito ao prémio: um monitor." if valor > 100 else "Ainda não tem direito ao prémio.")

def ex2():
    numero = int(input("Número inteiro: "))
    print("Par" if numero % 2 == 0 else "Ímpar")

def ex3():
    idade = int(input("Idade: "))
    print("Pode entrar." if idade >= 18 else "Não pode entrar.")

def ex4():
    print(random.choice(["cara", "coroa"]))

def ex5():
    ano = int(input("Ano: "))
    bissexto = (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)
    print("É bissexto." if bissexto else "Não é bissexto.")

def ex6():
    raio = float(input("Raio: "))
    altura = float(input("Altura: "))
    area = 2 * math.pi * raio ** 2 + 2 * math.pi * raio * altura
    print(f"Área total: {area:.2f}")

def ex7():
    idade = int(input("Idade: "))
    if 0 <= idade <= 12:
        print("Criança")
    elif idade <= 17:
        print("Adolescente")
    elif idade <= 64:
        print("Adulto")
    else:
        print("Sénior")

def ex8():
    palavra = input("Palavra: ").strip()
    print("Mais de 5 caracteres." if len(palavra) > 5 else "5 ou menos caracteres.")

def ex9():
    opcoes = ["pedra", "papel", "tesoura"]
    jogador = input("pedra, papel ou tesoura: ").strip().lower()
    computador = random.choice(opcoes)
    if jogador not in opcoes:
        print("Jogada inválida.")
    elif jogador == computador:
        print(f"Computador: {computador}. Empate.")
    elif (jogador, computador) in [("pedra", "tesoura"), ("papel", "pedra"), ("tesoura", "papel")]:
        print(f"Computador: {computador}. Ganhou!")
    else:
        print(f"Computador: {computador}. Perdeu.")

def ex10():
    nascimento = datetime.strptime(input("Nascimento DD/MM/AAAA: "), "%d/%m/%Y").date()
    hoje = date.today()
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
    print("Pode entrar." if idade >= 18 else "Não pode entrar.")

def ex11():
    dias = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]
    numero = int(input("Número de 1 a 7: "))
    print(dias[numero - 1] if 1 <= numero <= 7 else "Número inválido.")

programas = {
    "1": ex1, "2": ex2, "3": ex3, "4": ex4, "5": ex5, "6": ex6,
    "7": ex7, "8": ex8, "9": ex9, "10": ex10, "11": ex11,
}

print("Escolha um exercício de 1 a 11.")
opcao = input("Opção: ").strip()
if opcao in programas:
    programas[opcao]()
else:
    print("Opção inválida.")
