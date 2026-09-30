import re
from datetime import datetime


if __name__ == "__main__":

    nome = input()

    try:
        with open(nome, "r", encoding="utf-8") as ficheiro:
            linhas = ficheiro.readlines()

    except OSError:
        pass

    else:
        for linha in linhas:

            resultado_syslog = re.search(
                r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}",
                linha
            )

            if resultado_syslog:
                print(resultado_syslog.group())

            else:
                resultado_apache = re.search(
                    r"\[([^\]]+)\]",
                    linha
                )

                if resultado_apache:
                    try:
                        data = datetime.strptime(
                            resultado_apache.group(1),
                            "%d/%b/%Y:%H:%M:%S %z"
                        )

                        normalizado = data.strftime(
                            "%Y-%m-%d %H:%M:%S"
                        )

                        print(normalizado)

                    except ValueError:
                        pass
