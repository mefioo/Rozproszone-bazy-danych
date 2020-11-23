from flask import render_template
from app import app, database_connection, airports

dbConnection = database_connection

@app.route('/')
@app.route('/main')
def main():
    data = airports.readAndModifyData()
    #dbConnection.test(data)

    return render_template('main.html', title='Strona główna')
