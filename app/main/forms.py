from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField(
        'Nome do Professor',
        validators=[DataRequired()]
    )

    role = SelectField(
        'Disciplina:',
        choices=[],
        validators=[DataRequired()]
    )

    submit = SubmitField('Cadastrar')

