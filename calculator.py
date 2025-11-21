"""
Простой калькулятор для демонстрации CI/CD
"""


class Calculator:
    """Класс калькулятора с базовыми операциями"""
    
    def add(self, a: float, b: float) -> float:
        """
        Сложение двух чисел
        
        Args:
            a: первое число
            b: второе число
            
        Returns:
            Сумма чисел a и b
        """
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """
        Вычитание двух чисел
        
        Args:
            a: уменьшаемое
            b: вычитаемое
            
        Returns:
            Разность чисел a и b
        """
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """
        Умножение двух чисел
        
        Args:
            a: первый множитель
            b: второй множитель
            
        Returns:
            Произведение чисел a и b
        """
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        """
        Деление двух чисел
        
        Args:
            a: делимое
            b: делитель
            
        Returns:
            Частное от деления a на b
            
        Raises:
            ValueError: если b равно нулю
        """
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b


if __name__ == "__main__":
    calc = Calculator()
    print(f"2 + 3 = {calc.add(2, 3)}")
    print(f"5 - 2 = {calc.subtract(5, 2)}")
    print(f"4 * 3 = {calc.multiply(4, 3)}")
    print(f"10 / 2 = {calc.divide(10, 2)}")
