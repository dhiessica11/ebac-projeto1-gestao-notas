# Gestão de Notas Acadêmicas — Projeto 1 EBAC

Projeto autoral em **Python 3** com inicializador **Shell Script (Bash)**, criado para a atividade *Pratique | Projeto 1 (módulo 3)*. A aplicação permite registrar alunos e notas, calcular médias e emitir um relatório no terminal.

## Funcionalidades

- Cadastro de diversos alunos na mesma execução.
- Registro de 1 a 10 notas por aluno, no intervalo de 0 a 10.
- Aceita vírgula ou ponto como separador decimal.
- Cálculo da média aritmética por aluno.
- Classificação **APROVADO** para média maior ou igual a 7 e **REPROVADO** caso contrário.
- Relatório com alunos, situação, totais e média geral.
- Validação de entradas e menu interativo.
- Testes unitários sem dependências externas.

> Os registros são mantidos somente na memória durante a execução. O projeto é demonstrativo e não utiliza banco de dados.

## Estrutura

```text
ebac-projeto1/
├── gestor_notas.py          # Aplicação Python
├── executar.sh              # Inicializador Bash
├── tests/
│   └── test_gestor_notas.py # Testes unitários
├── .gitignore
└── README.md                # Documentação
```

## Pré-requisitos

- Python 3.10 ou superior;
- Bash (macOS, Linux ou WSL no Windows).

## Como executar o arquivo .sh

No terminal, entre na pasta do projeto e execute:

```bash
chmod +x executar.sh
./executar.sh
```

O script identifica a pasta em que está localizado, confere se o comando `python3` está disponível e executa `gestor_notas.py`. Não é preciso instalar pacotes.

### Execução direta em Python

```bash
python3 gestor_notas.py
```

### Testes automatizados

```bash
python3 -m unittest discover -s tests -v
```

## Exemplo de uso

```text
=== GESTÃO DE NOTAS ===
1 - Cadastrar aluno e notas
2 - Exibir relatório
0 - Sair
Escolha: 1
Nome do aluno: Marina
Quantas notas deseja informar (1 a 10)? 3
Nota 1 (0 a 10): 8
Nota 2 (0 a 10): 7,5
Nota 3 (0 a 10): 9
Registro salvo: Marina | Média: 8.17 | APROVADO
```

## Como o código funciona

1. `main()` apresenta um menu em laço `while` e guarda os resultados durante a sessão.
2. `cadastrar_aluno()` solicita nome e quantidade de notas.
3. `solicitar_nota()` transforma a entrada em `float` e rejeita valores fora do intervalo.
4. `calcular_media()` utiliza `statistics.mean` e valida a lista recebida.
5. `avaliar_aluno()` utiliza a nota mínima de aprovação para classificar cada registro; o resultado é representado pela classe `Resultado` (`dataclass`).
6. `exibir_relatorio()` apresenta médias, situação e totais de alunos cadastrados.
7. `executar.sh` automatiza a inicialização no terminal.

## Conceitos demonstrados

Python, variáveis, listas, tuplas, funções, parâmetros, retorno, condições, repetição, validação de dados, tratamento de exceções, módulos da biblioteca padrão, testes unitários, Bash, Git e GitHub.

## Autoria e finalidade

Projeto desenvolvido para estudo e entrega acadêmica na EBAC. Implementação independente, sem reutilização do código da calculadora compartilhada como referência.
