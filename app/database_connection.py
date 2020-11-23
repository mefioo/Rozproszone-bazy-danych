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


def test(data):
    for airport in data:
        sql_query = "INSERT INTO AIRPORT@RYAN2WIZZ (AIRPORT_ID, CITY) VALUES ('{}', '{}')".format(airport["code"], airport["city"])
        try:
            cursor.execute(sql_query)
            con.commit()
        except Exception as e:
            pass


