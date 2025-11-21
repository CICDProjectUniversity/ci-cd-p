"""
Unit-тесты для калькулятора
"""
import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Тесты для класса Calculator"""
    
    def setUp(self):
        """Инициализация перед каждым тестом"""
        self.calc = Calculator()
    
    def test_add(self):
        """Тест сложения"""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
    
    def test_subtract(self):
        """Тест вычитания"""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
    
    def test_multiply(self):
        """Тест умножения"""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 5), 0)
    
    def test_divide(self):
        """Тест деления"""
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(-6, 2), -3)
    
    def test_divide_by_zero(self):
        """Тест деления на ноль"""
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)


if __name__ == "__main__":
    unittest.main()
