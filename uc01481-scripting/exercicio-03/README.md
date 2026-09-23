# Exercício 3 — Ranking de endereços IP

Objetivo: ler um ficheiro de log, localizar endereços IPv4, contar ocorrências e ordenar o ranking.

## Ficheiros

- `analisar_log_ex_3.py` — versão desenvolvida durante a aula, com saída explicativa.
- `main_pyaula.py` — versão ajustada ao formato exato do avaliador automático PyAula.
- `dados/log_simulado.log` — ficheiro de treino.

## Diferença importante no PyAula

O avaliador fornece o caminho do ficheiro através de `input()` e espera apenas linhas no formato:

```text
10.0.0.8 3
172.16.0.2 2
```

Por isso, a versão automática não imprime títulos, prompts ou mensagens adicionais.
