# Fundamentos de scripting — guia de revisão

Este diretório acompanha a matéria de **Scripting na Cibersegurança**.

---

## 1. Funções — `01_hello_world_funcao.py`

Código:

```python
def world_function():
    print("Hello, world!")

world_function()
```

### Explicação linha a linha

**Linha 1 — `def world_function():`**

- `def` significa **define**.
- Indica ao Python que estamos a criar uma função.
- `world_function` é o nome escolhido para a função.
- Os parênteses `()` indicam a zona onde poderiam existir parâmetros.
- Os dois pontos `:` indicam que começa o bloco da função.

**Linha 2 — `print("Hello, world!")`**

- Está indentada, logo pertence à função.
- `print()` escreve informação no terminal.
- `"Hello, world!"` é uma string, ou seja, texto.

**Linha 4 — `world_function()`**

- Chama/executa a função.
- Definir uma função não significa executá-la.
- A execução só acontece quando fazemos a chamada.

---

## 2. Função principal — `02_funcao_main.py`

Código essencial:

```python
def world_function():
    print("Hello, world!")

def main():
    print("Hello")
    world_function()

if __name__ == "__main__":
    main()
```

### Explicação linha a linha

**`def world_function():`**

Cria uma função reutilizável.

**`print("Hello, world!")`**

Mostra a mensagem no ecrã.

**`def main():`**

Cria a função `main`, utilizada como ponto principal de organização do programa.

**`print("Hello")`**

É a primeira ação executada dentro de `main()`.

**`world_function()`**

A função `main()` chama outra função. Isto permite dividir um programa em blocos menores.

**`if __name__ == "__main__":`**

- `__name__` é uma variável especial criada automaticamente pelo Python.
- Se o ficheiro estiver a ser executado diretamente, `__name__` recebe o valor `"__main__"`.
- O `if` testa essa condição.
- Isto evita executar automaticamente `main()` quando o ficheiro é importado por outro programa.

**`main()`**

Inicia a execução da lógica principal.

---

## 3. Tratamento de exceções — `03_try_except.py`

Código essencial:

```python
try:
    print(x)
except NameError:
    print("A variável x não está definida")
except Exception as erro:
    print(f"Algo correu mal: {erro}")
```

### Explicação linha a linha

**`try:`**

Inicia um bloco de código que o Python vai tentar executar.

**`print(x)`**

Tenta mostrar o valor de `x`. Como `x` não foi definida, é gerado um `NameError`.

**`except NameError:`**

Captura especificamente o erro provocado pela utilização de uma variável inexistente.

**`print("A variável x não está definida")`**

Apresenta uma mensagem compreensível em vez de terminar o programa abruptamente.

**`except Exception as erro:`**

Captura outras exceções que sejam subclasses de `Exception`.

**`as erro`**

Guarda o objeto da exceção na variável `erro`.

**`print(f"Algo correu mal: {erro}")`**

Utiliza uma *f-string* para apresentar a mensagem juntamente com o detalhe da exceção.

---

## Ideia principal para a aula

Uma boa forma de explicar é:

> Uma função é um bloco de código com uma tarefa concreta.  
> A função `main()` organiza o ponto de entrada do programa.  
> O `try/except` permite controlar erros previsíveis sem deixar o programa terminar de forma descontrolada.
