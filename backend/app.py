from flask import Flask, jsonify
import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file only in local development
if os.getenv('ENVIRONMENT', 'local') == 'local':  # Check if we're in local environment
    load_dotenv()  # This will load the variables from the .env file

app = Flask(__name__)

# Determine which environment we're in and set database configuration
environment = os.getenv('ENVIRONMENT', 'local')  # Default to 'local' if not specified

if environment == 'local':
    # Uses the local database configuration with locally set .env file variables (duh)
    app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')  
    app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
    app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
    app.config['MYSQL_DATABASE'] = os.getenv('MYSQL_DATABASE')
elif environment == 'test':
    app.config['MYSQL_HOST'] = os.getenv('TEST_MYSQL_HOST')
    app.config['MYSQL_USER'] = os.getenv('TEST_MYSQL_USER')
    app.config['MYSQL_PASSWORD'] = os.getenv('TEST_MYSQL_PASSWORD')
    app.config['MYSQL_DATABASE'] = os.getenv('TEST_MYSQL_DATABASE')
elif environment == 'production':
    app.config['MYSQL_HOST'] = os.getenv('PROD_MYSQL_HOST')
    app.config['MYSQL_USER'] = os.getenv('PROD_MYSQL_USER')
    app.config['MYSQL_PASSWORD'] = os.getenv('PROD_MYSQL_PASSWORD')
    app.config['MYSQL_DATABASE'] = os.getenv('PROD_MYSQL_DATABASE')

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
