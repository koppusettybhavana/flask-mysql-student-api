# -----------------------------------------
# 1. IMPORT REQUIRED MODULES
# -----------------------------------------
from flask import Flask, request, jsonify
import mysql.connector


# -----------------------------------------
# 2. CREATE FLASK APP
# -----------------------------------------
app = Flask(__name__)


# -----------------------------------------
# 3. DATABASE CONNECTION FUNCTION
# -----------------------------------------
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",          # change if needed
        password="password",  # change if needed
        database="internship_db"
    )


# -----------------------------------------
# 4. HOME ROUTE
# -----------------------------------------
@app.route("/")
def home():
    return "Simple Flask API is running"


# -----------------------------------------
# 5. ADD STUDENT (CREATE)
# -----------------------------------------
@app.route("/add-student", methods=["POST"])
def add_student():
    data = request.json
    name = data["name"]
    email = data["email"]

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, email) VALUES (%s, %s)",
        (name, email)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Student added successfully"})


# -----------------------------------------
# 6. VIEW ALL STUDENTS (READ)
# -----------------------------------------
@app.route("/students", methods=["GET"])
def get_students():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(students)


# -----------------------------------------
# 7. DELETE STUDENT (DELETE)
# -----------------------------------------
@app.route("/delete-student/<int:id>", methods=["DELETE"])
def delete_student(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id = %s",
        (id,)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Student deleted successfully"})


# -----------------------------------------
# 8. RUN FLASK APPLICATION
# -----------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
