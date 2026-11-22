"""Sistema interativo de acompanhamento de notas acadêmicas.

Projeto educacional independente, desenvolvido com a biblioteca padrão do Python.
"""

from dataclasses import dataclass
from statistics import mean

NOTA_MINIMA = 0.0
NOTA_MAXIMA = 10.0
MEDIA_APROVACAO = 7.0


@dataclass(frozen=True)
class Resultado:
    nome: str
    notas: tuple[float, ...]
    media: float
    situacao: str


def calcular_media(notas: list[float] | tuple[float, ...]) -> float:
    """Calcula a média aritmética, validando quantidade e intervalo das notas."""
    if not notas:
        raise ValueError("Informe pelo menos uma nota.")
    if any(not 0 <= nota <= 10 for nota in notas):
        raise ValueError("As notas precisam estar entre 0 e 10.")
    return mean(notas)


def avaliar_aluno(nome: str, notas: list[float]) -> Resultado:
    """Gera a situação acadêmica de um aluno a partir das notas."""
    nome = nome.strip()
    if not nome:
        raise ValueError("O nome do aluno não pode estar vazio.")
    media = calcular_media(notas)
    situacao = "APROVADO" if media >= MEDIA_APROVACAO else "REPROVADO"
    return Resultado(nome, tuple(notas), media, situacao)


def solicitar_nota(indice: int) -> float:
    while True:
        entrada = input(f"Nota {indice} (0 a 10): ").strip().replace(",", ".")
        try:
            nota = float(entrada)
            if not (0 <= nota <= 10):
                raise ValueError
            return nota
        except ValueError:
            print("Valor inválido. Digite um número entre 0 e 10.")


def solicitar_quantidade() -> int:
    while True:
        entrada = input("Quantas notas deseja informar (1 a 10)? ").strip()
        if entrada.isdigit() and 1 <= int(entrada) <= 10:
            return int(entrada)
        print("Informe um número inteiro de 1 a 10.")


def cadastrar_aluno() -> Resultado:
    while True:
        nome = input("Nome do aluno: ").strip()
        if nome:
            break
        print("O nome é obrigatório.")
    quantidade = solicitar_quantidade()
    notas = [solicitar_nota(i) for i in range(1, quantidade + 1)]
    return avaliar_aluno(nome, notas)


def exibir_relatorio(resultados: list[Resultado]) -> None:
    if not resultados:
        print("Nenhum aluno cadastrado.")
        return
    print("\n=== RELATÓRIO ACADÊMICO ===")
    print(f"{'ALUNO':<24} {'MÉDIA':>7}  SITUAÇÃO")
    print("-" * 46)
    for resultado in resultados:
        print(f"{resultado.nome[:24]:<24} {resultado.media:>7.2f}  {resultado.situacao}")
    aprovados = sum(r.situacao == "APROVADO" for r in resultados)
    print("-" * 46)
    print(f"Total: {len(resultados)} | Aprovados: {aprovados} | Reprovados: {len(resultados) - aprovados}")
    print(f"Média geral: {mean(r.media for r in resultados):.2f}\n")


def main() -> None:
    resultados: list[Resultado] = []
    while True:
        print("\n=== GESTÃO DE NOTAS ===")
        print("1 - Cadastrar aluno e notas")
        print("2 - Exibir relatório")
        print("0 - Sair")
        opcao = input("Escolha: ").strip()
        if opcao == "1":
            resultado = cadastrar_aluno()
            resultados.append(resultado)
            print(f"Registro salvo: {resultado.nome} | Média: {resultado.media:.2f} | {resultado.situacao}")
        elif opcao == "2":
            exibir_relatorio(resultados)
        elif opcao == "0":
            print("Programa encerrado.")
            return
        else:
            print("Opção inválida. Escolha 0, 1 ou 2.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nExecução encerrada.")
