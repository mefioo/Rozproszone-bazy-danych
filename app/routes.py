from flask import render_template, redirect, url_for, flash
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
    flightList = db.selectFligths()
    flights = []
    for flight in flightList:
        flights.append(flight[0])
    form.flightId.choices = flights
    data = db.selectFlightsForTable()
    if form.validate_on_submit():
        passId = db.selectPassengerIdByDocument(form.documentNumber.data)
        if db.insertFlightPassenger(passId, form.flightId.data) == True:
            flash('Rezerwacja została dodana!', 'success')
        else:
            flash('Coś poszło nie tak!', 'danger')
        return redirect(url_for('main'))
    return render_template('search.html', title='Szukaj', data=data, form=form)



# db menegment

@app.route('/add_flight')
def add_flight():
    return render_template('addFlight.html', title='Dodaj lot')
