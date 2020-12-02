from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, SelectField, DateField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length


class SearchFlight(FlaskForm):
    name = StringField('Imię', validators=[DataRequired()])
    surname = StringField('Nazwisko', validators=[DataRequired()])
    documentType = SelectField('Typ dokumentu', choices=[('1', 'Dowod osobisty'), ('2', 'Paszport')])
    documentNumber = StringField('Numer dokumentu', validators=[DataRequired()])
    flightId = SelectField('ID lotu', choices=[])
    submit = SubmitField('Rezerwuj')


class AddFlight(FlaskForm):
    id = StringField('ID lotu', validators=[DataRequired(), Length(min=6, max=6)])
    depAir = SelectField('Lotnisko startowe', choices=[])
    arrAir = SelectField('Lotnisko docelowe', choices=[])
    depDate = StringField('Data wylotu', validators=[DataRequired()])
    arrDate = StringField('Data przylotu', validators=[DataRequired()])
    airplanes = SelectField('ID samolotu', choices=[])
    price = FloatField('Cena', validators=[DataRequired()])
    submit = SubmitField('Dodaj')


class AddAirplane(FlaskForm):
    id = StringField('ID samolotu', validators=[DataRequired(), Length(min=4, max=6)])
    capacity = IntegerField('Pojemność', validators=[DataRequired()])
    airline = SelectField('Linia lotnicza', choices=[('1', 'RyanAir'), ('2', 'WizzAir')])
    submit = SubmitField('Dodaj')


class EditPrice(FlaskForm):
    flightId = SelectField('ID lotu', choices=[])
    price = FloatField('Cena', validators=[DataRequired()])
    submit = SubmitField('Edytuj')


class DeleteFlightPassenger(FlaskForm):
    passengerId = SelectField('Rezerwacje', choices=[])
    submit = SubmitField('Usuń')
