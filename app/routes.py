from flask import render_template, flash, redirect
from app import app, database_connection
from app.forms import SearchFlight

db = database_connection


@app.route('/')
@app.route('/main')
def main():
    return render_template('main.html', title='Strona główna')


@app.route('/database_menegment')
def database_menegment():
    return render_template('dbMenegment.html', title='Zarządzaj')



# search
@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchFlight()
    form.depAir.choices = db.selectAirports()
    form.arrAir.choices = db.selectAirports()

    if form.validate_on_submit():
        depAir = form.depAir.data[-4:-1]
        arrAir = form.arrAir.data[-4:-1]
        flights = db.selectFligths(depAir, arrAir)

    else:
        flash('Coś poszło nie tak!', 'danger')
    return render_template('search.html', title='Szukaj', form=form)



# db menegment

@app.route('/add_flight')
def add_flight():
    return render_template('addFlight.html', title='Dodaj lot')
