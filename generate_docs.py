import os
from datetime import datetime

DOCS_DIR = "docs"

def main():
    os.makedirs(DOCS_DIR, exist_ok=True)

    # index
    with open(os.path.join(DOCS_DIR, "index.md"), "w", encoding="utf-8") as f:
        f.write(
            "# Python Calculator\n\n"
            "Это документация для проекта калькулятора.\n\n"
            "## Разделы\n"
            "- [API](api.md)\n"
            "- [История изменений](CHANGELOG.md)\n"
        )

    # api
    with open(os.path.join(DOCS_DIR, "api.md"), "w", encoding="utf-8") as f:
        f.write(
            "# API Reference\n\n"
            "## Функции\n\n"
            "- `add(a, b)` — сложение\n"
            "- `subtract(a, b)` — вычитание\n"
            "- `multiply(a, b)` — умножение\n"
            "- `divide(a, b)` — деление\n"
        )

    # changelog
    with open(os.path.join(DOCS_DIR, "CHANGELOG.md"), "w", encoding="utf-8") as f:
        f.write(
            "# Changelog\n\n"
            f"- Документация сгенерирована: {datetime.now()}\n"
        )

    print("Документация успешно сгенерирована.")


if __name__ == "__main__":
    main()

