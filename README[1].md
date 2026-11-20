# Лабораторная работа: CI и модульное тестирование

## Состав проекта
- `calculator.py` — исправленная реализация калькулятора.
- `test_calculator.py` — модульные тесты, включая параметризованные сценарии.
- `.github/workflows/ci.yml` — GitHub Actions: mypy, pytest и покрытие.
- `requirements.txt` — зависимости.

## Запуск локально
Требуется Python 3.10 или новее.

```bash
python -m venv .venv
# Windows:
.venv\\Scripts\\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
mypy calculator.py
pytest --cov=calculator --cov-report=term-missing
```

## Публикация на GitHub
1. Создайте новый репозиторий на GitHub.
2. Откройте терминал в папке проекта.
3. Выполните команды (замените URL на адрес своего репозитория):

```bash
git init
git add .
git commit -m "Complete CI lab"
git branch -M main
git remote add origin https://github.com/ВАШ-АККАУНТ/ВАШ-РЕПОЗИТОРИЙ.git
git push -u origin main
```

4. На GitHub откройте вкладку **Actions** и дождитесь завершения workflow.
5. Убедитесь, что все шаги завершились успешно (зелёная отметка).

Чтобы показать предусмотренный заданием первый неуспешный запуск, сначала отправьте исходный вариант `calculator.py` с ошибками и тесты, затем исправьте калькулятор и отправьте изменения. Если преподаватель требует именно такую демонстрацию, не пропускайте этот этап.

## Исправленные дефекты
- `subtract`: изменён порядок вычитания на `a - b`.
- `multiply`: вместо константы возвращается `a * b`.
- `divide`: при `b == 0` выбрасывается `ValueError`, иначе возвращается `a / b`.
