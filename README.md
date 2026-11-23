Лабораторна робота №7–8

Тема: Робота з моделями даних, ORM та тестування в Django і Flask.

У цій лабораторній роботі створено два вебдодатки «Планувальник навчальних завдань» на Django та Flask.

У проєктах можна переглядати навчальні завдання, додавати нові та працювати з базою даних SQLite.

Що реалізовано

Чотири моделі: Course, Label, Task, TaskPlan.

Зв'язки між моделями.

Міграції бази даних.

CRUD-операції та ORM-запити.

Автоматизовані тести PyTest.

Мок-тестування та перевірка покриття коду.

Запуск Django

Потрібен Python 3.12.

Відкрити CMD у папці django_project та виконати:

py -3.12 -m venv venv
venv\Scripts\python.exe -m pip install -r requirements.txt
copy .env.example .env

У файлі .env замінити DJANGO_SECRET_KEY на власний випадковий ключ.

Потім виконати:

venv\Scripts\python.exe manage.py migrate
venv\Scripts\python.exe manage.py runserver

Сайт: http://127.0.0.1:8000/

Запуск Flask

Відкрити CMD у папці flask_project та виконати:

py -3.12 -m venv venv
venv\Scripts\python.exe -m pip install -r requirements.txt
copy .env.example .env

У файлі .env замінити FLASK_SECRET_KEY на власний випадковий ключ.

Потім виконати:

venv\Scripts\python.exe -m flask --app app:app db upgrade
venv\Scripts\python.exe app.py

Сайт: http://127.0.0.1:5000/

Робота з ORM

Для перевірки CRUD-операцій і запитів у кожному проєкті є файл orm_demo.py.

Запуск:

venv\Scripts\python.exe orm_demo.py

Тестування

Для запуску тестів у папці відповідного проєкту виконати:

venv\Scripts\python.exe -m pytest -v

Перевірка покриття коду Django:

venv\Scripts\python.exe -m pytest --cov=planner --cov-report=term-missing

Перевірка покриття коду Flask:

venv\Scripts\python.exe -m pytest --cov=app --cov=models --cov=forms --cov=helpers --cov=notifications --cov-report=term-missing

Результати

Під час виконання лабораторної роботи перевірила роботу моделей, міграцій, ORM-запитів та автоматизованих тестів.

Django: 18 успішних тестів, покриття 99%.

Flask: 17 успішних тестів, покриття 97%.

Обидва проєкти працюють із SQLite та мають приблизно однакові можливості.
