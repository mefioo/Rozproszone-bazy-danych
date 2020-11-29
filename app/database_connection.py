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


def selectFligths():
    sql_query = "select flight_id, airline from vflight"
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
    sql_query = "select passenger_id from passenger where document_number='{}'".format(docId)
    cursor.execute(sql_query)
    result = cursor.fetchall()
    result = result[0]
    try:
        return result[0]
    except Exception as e:
        pass


def insertFlightPassenger(passId, flightId):
    sql_query = "insert into flight_passenger (passenger_id, flight_id) values ('{}', '{}')".format(passId, flightId)
    try:
        cursor.execute(sql_query)
        con.commit()
        return True
    except Exception as e:
        return False
