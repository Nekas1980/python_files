# Auditoria de logs — IPs suspeitos

## Objetivo

Ler um ficheiro de log, considerar apenas linhas `ERROR` e `WARNING`, contar alertas por IP e apresentar os IPs com 3 ou mais alertas.

## Conceitos

- `input()`
- `try/except`
- `with open(...)`
- `readlines()`
- `for`
- `if`
- expressões regulares com `re`
- dicionários
- listas
- `.items()`
- `.append()`
- `.sort()`

## Execução

```powershell
py analise_timestamps.py
```

Quando o programa ficar à espera, introduzir apenas o caminho do ficheiro de log.

Exemplo:

```text
log_simulado.log
```

O ficheiro de dados deve permanecer separado do código para permitir analisar diferentes logs sem alterar o programa.
