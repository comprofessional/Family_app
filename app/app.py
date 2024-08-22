from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host="db",
        user="your_mysql_user",
        password="your_mysql_password",
        database="your_mysql_database"
    )
    return connection

@app.route('/')
def index():
    return "Welcome to the Family Database!"

@app.route('/family')
def family():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM family")
    family_members = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('family.html', family_members=family_members)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

