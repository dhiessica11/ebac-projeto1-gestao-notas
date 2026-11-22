"""Testes unitários usando apenas unittest (sem bibliotecas externas)."""
import unittest
from gestor_notas import avaliar_aluno, calcular_media


class TestGestorNotas(unittest.TestCase):
    def test_media(self):
        self.assertEqual(calcular_media([8, 6, 10]), 8)

    def test_aprovacao_limiar(self):
        self.assertEqual(avaliar_aluno("Ana", [7, 7]).situacao, "APROVADO")

    def test_reprovacao(self):
        self.assertEqual(avaliar_aluno("Bia", [5, 6]).situacao, "REPROVADO")

    def test_lista_vazia(self):
        with self.assertRaises(ValueError):
            calcular_media([])

    def test_nota_invalida(self):
        with self.assertRaises(ValueError):
            avaliar_aluno("Ana", [11])

    def test_nome_vazio(self):
        with self.assertRaises(ValueError):
            avaliar_aluno("   ", [8])


if __name__ == "__main__":
    unittest.main()
