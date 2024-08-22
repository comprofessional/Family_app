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
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        family_member_name = request.form.get("name")
        relation = request.form.get("relation")

        # Insert into MySQL database
        cursor.execute("INSERT INTO family (name, relation) VALUES (%s, %s)", (family_member_name, relation))
        conn.commit()

        return redirect("/")

    # Retrieve family members from the database
    cursor.execute("SELECT name, relation FROM family")
    family_members = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("index.html", family_members=family_members)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

