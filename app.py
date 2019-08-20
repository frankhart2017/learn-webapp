from flask import Flask, render_template, request, redirect, jsonify, Response
from connect import cursor, db
from helper import check_email

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = 'my-secret-key'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/', methods=['GET'])
def index():

    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        return render_template('login.html')

    elif request.method == "POST":

        email = request.form['email']
        password = request.form['password']

        if(not check_email(email)):
            return jsonify({"status": "Invalid email address!", "code": -1})

        cursor.execute("SELECT password FROM user WHERE email = '%s'" % (email))
        data = cursor.fetchone()
        count = cursor.rowcount

        if(count == -1):
            return jsonify({"status": "Account does not exist!", "code": -1})
        elif(password != data[0]):
            return jsonify({"status": "Incorrect credentials!", "code": -1})

        return jsonify({"status": "Logged in successfully!", "code": 1})

@app.route("/signup", methods=['GET', 'POST'])
def signup():

    if request.method ==  "GET":
        return render_template("signup.html")

    elif request.method == "POST":

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']

        errorString = ""
        errors = 0

        if(not check_email(email)):
            errors += 1
            errorString += "Invalid email address!\n"

        if(len(phone) != 10):
            errors += 1
            errorString += "Invlaid phone number\n"

        if(not errors):

            cursor.execute("SELECT id FROM user WHERE email='%s' OR phone='%s'" % (email, phone))
            cursor.fetchone()

            if(cursor.rowcount >= 1):
                return jsonify({"status": "Account with this email or phone exists!", "code": -1})

            cursor.execute("INSERT INTO user(name, email, phone, password) VALUES('%s', '%s', '%s', '%s')" %
                            (name, email, phone, password))
            db.commit()
            return jsonify({"status": "Signed up successfully!", "code": 1})

        return jsonify({"status": errorString, "code": -1})
