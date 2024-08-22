# app/app.py
from flask import Flask, render_template, request, redirect
import mysql.connector
import os

app = Flask(__name__)

# MySQL connection
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        family_member_name = request.form.get("name")
        relation = request.form.get("relation")
        
        # Insert into MySQL database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO family (name, relation) VALUES (%s, %s)", (family_member_name, relation))
        conn.commit()
        cursor.close()
        conn.close()
        
        return redirect("/")
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

