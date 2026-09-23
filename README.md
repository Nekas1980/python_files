# Python — Formação, Exercícios e Portefólio Técnico

Este repositório é o **hub académico de Python**: exercícios da formação, materiais de estudo, dados de teste e exercícios de scripting.

Os projetos maiores continuam em repositórios próprios e estão indexados em [PROJETOS.md](PROJETOS.md).

## Estrutura

```text
python_files/
├── README.md
├── PROJETOS.md
├── .gitignore
├── bloco-01/
├── bloco-02/
│   ├── 07_classificacao_idade.py
│   └── rascunhos/
├── bloco-03/
├── bloco-05/
├── bloco-07/
├── bloco-08/
│   ├── 01_04_ficheiros_menu.py
│   ├── 05_gerar_turma.py
│   ├── 07_subtrair_semana.py
│   ├── 08_calcular_dias.py
│   ├── dados/
│   └── rascunhos/
├── bloco-09/
├── guia/
└── uc01481-scripting/
    └── exercicio-03/
        ├── analisar_log_ex_3.py
        ├── main_pyaula.py
        ├── README.md
        └── dados/
            └── log_simulado.log
```

## Percurso de aprendizagem

1. **Bloco 1 — Fundamentos**: `print`, `input`, variáveis, tipos de dados, operadores e cálculos simples.
2. **Bloco 2 — Condições**: `if`, `elif`, `else`, operadores relacionais e validações.
3. **Bloco 3 — Ciclo `for`**: `range`, acumulações, padrões, fatorial, tabuadas e números primos.
4. **Bloco 4 — Strings**: métodos de strings, slicing e manipulação de texto.
5. **Bloco 5 — Listas**: percorrer, transformar, ordenar e contar elementos.
6. **Bloco 6 — Ciclo `while`**: repetição condicionada, jogos e conversões.
7. **Bloco 7 — Dicionários**: estruturas chave/valor, inventários, contactos e contagens.
8. **Bloco 8 — Ficheiros, datas, regex e CSV**.
9. **Bloco 9 — Exercícios dinâmicos e integração de vários conceitos**.

## Estado dos ficheiros

- **Soluções**: ficheiros que compilam e estão organizados na pasta do respetivo bloco.
- **Rascunhos**: versões originais com erros de sintaxe ou estrutura, mantidas para estudo e comparação.
- **Dados**: ficheiros `.txt`, `.log` e `.csv` usados pelos exercícios.
- **UC01481 Scripting**: exercícios de análise de logs e automação.

## Repositórios académicos legados

Alguns blocos começaram como repositórios separados e continuam disponíveis para preservar o histórico:

- [Bloco 2](https://github.com/Nekas1980/bloco-2)
- [Bloco 4](https://github.com/Nekas1980/bloco-4)
- [Bloco 6](https://github.com/Nekas1980/bloco_6)

O desenvolvimento académico novo deve ser centralizado aqui em `python_files`.

## Trabalhar em qualquer computador

### Primeira utilização num computador

```bash
git clone https://github.com/Nekas1980/python_files.git
cd python_files
code .
```

### Antes de começar

```bash
git pull
```

### Depois de trabalhar

```bash
git add .
git commit -m "Atualizar exercícios"
git push
```

## Regra de organização

- Um exercício = um ficheiro Python sempre que possível.
- O nome começa pelo número do exercício: `07_nome_exercicio.py`.
- Ficheiros auxiliares ficam em `dados/`.
- Versões incompletas ficam em `rascunhos/`.
- Projetos completos não são misturados com exercícios: ficam em repositórios próprios e são ligados através de [PROJETOS.md](PROJETOS.md).
