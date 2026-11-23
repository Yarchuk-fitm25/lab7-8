# Лабораторна робота №7–8

**Тема:** Моделі даних, ORM-запити, міграції та тестування в Django і Flask.

Це навчальний проєкт **«Планувальник навчальних завдань»**. У ньому можна переглядати предмети і завдання та додавати нові завдання. Є дві реалізації однієї предметної області: Django і Flask.

## Структура

- `django_project` — Django ORM, Django migrations, PyTest.
- `flask_project` — Flask-SQLAlchemy, Flask-Migrate, PyTest.
- `PLAN_SKRINSHOTIV.md` — скріншоти для звіту з підписами.
- `ZVIT_MATERIALY.md` — короткі пояснення й таблиці для звіту.

## Моделі та зв'язки

| Модель | Призначення |
|---|---|
| `Course` | Предмет: назва, код, семестр, опис |
| `Label` | Позначка завдання: назва, колір, опис |
| `Task` | Завдання: код, назва, термін, пріоритет, стан, опис |
| `TaskPlan` | Особистий план виконання: кроки, години, посилання, нотатки |

Зв'язки: `Course` → `Task` (один-до-багатьох, захищене видалення предмета), `Task` ↔ `Label` (багато-до-багатьох), `Task` ↔ `TaskPlan` (один-до-одного, каскадне видалення плану разом із завданням).

**Дві міграції у кожному проєкті:** `0001` створює таблиці, `0002` додає до `Task` поле `is_important`. Файли міграцій уже включені, не змінюйте їх вручну. Для нових змін використовуйте генератори міграцій.

## Потрібні програми

Windows, Python **3.12**, CMD, VS Code, браузер. Після розпакування в `C:\tania` назва основної папки має бути `C:\tania\lab7_8_navchalnyi_planuvalnyk`.

## Django: запуск

Відкрийте CMD:

```bat
cd /d C:\tania\lab7_8_navchalnyi_planuvalnyk\django_project
py -3.12 -m venv venv
venv\Scripts\python.exe -m pip install -r requirements.txt
copy .env.example .env
notepad .env
```

У `.env` замініть значення `DJANGO_SECRET_KEY` на власний випадковий рядок із 32+ символів. Далі:

```bat
venv\Scripts\python.exe manage.py migrate
venv\Scripts\python.exe manage.py showmigrations planner
venv\Scripts\python.exe manage.py sqlmigrate planner 0002
venv\Scripts\python.exe manage.py check
venv\Scripts\python.exe manage.py runserver
```

Сторінки: <http://127.0.0.1:8000/>, <http://127.0.0.1:8000/tasks/>, <http://127.0.0.1:8000/tasks/add/>. Після першого запуску список порожній, це нормально. Дані для демонстрації додає `orm_demo.py`.

У другому CMD для завдання 4:

```bat
cd /d C:\tania\lab7_8_navchalnyi_planuvalnyk\django_project
venv\Scripts\python.exe orm_demo.py
```

Тести та покриття:

```bat
venv\Scripts\python.exe -m pytest -v
venv\Scripts\python.exe -m pytest -v --cov=planner --cov-report=term-missing
```

## Flask: запуск

Відкрийте нове CMD:

```bat
cd /d C:\tania\lab7_8_navchalnyi_planuvalnyk\flask_project
py -3.12 -m venv venv
venv\Scripts\python.exe -m pip install -r requirements.txt
copy .env.example .env
notepad .env
```

У `.env` замініть значення `FLASK_SECRET_KEY` на власний рядок із 32+ символів. Далі:

```bat
venv\Scripts\python.exe -m flask --app app:app db history
venv\Scripts\python.exe -m flask --app app:app db upgrade
venv\Scripts\python.exe -m flask --app app:app db current
venv\Scripts\python.exe app.py
```

У папці `migrations` **уже є середовище Alembic та дві ревізії**, тому повторно виконувати `flask db init` не потрібно. Якщо створюєте міграції в новому порожньому проєкті, послідовність така: `flask db init` → `flask db migrate` → `flask db upgrade`. У цьому архіві початкові файли міграцій уже готові, щоб їх можна було відтворити з нуля командою `db upgrade`.

Сторінки: <http://127.0.0.1:5000/>, <http://127.0.0.1:5000/tasks/>, <http://127.0.0.1:5000/tasks/add/>.

Демонстраційні ORM-операції (в іншому CMD):

```bat
cd /d C:\tania\lab7_8_navchalnyi_planuvalnyk\flask_project
venv\Scripts\python.exe orm_demo.py
```

Тести та покриття:

```bat
venv\Scripts\python.exe -m pytest -v
venv\Scripts\python.exe -m pytest -v --cov=app --cov=models --cov=forms --cov=helpers --cov=notifications --cov-report=term-missing
```

**У тестах Flask** конфігурація `WTF_CSRF_ENABLED=False` діє лише для тимчасового тестового додатка. У звичайному додатку перевірка CSRF залишається увімкненою, і у форму вставлено `form.hidden_tag()`. Відсутня в прикладі помилка з тестуванням CSRF не повинна повторюватися за належного встановлення бібліотек.

## Що потрібно показати для лабораторної

1. Чотири моделі та три зв'язки.
2. Дві послідовні міграції Django, `showmigrations` та `sqlmigrate`.
3. Дві ревізії Flask-Migrate та підключення до SQLite.
4. CRUD та ORM-аналітика у `orm_demo.py`.
5. Фікстури, параметризація та PyTest.
6. Тести HTTP-запитів (статуси 200, 302, 404).
7. Моки надсилання повідомлень і поточного року, coverage.

Детальні підписи до скріншотів є у `PLAN_SKRINSHOTIV.md`. Фактичні результати тестів і відсоток покриття потрібно брати **з власного CMD після запуску**, а не вигадувати числа.

## GitHub

У репозиторій включати код, дві папки `migrations`, `requirements.txt`, `README.md` та `.env.example`. Файли `.env`, `.sqlite3`, `.db`, `venv`, `instance`, `__pycache__` виключає `.gitignore`.
