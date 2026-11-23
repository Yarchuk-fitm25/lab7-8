# Скриншоти до лабораторної №7–8

**Робимо скрін лише після виконання вказаного кроку.** Код фотографуємо у VS Code, результат команд у CMD. Секретні ключі та `.env` на скріншоти не виносимо.

## Завдання 1. Моделі Django

1. Відкрити `django_project/planner/models.py`. **Скрін №1:** класи `Course`, `Label`. Підпис: «Створення моделей навчального предмета та позначки у Django».
2. Нижня частина `models.py` з `Task` і `TaskPlan`, видно `ForeignKey`, `ManyToManyField`, `OneToOneField`. **Скрін №2.** Підпис: «Реалізація трьох типів зв'язків між моделями Django».
3. Скрін структури папки `planner/migrations` після ознайомлення з міграціями. **Скрін №3.** Підпис: «Структура моделей і файлів міграцій Django».

## Завдання 2. Django-міграції

4. Після `manage.py migrate` зробити **скрін №4** з рядками `Applying planner.0001_initial... OK` та `planner.0002_task_is_important... OK`. Підпис: «Застосування двох міграцій бази даних Django».
5. Після `manage.py showmigrations planner` зробити **скрін №5**. Підпис: «Перевірка стану міграцій Django».
6. Після `manage.py sqlmigrate planner 0002` зробити **скрін №6**. Підпис: «Перегляд SQL-команд для другої міграції Django».
7. Відкрити `0002_task_is_important.py`. **Скрін №7.** Підпис: «Додавання поля важливості завдання через другу міграцію».

## Завдання 3. Flask-SQLAlchemy

8. Відкрити `flask_project/models.py`, верх із `task_labels`, `Course`, `Label`. **Скрін №8.** Підпис: «Створення моделей і проміжної таблиці зв'язку в Flask-SQLAlchemy».
9. Нижня частина `models.py` з `Task`, `TaskPlan`, `db.relationship`. **Скрін №9.** Підпис: «Налаштування зв'язків між таблицями Flask-SQLAlchemy».
10. Фрагмент `app.py` з `SQLALCHEMY_DATABASE_URI` і `migrate.init_app`. **Скрін №10.** Підпис: «Підключення SQLite та Flask-Migrate до Flask-додатка».
11. Після `flask db history`, `flask db upgrade`, `flask db current` зробити **скрін №11**. Підпис: «Перевірка двох ревізій і застосування міграцій Flask-Migrate».
12. Структура `migrations/versions/` з файлами `0001`, `0002`. **Скрін №12.** Підпис: «Файли початкової та другої міграцій Flask».

## Завдання 4. ORM-запити

13. Відкрити `django_project/orm_demo.py`, показати `create`, `filter`, `exclude`, `Q`, `aggregate`, `annotate`. **Скрін №13.** Підпис: «CRUD-операції та аналітичні запити через Django ORM».
14. Після запуску `venv\\Scripts\\python.exe orm_demo.py` у Django. **Скрін №14.** Підпис: «Результати CRUD і ORM-запитів Django у CMD».
15. Відкрити `flask_project/orm_demo.py`, показати `db.session.commit`, `rollback` та CRUD. **Скрін №15.** Підпис: «CRUD-операції та керування транзакціями у Flask-SQLAlchemy».
16. Після запуску `orm_demo.py` у Flask. **Скрін №16.** Підпис: «Результати ORM-операцій і перевірки транзакцій Flask».

## Завдання 5. PyTest

17. Відкрити `django_project/tests/conftest.py` і `test_models.py`. **Скрін №17.** Підпис: «Фікстури та параметризовані тести моделей Django».
18. Після `python -m pytest -v` у Django. **Скрін №18.** Підпис: «Результати автоматизованого тестування моделей Django».
19. Відкрити `flask_project/tests/conftest.py` і `test_models.py`. **Скрін №19.** Підпис: «Фікстури тимчасової бази даних та тести Flask».
20. Після `python -m pytest -v` у Flask. **Скрін №20.** Підпис: «Результати автоматизованого тестування моделей Flask».

## Завдання 6. HTTP-тести

21. Відкрити `django_project/tests/test_views.py`. **Скрін №21.** Підпис: «Тестування маршрутів, статус-кодів і POST-запитів Django».
22. Відкрити `flask_project/tests/test_views.py`. **Скрін №22.** Підпис: «Інтеграційні HTTP-тести Flask через тестовий клієнт».
23. За бажанням зробити скрін `/tasks/` та `/tasks/add/` у браузері після запуску `orm_demo.py`. **Скрін №23.** Підпис: «Перевірка сторінок планувальника навчальних завдань».

## Завдання 7. Моки й покриття

24. Відкрити `tests/test_mocks.py` Django, видно два тести та `assert_called_once_with`. **Скрін №24.** Підпис: «Мок-тестування надсилання повідомлення та поточного року в Django».
25. Аналогічний `tests/test_mocks.py` Flask. **Скрін №25.** Підпис: «Ізоляція зовнішніх і внутрішніх залежностей у Flask-тестах».
26. Запустити `pytest -v --cov=planner --cov-report=term-missing` у Django. **Скрін №26.** Підпис: «Аналіз покриття коду Django за допомогою pytest-cov».
27. Запустити `pytest -v --cov=app --cov=models --cov=forms --cov=helpers --cov=notifications --cov-report=term-missing` у Flask. **Скрін №27.** Підпис: «Аналіз покриття коду Flask за допомогою pytest-cov».

**Примітка:** якщо тест не пройшов, не видавай його за успішний. Надішли скрін помилки, виправимо код і повторимо запуск.
