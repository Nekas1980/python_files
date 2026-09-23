import re

padrao_ip = re.compile(r"\b\d{1,3}(?:\.\d{1,3}){3}\b")
contagem_ips = {}

caminho_ficheiro = input()

try:
    with open(caminho_ficheiro, "r", encoding="utf-8", errors="ignore") as ficheiro:
        for linha in ficheiro:
            for ip in padrao_ip.findall(linha):
                octetos = ip.split(".")
                if all(0 <= int(octeto) <= 255 for octeto in octetos):
                    contagem_ips[ip] = contagem_ips.get(ip, 0) + 1
except (FileNotFoundError, OSError):
    pass

ranking = sorted(
    contagem_ips.items(),
    key=lambda item: (
        -item[1],
        tuple(int(octeto) for octeto in item[0].split("."))
    )
)

for ip, ocorrencias in ranking:
    print(f"{ip} {ocorrencias}")
