from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, SelectField, DateField, BooleanField
from wtforms.validators import DataRequired, Length


class AddFlight(FlaskForm):
    id = StringField('Id lotu', validators=[DataRequired(), Length(max=6)])
    depAir = SelectField()
    arrAir = SelectField()


class SearchFlight(FlaskForm):
    depDate = StringField('Data wylotu', validators=[DataRequired()])
    arrDate = StringField('Data przylotu', validators=[DataRequired()])
    submit = SubmitField('Szukaj')
    depAir = SelectField('Wylot', choices=[], validators=[DataRequired()])
    arrAir = SelectField('Przylot', choices=[], validators=[DataRequired()])
    cheap = BooleanField('Czy tanie loty?')
    notEmpty = BooleanField('Czy loty z bez wolnego miejsca?')
