# Mapa de Estudo — Introdução à Programação em Python

Este guia organiza os apontamentos e exercícios por ordem pedagógica, para ser fácil perceber **o que cada conceito faz** e **em que bloco é praticado**.

## 1. Programação e algoritmos

**Programação** é escrever e organizar código para o computador realizar tarefas específicas.

Um **algoritmo** é uma sequência de passos. A ideia é semelhante a uma receita: existe uma ordem e cada passo tem uma finalidade.

Antes de escrever Python, é útil perguntar:

- O que entra no programa?
- Que processamento é necessário?
- Há alguma decisão?
- Há alguma repetição?
- O que deve sair no final?

## 2. Fluxogramas

Os fluxogramas representam visualmente o algoritmo.

Conceitos principais:

- **Início/Fim** — delimita o programa.
- **Entrada/Saída** — receber dados ou apresentar resultados.
- **Processamento** — cálculos ou transformações.
- **Decisão** — condição com caminhos diferentes, por exemplo “é par?”.

Os exercícios iniciais devem ser pensados primeiro como fluxograma e só depois convertidos para Python.

## 3. Variáveis e tipos de dados

Uma **variável** guarda um valor na memória e tem um nome que permite voltar a utilizar esse valor.

Exemplos:

```python
idade = 46          # int
altura = 1.80       # float
nome = "Nelson"     # str
ativo = True        # bool
```

Boas práticas:

- usar nomes descritivos;
- usar `snake_case` em Python;
- não começar o nome por um número;
- não usar espaços;
- lembrar que `idade` e `Idade` são nomes diferentes.

## 4. Entrada, saída e conversão de dados

```python
nome = input("Nome: ")
idade = int(input("Idade: "))
preco = float(input("Preço: "))
print(f"Olá, {nome}")
```

`input()` devolve texto. Quando é necessário calcular com números, é habitual converter com `int()` ou `float()`.

**Bloco principal:** Bloco 1.

## 5. Operadores

### Aritméticos

- `+` adição
- `-` subtração
- `*` multiplicação
- `/` divisão
- `//` divisão inteira
- `**` potência
- `%` resto da divisão

### Relacionais

- `==`, `!=`, `>`, `<`, `>=`, `<=`

O resultado de uma comparação é `True` ou `False`.

### Lógicos

- `and` — as duas condições têm de ser verdadeiras;
- `or` — pelo menos uma condição é verdadeira;
- `not` — inverte o resultado lógico.

## 6. Funções

Uma função é um bloco reutilizável de código que executa uma tarefa específica.

```python
def somar(x, y):
    return x + y

resultado = somar(4, 7)
print(resultado)
```

- `def` cria a função;
- os valores recebidos chamam-se parâmetros;
- `return` devolve um resultado.

Uma estrutura organizada pode usar:

```python
def main():
    pass

if __name__ == "__main__":
    main()
```

Isto define um ponto de entrada e evita que o programa seja executado automaticamente quando o ficheiro é importado.

## 7. Decisões — `if`, `elif`, `else`

Usam-se quando o programa precisa de escolher um caminho.

```python
if idade < 18:
    print("Menor de idade")
elif idade < 65:
    print("Adulto")
else:
    print("Sénior")
```

**Bloco principal:** Bloco 2.

## 8. Ciclo `for`

Usa-se normalmente quando sabemos quantas repetições queremos realizar ou quando percorremos uma sequência.

```python
for numero in range(1, 6):
    print(numero)
```

**Blocos principais:** Bloco 3 e Bloco 5.

## 9. Listas

Uma lista guarda vários valores numa única variável.

```python
frutas = ["maçã", "banana", "laranja", "uva"]

for fruta in frutas:
    print(fruta)
```

Depois aprende-se a somar, contar, inverter, ordenar, filtrar e separar elementos.

**Bloco principal:** Bloco 5.

## 10. Ciclo `while`

Repete enquanto uma condição for verdadeira.

```python
contador = 1
while contador <= 5:
    print(contador)
    contador += 1
```

Ao estudar `while`, verificar sempre:

1. qual é a condição;
2. o que muda em cada repetição;
3. como o ciclo termina.

**Bloco principal:** Bloco 6.

## Ordem recomendada de estudo

```text
Algoritmos e fluxogramas
        ↓
Variáveis e tipos
        ↓
input / print / operadores
        ↓
Funções
        ↓
if / elif / else
        ↓
for / range
        ↓
strings e métodos
        ↓
listas
        ↓
while
```

A regra de trabalho é: **ler o problema → desenhar a lógica → programar → executar → testar → corrigir → documentar → enviar para GitHub**.
