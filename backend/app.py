from flask import Flask, jsonify
import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# MySQL Configuration from .env
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DATABASE'] = os.getenv('MYSQL_DATABASE')

# Establish a connection to MySQL
db_connection = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DATABASE']
)

@app.route('/api/portfolio', methods=['GET'])
def get_projects():
    cursor = db_connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM projects")
    projects = cursor.fetchall()
    cursor.close()
    return jsonify(projects)

if __name__ == '__main__':
    app.run(debug=True)
