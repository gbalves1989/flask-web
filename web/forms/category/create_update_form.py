from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired


class CreateUpdateForm(FlaskForm):
    name = StringField(
        label='Nome da Categoria:',
        validators=[
            Length(
                min=5,
                max=20,
                message='Nome deve ter de 5 a 120 caracteres'
            ),
            DataRequired()
        ])

    submit = SubmitField(label='Salvar')
