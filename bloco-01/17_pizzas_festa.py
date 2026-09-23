# Exercício 17 — Quantas pizzas são necessárias para uma festa
# O enunciado não define as fatias por pizza.
# Nesta solução assume-se 8 fatias por pizza; a constante pode ser alterada.
import math
FATIAS_POR_PIZZA = 8
pessoas = int(input("Número de pessoas: "))
fatias_por_pessoa = int(input("Fatias por pessoa: "))
fatias_necessarias = pessoas * fatias_por_pessoa
pizzas = math.ceil(fatias_necessarias / FATIAS_POR_PIZZA)
print(f"São necessárias {pizzas} pizza(s).")
