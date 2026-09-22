import re

ips_encontrados = set()

contagem_ips = {}

#def analisar_log():

caminho_ficheiro = input("Indica o caminho do ficheiro .log")

try:

    with open(caminho_ficheiro, "r", encoding="utf-8", errors="ignore") as ficheiro:

        contagem_ips = {}

        padrao_ip = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

        for linha in ficheiro:

            ips_encontrados = re.findall(padrao_ip, linha)

            for ip in ips_encontrados:

                if ip in contagem_ips:

                    contagem_ips[ip] += 1

                else:

                    contagem_ips[ip] = 1

except FileNotFoundError:

    print("Erro: o ficheirp não existe.")

except OSError as erro:

    print(f"Erro ao abrir o ficheiro: {erro}")

ranking = sorted(

    contagem_ips.items(),

    key=lambda item: item[1],

    reverse=True

)

print("\n== Ranking de endereços IP ==")

if not ranking:

    print("Não foram encontrados IP no ficheiro.")

for posicao, (ip, ocorrencias) in enumerate(ranking, start=1):

    print(f"{posicao:>2}. {ip} - {ocorrencias} ocorrencias")
