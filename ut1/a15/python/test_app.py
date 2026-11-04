import unittest
from main import calcular

class TestCalculadora(unittest.TestCase):
    def test_operaciones_correctas(self):
        self.assertEqual(calcular(10, 5, "+"), 15)
        self.assertEqual(calcular(10, 2, "/"), 5)

    def test_division_por_cero(self):
        with self.assertRaises(ZeroDivisionError):
            calcular(10, 0, "/")

    def test_fallido_intencional(self):
        self.assertEqual(calcular(2, 2, "+"), 5)

if __name__ == "__main__":
    unittest.main()
