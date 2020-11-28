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


def selectFligths(depAir, arrAir):
    sql_query = "select * from flight where departure_airport_id='{}' and arrival_airport_id='{}'".format(depAir, arrAir)
    cursor.execute(sql_query)
    result = cursor.fetchall()
    try:
        return result
    except Exception as e:
        pass


def addFlight(data):
    sql_query = "INSERT INTO AIRPORT@RYAN2WIZZ (AIRPORT_ID, CITY) VALUES ('{}', '{}')".format(1, 2)
    try:
        cursor.execute(sql_query)
        con.commit()
    except Exception as e:
        pass


