from datetime import datetime  # Importamos a ferramenta para gerir datas

def calcular_diferenca_dias():
    print("=======================================")
    print("    DIFERENÇA EM DIAS ENTRE DATAS      ")
    print("=======================================")

    while True:
        print("\n(Usa o formato DD/MM/YYYY - ex: 09/10/2026)")
        data1_input = input("Introduz a primeira data (ou 'sair'): ").strip()

        if data1_input.lower() == "sair":
            print("Programa encerrado.")
            break

        data2_input = input("Introduz a segunda data: ").strip()

        try:
            data1 = datetime.strptime(data1_input, "%d/%m/%Y")
            data2 = datetime.strptime(data2_input, "%d/%m/%Y")
            diferenca = data2 - data1
            total_dias = abs(diferenca.days)

            print("---------------------------------------")
            print(f"✓ Data Inicial: {data1_input}")
            print(f"✓ Data Final:   {data2_input}")
            print(f"✓ Resposta:     {total_dias} dias")
            print("---------------------------------------")
            break

        except ValueError:
            print(" Erro: Formato de data inválido! Garante que usas as barras: DD/MM/YYYY (ex: 03/10/2026).")
        except Exception as e:
            print(f" Ocorreu um erro inesperado: {e}")
            break

if __name__ == "__main__":
    calcular_diferenca_dias()
