"""
Простой калькулятор для демонстрации CI/CD
"""


def add(a, b):
    """Складывает два числа"""
    return a + b


def subtract(a, b):
    """Вычитает второе число из первого"""
    return a - b


def multiply(a, b):
    """Умножает два числа"""
    return a * b


def divide(a, b):
    """Делит первое число на второе"""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b


def power(a, b):
    """Возводит первое число в степень второго"""
    return a ** b


def modulo(a, b):
    """Возвращает остаток от деления"""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a % b
development


def square(a):
    """Возводит число в квадрат"""
    return a ** 2

 main
