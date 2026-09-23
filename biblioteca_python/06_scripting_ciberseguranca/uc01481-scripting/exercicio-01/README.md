# Exercício 1 — Análise de ficheiros de log

## Requisitos do enunciado

O programa deve:

1. receber o caminho para `log_simulado.log`;
2. abrir e ler o ficheiro;
3. contar o número total de linhas;
4. contar linhas que contenham `ERROR`;
5. contar linhas que contenham `WARNING`;
6. utilizar `readlines()`;
7. utilizar `try/except`;
8. opcionalmente utilizar `strip()` no caminho introduzido.

## Ficheiros desta pasta

- `analisar_log.py` — versão direta e simples, ideal para explicar em aula sem funções.
- `analisar_log_com_funcoes.py` — versão modular para estudar funções e `main()`.

---

# Versão simples — explicação linha a linha

### `caminho_ficheiro = input(...).strip()`

- `input()` pára o programa e espera que o utilizador escreva algo.
- O texto introduzido é uma `str`.
- `.strip()` remove espaços e quebras de linha no início e fim.
- O resultado fica guardado na variável `caminho_ficheiro`.

### `try:`

Indica que as instruções seguintes podem provocar uma exceção que queremos controlar.

### `with open(caminho_ficheiro, "r", encoding="utf-8") as ficheiro:`

- `open()` abre o ficheiro.
- `caminho_ficheiro` indica qual ficheiro abrir.
- `"r"` significa *read*: modo de leitura.
- `encoding="utf-8"` indica a codificação.
- `as ficheiro` cria a variável usada para trabalhar com o ficheiro.
- `with` garante que o ficheiro é fechado corretamente.

### `linhas = ficheiro.readlines()`

- `readlines()` lê todas as linhas.
- O resultado é uma lista.
- Cada elemento da lista corresponde normalmente a uma linha do ficheiro.

### `total_linhas = len(linhas)`

- `len()` conta os elementos da lista.
- Como cada elemento representa uma linha, obtemos o total de linhas.

### `total_erros = 0`

Cria o contador de erros e começa em zero.

### `total_warnings = 0`

Cria o contador de avisos e começa em zero.

### `for linha in linhas:`

Percorre a lista uma linha de cada vez.

### `if "ERROR" in linha:`

Verifica se a sequência de caracteres `ERROR` existe na linha atual.

### `total_erros += 1`

É uma forma abreviada de escrever:

```python
total_erros = total_erros + 1
```

### `if "WARNING" in linha:`

Verifica se a linha atual contém `WARNING`.

### `total_warnings += 1`

Incrementa o contador de warnings.

### `print(f"Total de linhas: {total_linhas}")`

- `print()` mostra informação.
- O prefixo `f` cria uma *f-string*.
- `{total_linhas}` é substituído pelo valor da variável.

O mesmo princípio aplica-se às linhas que mostram `total_erros` e `total_warnings`.

### `except FileNotFoundError:`

É executado se o caminho introduzido não corresponder a um ficheiro existente.

### `except OSError as erro:`

Trata outros erros de sistema relacionados com o ficheiro.

### `print(f"Erro ao abrir ou ler o ficheiro: {erro}")`

Apresenta ao utilizador o detalhe do erro capturado.

---

# Versão com funções — conceitos adicionais

### `def analisar_log(caminho_ficheiro):`

Cria uma função que recebe o caminho do ficheiro como parâmetro.

### `"""..."""`

É uma *docstring*: documentação interna da função.

### `sum(1 for linha in linhas if "ERROR" in linha)`

Esta expressão:

1. percorre cada `linha`;
2. verifica se contém `ERROR`;
3. produz o valor `1` quando a condição é verdadeira;
4. `sum()` soma todos esses valores.

É uma forma compacta de fazer um contador.

### `return total_linhas, total_erros, total_warnings`

Termina a função e devolve três valores.

### `def main():`

Cria a função principal, onde organizamos a interação com o utilizador.

### `total_linhas, total_erros, total_warnings = analisar_log(caminho_ficheiro)`

Chama `analisar_log()` e faz *unpacking* dos três valores devolvidos.

### `if __name__ == "__main__":`

Confirma que o ficheiro está a ser executado diretamente.

### `main()`

Arranca a lógica principal do programa.

---

## Como executar

A partir desta pasta:

```powershell
py analisar_log.py
```

ou:

```bash
python analisar_log.py
```

Quando o programa pedir o caminho, podes indicar, por exemplo:

```text
../exercicio-03/dados/log_simulado.log
```

Se estiveres na raiz do repositório:

```powershell
py uc01481-scripting/exercicio-01/analisar_log.py
```

e depois indicar:

```text
uc01481-scripting/exercicio-03/dados/log_simulado.log
```

---

## Perguntas de revisão

1. Qual é a diferença entre `read()`, `readline()` e `readlines()`?
2. Porque começamos os contadores em zero?
3. O que significa `"ERROR" in linha`?
4. Para que serve `try/except`?
5. Qual é a vantagem de usar `with open(...)`?
6. O que acontece se o ficheiro não existir?
7. Qual é a diferença entre definir uma função e chamá-la?
8. Para que serve `return`?
9. O que faz `if __name__ == "__main__":`?
10. Porque uma versão com funções é mais fácil de reutilizar?
