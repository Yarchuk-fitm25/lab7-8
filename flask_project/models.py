from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


task_labels = db.Table(
    "task_labels",
    db.Column("task_id", db.Integer, db.ForeignKey("task.id", ondelete="CASCADE"), primary_key=True),
    db.Column("label_id", db.Integer, db.ForeignKey("label.id", ondelete="CASCADE"), primary_key=True),
)


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    code = db.Column(db.String(15), nullable=False, unique=True)
    semester = db.Column(db.Integer, nullable=False, default=1)
    description = db.Column(db.Text, nullable=False, default="")

    def __str__(self):
        return self.name


class Label(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False, unique=True)
    color = db.Column(db.String(10), nullable=False, default="blue")
    description = db.Column(db.String(150), nullable=False, default="")

    def __str__(self):
        return self.name


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), nullable=False, unique=True)
    title = db.Column(db.String(120), nullable=False)
    summary = db.Column(db.Text, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    priority = db.Column(db.String(10), nullable=False, default="medium")
    status = db.Column(db.String(10), nullable=False, default="todo")
    course_id = db.Column(db.Integer, db.ForeignKey("course.id", ondelete="RESTRICT"), nullable=False)
    is_important = db.Column(db.Boolean, nullable=False, default=False, server_default="0")

    course = db.relationship("Course", backref=db.backref("tasks", lazy=True))
    labels = db.relationship("Label", secondary=task_labels, backref=db.backref("tasks", lazy=True), lazy=True)
    plan = db.relationship("TaskPlan", backref=db.backref("task", uselist=False), uselist=False,
                           cascade="all, delete-orphan")

    def __str__(self):
        return self.title


class TaskPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey("task.id", ondelete="CASCADE"), nullable=False, unique=True)
    steps = db.Column(db.Text, nullable=False)
    planned_hours = db.Column(db.Integer, nullable=False, default=1)
    resource_url = db.Column(db.String(250), nullable=False, default="")
    notes = db.Column(db.Text, nullable=False, default="")

    def __str__(self):
        return f"План: {self.task.title}"
