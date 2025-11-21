#!/bin/bash

echo "================================"
echo "Запуск всех тестов"
echo "================================"
echo ""

echo "→ Запуск unit-тестов..."
python -m unittest test_calculator.py -v
UNIT_RESULT=$?

echo ""
echo "→ Запуск интеграционных тестов..."
python -m unittest test_integration.py -v
INTEGRATION_RESULT=$?

echo ""
echo "================================"
echo "Результаты тестирования"
echo "================================"

if [ $UNIT_RESULT -eq 0 ]; then
    echo "✅ Unit-тесты: PASSED"
else
    echo "❌ Unit-тесты: FAILED"
fi

if [ $INTEGRATION_RESULT -eq 0 ]; then
    echo "✅ Интеграционные тесты: PASSED"
else
    echo "❌ Интеграционные тесты: FAILED"
fi

echo ""

if [ $UNIT_RESULT -eq 0 ] && [ $INTEGRATION_RESULT -eq 0 ]; then
    echo "🎉 Все тесты прошли успешно!"
    exit 0
else
    echo "⚠️  Некоторые тесты не прошли"
    exit 1
fi
