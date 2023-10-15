from flask import Flask, jsonify, request, render_template
import mysql.connector

app = Flask(__name__)

# Database configuration for student records
db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': '3306',
    'database': 'student_records',
    'auth_plugin': 'mysql_native_password'
}


# Function to create a database connection
def create_db_connection():
    return mysql.connector.connect(**db_config)


@app.route('/')
def index():
    """
    This route provides a welcome message when accessing the root URL.
    """
    return jsonify({'message': 'Welcome to the StudentPortal API'})


@app.route('/add_student', methods=['POST'])
def add_student():
    """
    This route handles the submission of the student data input form via a POST request.
    It retrieves the form data, validates it, and inserts the student data into the database.
    """
    # Get form data
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    major = request.form['major']
    average_grade = request.form['average_grade']

    # Create a database connection and cursor
    connection = create_db_connection()
    cursor = connection.cursor()

    try:
        # Insert student data into the database
        query = "INSERT INTO students (FirstName, LastName, Major, AverageGrade) VALUES (%s, %s, %s, %s)"
        values = (first_name, last_name, major, average_grade)
        cursor.execute(query, values)
        connection.commit()
        return jsonify({'message': 'Student data added successfully'})
    except mysql.connector.Error as err:
        return jsonify({'error': f'Error adding student data: {err}'}), 500
    finally:
        # Close the cursor and the database connection
        cursor.close()
        connection.close()


@app.route('/add_student_form', methods=['GET'])
def add_student_form():
    """
    This route renders the HTML form for adding a student's information.
    It responds to a GET request, displaying the student data input form.
    """
    return render_template('add_student.html')


@app.route('/student_data', methods=['GET'])
def get_student_data():
    """
    This route retrieves student data from the database and returns it as JSON.
    It responds to GET requests and provides a list of student names, majors, and average grades.
    """
    # Create a database connection and cursor
    connection = create_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        # SQL query to retrieve student data
        cursor.execute('SELECT FirstName, LastName, Major, AverageGrade FROM students')
        results = cursor.fetchall()
        return jsonify({'student_data': results})
    except mysql.connector.Error as err:
        return jsonify({'error': f'Error fetching student data: {err}'}), 500
    finally:
        # Close the cursor and the database connection
        cursor.close()
        connection.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
