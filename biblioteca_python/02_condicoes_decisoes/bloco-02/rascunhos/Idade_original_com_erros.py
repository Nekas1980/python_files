

def classifica_idade(idade):
    if 0 <= idade <= 12:
        return "Criança"
    elif 13 <= idade <= 17:
        return "Adolescente"
    elif 12 <= idade <= 64:
        return "Adulto"
    elif idade >= 65:
        return "Sénior"

if__name__ == "__main__":
    idade = int(input("Digite a sua idade: "))
    classificacao = classifica_idade(idade)
    print(f"Você é classificado como: {classificacao}")
