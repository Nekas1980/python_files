# Exercício 6 — Área total de um cilindro
import math

def area_circle(ray):
    return math.pi * pow(ray, 2)

def area_cylinder(ray, height):
    area_bases = 2 * area_circle(ray)
    area_lateral = 2 * math.pi * ray * height
    return area_bases + area_lateral

raio = float(input("Raio do cilindro: "))
altura = float(input("Altura do cilindro: "))
print(f"Área total do cilindro: {area_cylinder(raio, altura):.2f}")
