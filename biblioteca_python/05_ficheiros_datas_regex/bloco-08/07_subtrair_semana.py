from datetime import datetime, timedelta  # Importamos as ferramentas do tempo

def subtrair_semana_com_timestamp():
    print("=======================================")
    print("   SUBTRAIR 1 SEMANA & TIMESTAMP       ")
    print("=======================================")

    while True:
        data_input = input("\nIntroduz uma data (DD MM YYYY) ou 'sair': ").strip()

        if data_input.lower() == "sair":
            print("Programa encerrado.")
            break

        try:
            data_objeto = datetime.strptime(data_input, "%d %m %Y")
            nova_data = data_objeto - timedelta(days=7)
            data_final_formatada = nova_data.strftime("%d %m %Y")
            unix_timestamp = nova_data.timestamp()
            timestamp_log = nova_data.strftime("%Y-%m-%d %H:%M:%S")

            print("---------------------------------------")
            print(f"✓ Data original:       {data_input}")
            print(f"✓ Uma semana antes:    {data_final_formatada}")
            print(f"✓ Timestamp de Redes:  {int(unix_timestamp)} (Segundos Unix)")
            print(f"✓ Timestamp de Log:    {timestamp_log}")
            print("---------------------------------------")
            break

        except ValueError:
            print("Erro: Data inválida! Usa o formato: DD MM YYYY (ex: 27 06 2026).")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            break

if __name__ == "__main__":
    subtrair_semana_com_timestamp()
