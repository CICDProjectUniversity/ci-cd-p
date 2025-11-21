#!/usr/bin/env python3
"""
Скрипт для автоматической генерации документации
"""
import inspect
import sys
from datetime import datetime
from pathlib import Path

# Импортируем модуль calculator
sys.path.insert(0, '.')
import calculator


def generate_docs():
    """Генерирует Markdown документацию из docstrings"""
    
    # Создаём директорию для документации
    docs_dir = Path('docs')
    docs_dir.mkdir(exist_ok=True)
    
    # Получаем класс Calculator
    calc_class = calculator.Calculator
    
    # Начинаем формировать документацию
    doc_lines = []
    doc_lines.append("# Документация проекта Calculator\n")
    doc_lines.append(f"**Дата обновления:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    doc_lines.append("")
    doc_lines.append("## Описание\n")
    doc_lines.append("Простой калькулятор с базовыми математическими операциями.\n")
    doc_lines.append("")
    doc_lines.append("## Класс Calculator\n")
    
    # Получаем docstring класса
    if calc_class.__doc__:
        doc_lines.append(f"{calc_class.__doc__.strip()}\n")
        doc_lines.append("")
    
    doc_lines.append("### Методы:\n")
    
    # Перебираем все методы класса
    for name, method in inspect.getmembers(calc_class, predicate=inspect.isfunction):
        if name.startswith('_'):  # Пропускаем приватные методы
            continue
        
        # Получаем сигнатуру метода
        sig = inspect.signature(method)
        doc_lines.append(f"#### `{name}{sig}`\n")
        
        # Получаем docstring метода
        if method.__doc__:
            docstring = method.__doc__.strip()
            doc_lines.append(f"{docstring}\n")
        
        doc_lines.append("---\n")
        doc_lines.append("")
    
    # Добавляем примеры использования
    doc_lines.append("## Примеры использования\n")
    doc_lines.append("```python")
    doc_lines.append("from calculator import Calculator")
    doc_lines.append("")
    doc_lines.append("calc = Calculator()")
    doc_lines.append("")
    doc_lines.append("# Сложение")
    doc_lines.append("result = calc.add(2, 3)      # 5")
    doc_lines.append("")
    doc_lines.append("# Вычитание")
    doc_lines.append("result = calc.subtract(5, 2)  # 3")
    doc_lines.append("")
    doc_lines.append("# Умножение")
    doc_lines.append("result = calc.multiply(4, 3)  # 12")
    doc_lines.append("")
    doc_lines.append("# Деление")
    doc_lines.append("result = calc.divide(10, 2)   # 5.0")
    doc_lines.append("```\n")
    
    # Добавляем информацию о тестировании
    doc_lines.append("## Тестирование\n")
    doc_lines.append("Проект включает unit-тесты и интеграционные тесты:\n")
    doc_lines.append("```bash")
    doc_lines.append("# Запуск всех тестов")
    doc_lines.append("python -m unittest discover -v")
    doc_lines.append("")
    doc_lines.append("# Запуск конкретных тестов")
    doc_lines.append("python -m unittest test_calculator.py -v")
    doc_lines.append("python -m unittest test_integration.py -v")
    doc_lines.append("```\n")
    
    # Добавляем структуру проекта
    doc_lines.append("## Структура проекта\n")
    doc_lines.append("```")
    doc_lines.append(".")
    doc_lines.append("├── calculator.py           # Основной модуль")
    doc_lines.append("├── test_calculator.py      # Unit-тесты")
    doc_lines.append("├── test_integration.py     # Интеграционные тесты")
    doc_lines.append("├── requirements.txt        # Зависимости")
    doc_lines.append("├── generate_docs.py        # Скрипт генерации документации")
    doc_lines.append("└── docs/                   # Документация (автогенерация)")
    doc_lines.append("    └── README.md")
    doc_lines.append("```\n")
    
    # Добавляем footer
    doc_lines.append("---\n")
    doc_lines.append("*Документация автоматически генерируется при каждом изменении кода через GitHub Actions.*")
    
    # Записываем в файл
    readme_path = docs_dir / 'README.md'
    readme_path.write_text('\n'.join(doc_lines))
    
    print(f"✅ Документация успешно сгенерирована: {readme_path}")
    print(f"📝 Создано {len(doc_lines)} строк документации")


if __name__ == '__main__':
    try:
        generate_docs()
    except Exception as e:
        print(f"❌ Ошибка при генерации документации: {e}")
        sys.exit(1)
