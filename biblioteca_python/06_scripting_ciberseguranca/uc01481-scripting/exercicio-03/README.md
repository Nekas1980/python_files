# Exercício 3 — Ranking de endereços IP

Objetivo: ler um ficheiro de log, localizar endereços IPv4, contar ocorrências e ordenar o ranking.

## Ficheiros

- `analisar_log_ex_3.py` — versão desenvolvida durante a aula, com saída explicativa.
- `main_pyaula.py` — versão ajustada ao formato exato do avaliador automático PyAula.
- `log_simulado.log` — cópia direta do ficheiro usado no exercício, colocada ao lado do código para facilitar a execução.
- `dados/log_simulado.log` — mesma base de dados de treino, mantida na pasta de dados.

## Execução rápida

A partir da pasta `uc01481-scripting/exercicio-03`:

```powershell
py .\main_pyaula.py
```

O programa fica à espera do caminho do ficheiro porque usa apenas:

```python
caminho_ficheiro = input()
```

Escreve então:

```text
log_simulado.log
```

e carrega Enter.

Também podes executar a versão explicativa:

```powershell
py .\analisar_log_ex_3.py
```

e indicar igualmente:

```text
log_simulado.log
```

## Diferença importante no PyAula

O avaliador fornece o caminho do ficheiro através de `input()` e espera apenas linhas no formato:

```text
10.0.0.8 3
172.16.0.2 2
```

Por isso, a versão automática não imprime títulos, prompts ou mensagens adicionais.
