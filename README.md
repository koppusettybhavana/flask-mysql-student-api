
# flask-mysql-student-api
Simple Flask + MySQL CRUD API for internship assessment
# Flask MySQL CRUD API

This is a simple Flask REST API built using Python and MySQL for internship assessment.

## Features
- Add student (POST)
- View students (GET)
- Delete student (DELETE)

## Technologies Used
- Python
- Flask
- MySQL
- mysql-connector-python

## How to Run
1. Install dependencies:
   pip install flask mysql-connector-python

2. Create MySQL database and table:
   - Database: internship_db
   - Table: students

3. Run the app:
   python app.py

4. Test APIs:
   - GET /students
   - POST /add-student
   - DELETE /delete-student/<id>

## Note
This project was tested locally using Flask development server.
