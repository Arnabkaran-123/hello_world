from flask import Flask,render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask!'

#app.run(host='0.0.0.0', port=8080)
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return render_template('home.html')
    return render_template('login.html', error=error)

@app.route('/home', methods=['GET', 'POST'])
def homelink():
    error = None
    return render_template('home.html')
