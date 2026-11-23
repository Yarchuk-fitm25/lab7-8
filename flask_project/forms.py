from flask_wtf import FlaskForm
from wtforms import DateField, SelectField, SelectMultipleField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class TaskForm(FlaskForm):
    code = StringField("Код завдання", validators=[DataRequired(message="Вкажіть код"), Length(max=20)])
    title = StringField("Назва", validators=[DataRequired(message="Вкажіть назву"), Length(max=120)])
    summary = TextAreaField("Опис", validators=[DataRequired(message="Вкажіть опис")])
    due_date = DateField("Термін", validators=[DataRequired(message="Вкажіть дату")], format="%Y-%m-%d")
    course_id = SelectField("Предмет", coerce=int, validators=[DataRequired(message="Виберіть предмет")])
    priority = SelectField("Пріоритет", choices=[("low", "Низький"), ("medium", "Середній"), ("high", "Високий")])
    labels = SelectMultipleField("Позначки", coerce=int)
    submit = SubmitField("Зберегти")
