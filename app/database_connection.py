import cx_Oracle

config = {
    'username': 'loty',
    'password': 'loty',
    'dsn': '192.168.0.136/XE',
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


def test():
    return None


