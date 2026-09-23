# Exercício 7 — Gestor de uma lista de nomes
nomes = []

while True:
    print("\n1. Adicionar nome")
    print("2. Remover nome")
    print("3. Ordenar lista")
    print("4. Mostrar lista")
    print("5. Sair")
    opcao = input("Opção: ").strip()

    if opcao == "1":
        nome = input("Nome a adicionar: ").strip()
        if nome:
            nomes.append(nome)
            print("Nome adicionado.")
    elif opcao == "2":
        nome = input("Nome a remover: ").strip()
        if nome in nomes:
            nomes.remove(nome)
            print("Nome removido.")
        else:
            print("Nome não encontrado.")
    elif opcao == "3":
        nomes.sort(key=str.casefold)
        print("Lista ordenada.")
    elif opcao == "4":
        if nomes:
            for nome in nomes:
                print(f"- {nome}")
        else:
            print("A lista está vazia.")
    elif opcao == "5":
        print("Programa terminado.")
        break
    else:
        print("Opção inválida.")
