from flask import render_template
from app import app, database_connection

dbConnection = database_connection

@app.route('/')
@app.route('/main')
def main():
    dbConnection.test()
    data = 'Tekst jakiś tam'
    return render_template('main.html', title='Strona główna', data=data)
