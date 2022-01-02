from flask import Flask,render_template, redirect, url_for, request
import dbcon
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        #db validation here
        user = request.form['user_name']
        passd = request.form['password']
        mycursor = dbcon.connection.cursor()
        mycursor.execute("SELECT mobile_number,password FROM business_user1 where mobile_number = %s and password = %s", (user,passd))
        account = mycursor.fetchone()
        #account = True
  
        if account:
            return render_template('document.html')
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('index.html', error=error)

@app.route('/home', methods=['GET', 'POST'])
def homelink():
    error = None
    return render_template('home.html')

app.run(host='0.0.0.0', port=8080)