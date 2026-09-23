# Exercício 16 — Romanos ↔ árabes (1 a 10)
arabes_para_romanos = {
    1: "I", 2: "II", 3: "III", 4: "IV", 5: "V",
    6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X",
}
romanos_para_arabes = {romano: numero for numero, romano in arabes_para_romanos.items()}

print("1 - Árabe para romano")
print("2 - Romano para árabe")
opcao = input("Opção: ").strip()

if opcao == "1":
    numero = int(input("Número árabe (1-10): "))
    print(arabes_para_romanos.get(numero, "Número fora do intervalo 1-10."))
elif opcao == "2":
    romano = input("Número romano (I-X): ").strip().upper()
    print(romanos_para_arabes.get(romano, "Número romano inválido."))
else:
    print("Opção inválida.")
