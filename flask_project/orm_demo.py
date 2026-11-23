from datetime import date
from app import app
from models import db, Course, Label, Task, TaskPlan


def main():
    with app.app_context():
        course = Course.query.filter_by(code="DEMO-PRG").first()
        if course is None:
            course = Course(name="Основи програмування", code="DEMO-PRG", semester=3, description="Python")
            db.session.add(course)
            db.session.commit()
        label = Label.query.filter_by(name="Домашнє").first()
        if label is None:
            label = Label(name="Домашнє", color="blue", description="Робота вдома")
            db.session.add(label)
            db.session.commit()

        first = Task.query.filter_by(code="DEMO-1").first()
        if first is None:
            first = Task(code="DEMO-1", title="Створити таблиці", summary="Робота з SQLAlchemy",
                         due_date=date(2026, 12, 15), course_id=course.id, priority="high")
            db.session.add(first)
        second = Task.query.filter_by(code="DEMO-2").first()
        if second is None:
            second = Task(code="DEMO-2", title="Написати тести", summary="Перевірка PyTest",
                          due_date=date(2026, 12, 18), course_id=course.id, priority="medium")
            db.session.add(second)
        db.session.commit()
        if label not in first.labels:
            first.labels.append(label)
        if first.plan is None:
            db.session.add(TaskPlan(task_id=first.id, steps="Створити моделі та перевірити запити", planned_hours=3))
        db.session.commit()

        print("1 CREATE:", Task.query.filter(Task.code.like("DEMO-%")).count(), "завдання")
        print("2 READ:", Task.query.filter_by(code="DEMO-1").first().title)
        first.status = "doing"
        db.session.commit()
        print("3 UPDATE:", first.status)
        print("4 FILTER:", [t.code for t in Task.query.filter_by(priority="high").all()])
        print("5 RELATED OBJECTS:", first.course.name, [x.name for x in first.labels])
        print("6 JOIN + COUNT:", db.session.query(Course.name, db.func.count(Task.id)).join(Task).filter(Course.id == course.id).group_by(Course.id).all())
        original = first.title
        first.title = "Тимчасова зміна"
        db.session.flush()
        try:
            raise ValueError("Навмисна помилка для перевірки транзакції")
        except ValueError:
            db.session.rollback()
        db.session.refresh(first)
        print("7 ROLLBACK:", first.title == original)
        first.summary = "Оновлений опис завдання"
        second.summary = "Оновлені тестові сценарії"
        db.session.commit()
        print("8 COMMIT:", first.summary, ";", second.summary)
        db.session.delete(second)
        db.session.commit()
        print("9 DELETE: залишилось", Task.query.filter(Task.code.like("DEMO-%")).count())


if __name__ == "__main__":
    main()
