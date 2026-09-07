# VS Code + GitHub — Trabalhar em qualquer computador

O objetivo é simples: **GitHub = cópia central**; **VS Code = local onde trabalhas**.

## Primeira utilização num computador

1. Instalar Git e VS Code.
2. Entrar no GitHub com a tua conta.
3. No VS Code abrir a Paleta de Comandos (`Ctrl + Shift + P`).
4. Escolher **Git: Clone**.
5. Colar o endereço do repositório.
6. Escolher a pasta local.
7. Abrir a pasta clonada no VS Code.

Também podes usar o terminal:

```bash
git clone https://github.com/Nekas1980/python_files.git
cd python_files
code .
```

Para repositórios privados, a conta usada no VS Code/Git tem de ter acesso ao repositório.

## Rotina correta em cada sessão

### Antes de começar

```bash
git pull
```

Isto recebe alterações que possam ter sido feitas noutro computador.

### Trabalhar e testar

Exemplo:

```bash
python bloco-03/01_imprimir_numeros.py
```

### Guardar no GitHub

```bash
git status
git add .
git commit -m "Resolver exercício X"
git push
```

## Regra importante

Se trabalhares no computador A e depois fores para o computador B:

```text
Computador A: commit + push
        ↓
GitHub
        ↓
Computador B: pull
```

Antes de mudar novamente de computador, faz o processo inverso.

## Atalhos úteis do VS Code

| Atalho | Função |
|---|---|
| `Ctrl + S` | Guardar ficheiro |
| `Ctrl + \`` | Abrir/fechar terminal integrado |
| `Ctrl + P` | Procurar rapidamente um ficheiro |
| `Ctrl + Shift + P` | Abrir Paleta de Comandos |
| `Ctrl + /` | Comentar/descomentar linhas |
| `Alt + ↑ / ↓` | Mover linha |
| `Ctrl + D` | Selecionar próxima ocorrência |
| `Ctrl + F` | Pesquisar no ficheiro |
| `Ctrl + H` | Pesquisar e substituir |
| `F5` | Executar em modo de debug |
| `Shift + Alt + F` | Formatar o código |

## Repositórios do percurso

```text
Nekas1980/python_files   → índice central + Blocos 1, 3 e 5
Nekas1980/bloco-2        → Bloco 2
Nekas1980/bloco-4        → Bloco 4
Nekas1980/bloco_6        → Bloco 6
```

Quando forem criados repositórios próprios para os Blocos 1, 3 e 5, os respetivos conteúdos podem ser transferidos sem perder esta estrutura de estudo.
