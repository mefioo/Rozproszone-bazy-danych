import cx_Oracle

config = {
    'username': 'loty',
    'password': 'loty',
    'dsn': 'localhost/orcl',
    'port': 1521,
    'encoding': 'UTF-8'
}

try:
    con = cx_Oracle.connect(
        config['username'],
        config['password'],
        config['dsn']
    )
    cursor = con.cursor()

except cx_Oracle.Error as error:
    print(error)


def selectAirports():
    sql_query = "select * from mv_airport"
    cursor.execute(sql_query)
    result = cursor.fetchall()
    fin_result = []
    try:
        for element in result:
            fin_result.append(element[1] + ' (' + element[0] + ')')
        return fin_result
    except Exception as e:
        pass


def selectAirplanes():
    sql_query = "select * from vairplane"
    cursor.execute(sql_query)
    result = cursor.fetchall()
    try:
        return result
    except Exception as e:
        pass


def selectFligths():
    sql_query = "select flight_id, airline from vflight"
    cursor.execute(sql_query)
    result = cursor.fetchall()
    try:
        return result
    except Exception as e:
        pass


def selectAirlineByFlightId(id):
    sql_query = "select airline from vflight where flight_id='{}'".format(id)
    cursor.execute(sql_query)
    result = cursor.fetchall()
    result = result[0]
    try:
        return result[0]
    except Exception as e:
        pass


def selectAirlineByAirplaneId(id):
    sql_query = "select * from airplane where airplane_id='{}'".format(id)
    cursor.execute(sql_query)
    result1 = cursor.fetchall()
    sql_query = "select * from airplane@RYAN2WIZZ where airplane_id='{}'".format(id)
    cursor.execute(sql_query)
    result2 = cursor.fetchall()
    if len(result1) > len(result2):
        return 1
    else:
        return 2


def selectBooking():
    sql_query = "select * from vflight_passenger"
    cursor.execute(sql_query)
    result = cursor.fetchall()
    try:
        return result
    except Exception as e:
        pass


def selectFlightsForTable():
    sql_query = "select * from vflight"
    cursor.execute(sql_query)
    result = cursor.fetchall()
    try:
        return result
    except Exception as e:
        pass


def selectPassengerIdByDocument(docId):
    sql_query = "select passenger_id from vpassenger where document_number='{}'".format(docId)
    cursor.execute(sql_query)
    result = cursor.fetchall()
    result = result[0]
    try:
        return result[0]
    except Exception as e:
        pass


def selectAirlineByFlight(flight_id):
    sql_query = "select airline from vflight where flight_id='{}'".format(flight_id)
    cursor.execute(sql_query)
    result = cursor.fetchall()
    result = result[0]
    try:
        return result[0]
    except Exception as e:
        pass


def selectCapacityByAirplaneId(id):
    sql_query = "select capacity from vairplane where airplane_id = '{}'".format(id)
    cursor.execute(sql_query)
    result = cursor.fetchall()
    result = result[0]
    try:
        return result[0]
    except Exception as e:
        pass


def insertFlightPassenger(passId, flightId, airline):
    if airline == 1:
        sql_query = "insert into flight_passenger (passenger_id, flight_id) values ('{}', '{}')".format(passId, flightId)
    elif airline == 2:
        sql_query = "insert into flight_passenger@RYAN2WIZZ (passenger_id, flight_id) values ('{}', '{}')".format(passId,
                                                                                                        flightId)
    else:
        return False
    try:
        cursor.execute(sql_query)
        con.commit()
        return True
    except Exception as e:
        return False


def insertAirplane(id, capacity, airline):
    if airline == 1:
        sql_query = "insert into airplane (airplane_id, capacity) VALUES ('{}', {})".format(id, capacity)
    elif airline == 2:
        sql_query = "insert into airplane@RYAN2WIZZ(airplane_id, capacity) VALUES ('{}', {})".format(id, capacity)
    else:
        return False
    try:
        cursor.execute(sql_query)
        con.commit()
        return True
    except Exception as e:
        return False


def insertFlight(id, depAir, arrAir, depDate, arrDate, airplaneId, price, emptyPlaces, airline):
    if airline == 1:
        sql_query = "insert into flight (flight_id, departure_airport_id, arrival_airport_id, departure_date, " \
                    "arrival_date, airplane_id, price, empty_places, airline) " \
                    "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', {}, {}, {})"\
            .format(id, depAir, arrAir, depDate, arrDate, airplaneId, price, emptyPlaces, airline)
    elif airline == 2:
        sql_query = "insert into flight@RYAN2WIZZ (flight_id, departure_airport_id, arrival_airport_id, departure_date, " \
                    "arrival_date, airplane_id, price, empty_places, airline) " \
                    "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', {}, {}, {})"\
            .format(id, depAir, arrAir, depDate, arrDate, airplaneId, price, emptyPlaces, airline)
    else:
        return False
    try:
        cursor.execute(sql_query)
        con.commit()
        return True
    except Exception as e:
        return False


def updateFlightPrice(flightId, price, airline):
    if airline == 1:
        sql_query = "UPDATE flight SET price = {} WHERE flight_id = '{}'".format(price, flightId)
        print(sql_query)
    elif airline == 2:
        sql_query = "UPDATE flight@RYAN2WIZZ SET price = {} WHERE flight_id = '{}'".format(price, flightId)
    else:
        return False
    try:
        cursor.execute(sql_query)
        con.commit()
        return True
    except Exception as e:
        return False


def deleteBooking(passId, flightId, airline):
    if airline == 1:
        sql_query = "DELETE FROM flight_passenger WHERE passenger_id = '{}' and flight_id = '{}'".format(passId, flightId)
    elif airline == 2:
        sql_query = "DELETE FROM flight_passenger@RYAN2WIZZ WHERE passenger_id = '{}' and flight_id = '{}'".format(passId,
                                                                                                        flightId)
    else:
        return False
    try:
        cursor.execute(sql_query)
        con.commit()
        return True
    except Exception as e:
        return False

