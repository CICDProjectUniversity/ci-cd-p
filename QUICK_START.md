# 🚀 Быстрый старт - Команды для копирования

## 1️⃣ Создайте репозиторий на GitHub
- Перейдите на https://github.com/new
- Название: `python-ci-cd-project`
- Публичный репозиторий
- НЕ добавляйте README и .gitignore

## 2️⃣ Инициализация проекта

```bash
# Перейдите в папку с проектом
cd python-ci-cd-project

# Инициализация Git
git init

# Добавление всех файлов
git add .

# Первый коммит
git commit -m "Initial commit: настройка CI/CD"

# Подключение к GitHub (ЗАМЕНИТЕ YOUR_USERNAME!)
git remote add origin https://github.com/YOUR_USERNAME/python-ci-cd-project.git

# Отправка на GitHub
git branch -M main
git push -u origin main
```

## 3️⃣ Настройка GitHub Actions

**В браузере на GitHub:**
1. Settings → Actions → General
2. Workflow permissions → "Read and write permissions"
3. ✅ Allow GitHub Actions to create and approve pull requests
4. Save

## 4️⃣ Создание ветки development

```bash
# Создать и переключиться на development
git checkout -b development

# Отправить на GitHub
git push -u origin development
```

## 5️⃣ Проверка CI

**В браузере на GitHub:**
- Перейдите в Actions
- Должен запуститься workflow "CI/CD Pipeline"
- Дождитесь успешного завершения ✅

## 6️⃣ Тестирование автоматического PR

```bash
# Убедитесь что вы на ветке development
git checkout development

# Добавьте новую функцию в calculator.py
cat >> calculator.py << 'EOF'

    def power(self, a: float, b: float) -> float:
        """
        Возведение в степень
        
        Args:
            a: основание
            b: показатель степени
            
        Returns:
            a в степени b
        """
        return a ** b
EOF

# Коммит
git add calculator.py
git commit -m "feat: добавлена функция power"

# Push
git push origin development
```

**Результат:**
- Перейдите на GitHub → Pull Requests
- Через 1-2 минуты появится автоматический PR с документацией! 🎉

## 7️⃣ Создание PR development → main

```bash
# Через GitHub CLI (если есть)
gh pr create --base main --head development --title "Добавлена функция power"

# ИЛИ через веб-интерфейс:
# GitHub → Pull Requests → New pull request
# base: main ← compare: development
```

## 8️⃣ Локальное тестирование

```bash
# Запуск всех тестов
./run_tests.sh

# Или по отдельности
python -m unittest test_calculator.py -v
python -m unittest test_integration.py -v
```

## 9️⃣ Создание релиза

```bash
git checkout main
git pull origin main
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0
```

## ✅ Чек-лист для проверки

- [ ] Репозиторий создан на GitHub
- [ ] Файлы залиты в репозиторий
- [ ] Actions настроены (Read and write permissions)
- [ ] Ветка development создана
- [ ] Workflow запустился при push
- [ ] Тесты прошли успешно
- [ ] Автоматически создался PR с документацией
- [ ] PR можно просмотреть и смёржить

## 📸 Что нужно для отчёта

1. **Скриншот Actions** (зелёные галочки ✅)
2. **Скриншот автоматического PR** с документацией
3. **Скриншот успешных тестов**
4. **Ссылка на репозиторий**

## 🆘 Проблемы?

**Actions не запускаются:**
- Проверьте Settings → Actions → разрешите Actions

**PR не создаётся:**
- Settings → Actions → General → Allow GitHub Actions to create and approve pull requests

**Тесты падают:**
- Запустите локально: `python -m unittest test_calculator.py -v`
- Проверьте логи в Actions

## 📝 Полезные команды

```bash
# Просмотр статуса
git status

# История коммитов
git log --oneline --graph --all

# Переключение веток
git checkout main
git checkout development

# Обновление с удалённого репозитория
git pull origin main

# Просмотр веток
git branch -a
```
