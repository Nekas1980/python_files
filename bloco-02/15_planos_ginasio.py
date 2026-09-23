# Exercício 15 — Planos do ginásio
precos = {
    "básico": 25.0,
    "basico": 25.0,
    "intermédio": 40.0,
    "intermedio": 40.0,
    "premium": 60.0,
}
plano = input("Plano (básico/intermédio/premium): ").strip().lower()
meses = int(input("Número de meses: "))

if plano not in precos:
    print("Plano não reconhecido. Escolha entre básico, intermédio ou premium.")
elif meses <= 0:
    print("O número de meses deve ser superior a zero.")
else:
    total_sem_desconto = precos[plano] * meses
    if meses >= 12:
        percentagem = 0.20
    elif meses >= 6:
        percentagem = 0.10
    else:
        percentagem = 0.0
    desconto = total_sem_desconto * percentagem
    total_com_desconto = total_sem_desconto - desconto
    print(f"Total sem desconto: {total_sem_desconto:.2f} €")
    print(f"Desconto: {desconto:.2f} € ({percentagem * 100:.0f}%)")
    print(f"Total com desconto: {total_com_desconto:.2f} €")
