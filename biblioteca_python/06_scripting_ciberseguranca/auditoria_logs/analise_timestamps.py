import re

if __name__ == "__main__":

    caminho = input()

    try:
        with open(caminho, "r", encoding="utf-8") as ficheiro:
            linhas = ficheiro.readlines()

    except OSError:
        print(f"Nao foi possivel abrir o ficheiro: {caminho}")

    else:
        padrao_ip = re.compile(r"\b\d{1,3}(?:\.\d{1,3}){3}\b")

        alertas = {}

        for linha in linhas:

            if "ERROR" in linha or "WARNING" in linha:

                resultado = padrao_ip.search(linha)

                if resultado:
                    ip = resultado.group()

                    if ip in alertas:
                        alertas[ip] += 1
                    else:
                        alertas[ip] = 1

        suspeitos = []

        for ip, quantidade in alertas.items():

            if quantidade >= 3:
                suspeitos.append((-quantidade, ip))

        suspeitos.sort()

        print("=== RELATORIO DE AUDITORIA ===")
        print(f"Total de linhas analisadas: {len(linhas)}")
        print()
        print("IPs suspeitos (3 ou mais alertas ERROR/WARNING):")

        if suspeitos:
            for quantidade_negativa, ip in suspeitos:
                print(f"  {ip} - {-quantidade_negativa} alertas")
        else:
            print("  (nenhum)")
