"""
Интеграционные тесты для калькулятора
"""
import unittest
from calculator import Calculator


class TestCalculatorIntegration(unittest.TestCase):
    """Интеграционные тесты для проверки комплексных операций"""
    
    def setUp(self):
        """Инициализация перед каждым тестом"""
        self.calc = Calculator()
    
    def test_complex_calculation(self):
        """Тест сложных вычислений: (2 + 3) * 4 / 2"""
        result = self.calc.add(2, 3)
        result = self.calc.multiply(result, 4)
        result = self.calc.divide(result, 2)
        self.assertEqual(result, 10.0)
    
    def test_chain_operations(self):
        """Тест цепочки операций"""
        # Начинаем с 10
        result = 10
        # Вычитаем 3 = 7
        result = self.calc.subtract(result, 3)
        # Умножаем на 2 = 14
        result = self.calc.multiply(result, 2)
        # Делим на 7 = 2
        result = self.calc.divide(result, 7)
        # Прибавляем 8 = 10
        result = self.calc.add(result, 8)
        
        self.assertEqual(result, 10.0)
    
    def test_negative_numbers_workflow(self):
        """Тест работы с отрицательными числами"""
        result = self.calc.subtract(0, 5)  # -5
        result = self.calc.multiply(result, -2)  # 10
        result = self.calc.add(result, -3)  # 7
        result = self.calc.divide(result, -1)  # -7
        
        self.assertEqual(result, -7.0)
    
    def test_fractional_numbers(self):
        """Тест работы с дробными числами"""
        result = self.calc.divide(1, 3)  # 0.333...
        result = self.calc.multiply(result, 3)  # ~1.0
        self.assertAlmostEqual(result, 1.0, places=10)


if __name__ == "__main__":
    unittest.main()
