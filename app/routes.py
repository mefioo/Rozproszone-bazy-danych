from flask import render_template, redirect, url_for, flash
from app import app, database_connection
from app.forms import SearchFlight, AddFlight, AddAirplane, EditPrice, DeleteFlightPassenger

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
        airline = db.selectAirlineByFlight(form.flightId.data)
        if db.insertFlightPassenger(passId, form.flightId.data, airline) == True:
            flash('Rezerwacja została dodana!', 'success')
        else:
            flash('Coś poszło nie tak!', 'danger')
        return redirect(url_for('main'))
    return render_template('search.html', title='Szukaj', data=data, form=form)


# db menegment
@app.route('/add_flight', methods=['GET', 'POST'])
def add_flight():
    form = AddFlight()
    form.depAir.choices = db.selectAirports()
    form.arrAir.choices = db.selectAirports()
    airplanes = db.selectAirplanes()
    airplanes_ids = []
    for airplane in airplanes:
        airplanes_ids.append(airplane[0])
    form.airplanes.choices = airplanes_ids
    if form.validate_on_submit():
        if form.depAir.data == form.arrAir.data:
            flash('Wybierz dwa różne lotniska!', 'danger')
        else:
            flight_id = form.id.data
            depAir = form.depAir.data[-4:-1]
            arrAir = form.arrAir.data[-4:-1]
            depDate = form.depDate.data
            arrDate = form.arrDate.data
            airplane_id = form.airplanes.data
            empty_places = db.selectCapacityByAirplaneId(form.airplanes.data)
            price = form.price.data
            airline = db.selectAirlineByAirplaneId(airplane_id)
            db.insertFlight(flight_id, depAir, arrAir, depDate, arrDate, airplane_id, price, empty_places, airline)
            flash('Lot został dodany!', 'success')
            return redirect(url_for('main'))
    return render_template('addFlight.html', title='Dodaj lot', form=form)


@app.route('/add_airplane', methods=['GET', 'POST'])
def add_airplane():
    form = AddAirplane()
    if form.validate_on_submit():
        id = form.id.data
        capacity = form.capacity.data
        if form.airline.data == 'RyanAir':
            airline = 1
        else:
            airline = 2
        db.insertAirplane(id, capacity, airline)
        flash('Samolot został dodany!', 'success')
        return redirect(url_for('main'))
    return render_template('addAirplane.html', title='Dodaj samolot', form=form)


@app.route('/edit_price', methods=['GET', 'POST'])
def edit_price():
    form = EditPrice()
    flights = db.selectFligths()
    flight_ids = []
    for flight in flights:
        flight_ids.append(flight[0])
    form.flightId.choices = flight_ids
    if form.validate_on_submit():
        flightId = form.flightId.data
        price = form.price.data
        airline = db.selectAirlineByFlight(flightId)
        db.updateFlightPrice(flightId, price, airline)
        print(str(flightId) + ' ' + str(price) + ' ' + str(airline))
        flash('Cena została zaktualizowana!', 'success')
        return redirect(url_for('main'))
    return render_template('editPrice.html', title='Edytuj cenę lotu', form=form)


@app.route('/delete_flight_passenger', methods=['GET', 'POST'])
def delete_flight_passenger():
    form = DeleteFlightPassenger()
    bookings = db.selectBooking()
    bookings_to_html = []
    for booking in bookings:
        airline = db.selectAirlineByFlight(booking[1])
        bookings_to_html.append('Id pasażera: ' + str(booking[0]) + ', id lotu: ' + str(booking[1]) + ', linia lotnicza: '
                                + str(airline))
    form.passengerId.choices = bookings_to_html
    if form.validate_on_submit():
        data = form.passengerId.data.split(',')
        passId = int(data[0].split(': ')[1])
        flightId = data[1].split(': ')[1]
        airline = int(data[2].split(': ')[1])
        db.deleteBooking(passId, flightId, airline)
        flash('Rezerwacja została usunięta!', 'success')
        return redirect(url_for('main'))
    return render_template('deleteFlightPassenger.html', title='Usuń rezerwację', form=form)
