import os
from datetime import datetime


DOCS_DIR = "docs"


def write_file(path, content):
    """Write content into a file."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def generate_index():
    content = (
        "# Python Calculator\n\n"
        "Это документация для проекта калькулятора.\n\n"
        "## Разделы\n"
        "- [API](api.md)\n"
        "- [История изменений](CHANGELOG.md)\n"
    )
    write_file(os.path.join(DOCS_DIR, "index.md"), content)


def generate_api():
    content = (
        "# API Reference\n\n"
        "## Функции\n\n"
        "- `add(a, b)` — сложение\n"
        "- `subtract(a, b)` — вычитание\n"
        "- `multiply(a, b)` — умножение\n"
        "- `divide(a, b)` — деление\n"
    )
    write_file(os.path.join(DOCS_DIR, "api.md"), content)


def generate_changelog():
    timestamp = datetime.now()
    lines = [
        "# Changelog\n",
        f"- Документация сгенерирована: {timestamp}\n",
    ]
    write_file(os.path.join(DOCS_DIR, "CHANGELOG.md"), "".join(lines))


def main():
    os.makedirs(DOCS_DIR, exist_ok=True)
    generate_index()
    generate_api()
    generate_changelog()
    print("Документация успешно сгенерирована.")


if __name__ == "__main__":
    main()
