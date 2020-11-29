from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, SelectField, DateField, BooleanField
from wtforms.validators import DataRequired, Length


class SearchFlight(FlaskForm):
    name = StringField('Imię', validators=[DataRequired()])
    surname = StringField('Nazwisko', validators=[DataRequired()])
    documentType = SelectField('Typ dokumentu', choices=[('1', 'Dowod osobisty'), ('2', 'Paszport')])
    documentNumber = StringField('Numer dokumentu', validators=[DataRequired()])
    flightId = SelectField('ID lotu', choices=[])
    submit = SubmitField('Rezerwuj')
