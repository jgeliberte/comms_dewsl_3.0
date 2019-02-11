from flask import Flask, jsonify, request, json
from flask_mysqldb  import MySQL
from datetime import datetime
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'senslope'
app.config['MYSQL_DB'] = 'nodejs_login'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['JWT_SECRET_KEY'] = 'secret'

mysql = MySQL(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
CORS(app)

@app.route('/users/register', methods=['POST'])
def register():
    cur = mysql.connection.cursor()
    first_name = request.get_json()['first_name']
    last_name = request.get_json()['last_name']
    email = request.get_json()['email']
    password = bcrypt.generate_password_hash(request.get_json()['password']).decode('utf-8')
    created = datetime.utcnow()

    cur.execute("INSERT INTO users VALUES (0,'" +
    str(first_name) + "','" +
    str(last_name) + "','" +
    str(email) + "','" +
    str(password) + "','" +
    str(created) + "')")

    mysql.connection.commit()

    result = {
        "first_name": first_name,
        "last_name": last_name, 
        "email": email,
        "password": password,
        "created": created
    }

    return jsonify({"result": result})

@app.route('/users/login', methods=['POST'])
def login():
    cur = mysql.connection.cursor()
    email = request.get_json()['email']
    password = request.get_json()['password']
    result = ""

    cur.execute("SELECT * FROM users WHERE email = '" + str(email) + "'")
    return_value = cur.fetchone()
    
    if bcrypt.check_password_hash(return_value['password'], password):
        access_token = create_access_token(identity = {'first_name': return_value['first_name'],'last_name': return_value['last_name'],'email': return_value['email']})
        result = jsonify({"token": access_token})
    else:
        result = jsonify({"error": "Invalid username or password"})

    return result

if __name__ == '__main__':
    app.run(debug=True)