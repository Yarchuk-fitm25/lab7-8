import os
from flask import Flask, abort, flash, redirect, render_template, request, url_for
from flask_migrate import Migrate
from dotenv import load_dotenv
from forms import TaskForm
from helpers import current_year
from models import Course, Label, Task, TaskPlan, db


migrate = Migrate()


def create_app(test_config=None):
    load_dotenv()
    app = Flask(__name__)
    app.config.update(
        SECRET_KEY=os.environ.get("FLASK_SECRET_KEY", "local-study-only-not-for-production"),
        SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL", "sqlite:///planner.db"),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    if test_config:
        app.config.update(test_config)
    db.init_app(app)
    migrate.init_app(app, db)

    @app.route("/")
    def home():
        tasks = Task.query.order_by(Task.due_date).limit(5).all()
        return render_template("home.html", tasks=tasks, courses_count=Course.query.count(), year=current_year())

    @app.route("/tasks/")
    def task_list():
        query = Task.query.order_by(Task.due_date)
        status = request.args.get("status", "")
        if status in {"todo", "doing", "done"}:
            query = query.filter_by(status=status)
        return render_template("task_list.html", tasks=query.all(), year=current_year())

    @app.route("/tasks/<int:task_id>/")
    def task_detail(task_id):
        task = db.session.get(Task, task_id)
        if task is None:
            abort(404)
        return render_template("task_detail.html", task=task, year=current_year())

    @app.route("/tasks/add/", methods=["GET", "POST"])
    def add_task():
        form = TaskForm()
        form.course_id.choices = [(course.id, course.name) for course in Course.query.order_by(Course.name)]
        form.labels.choices = [(label.id, label.name) for label in Label.query.order_by(Label.name)]
        if form.validate_on_submit():
            if Task.query.filter_by(code=form.code.data).first():
                form.code.errors.append("Такий код уже існує")
            else:
                task = Task(code=form.code.data, title=form.title.data, summary=form.summary.data,
                            due_date=form.due_date.data, course_id=form.course_id.data,
                            priority=form.priority.data, status="todo")
                task.labels = Label.query.filter(Label.id.in_(form.labels.data)).all() if form.labels.data else []
                db.session.add(task)
                db.session.commit()
                flash("Завдання успішно додано.", "success")
                return redirect(url_for("task_list"))
        return render_template("add_task.html", form=form, year=current_year())

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
