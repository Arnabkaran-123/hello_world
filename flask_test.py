from flask import Flask,render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        #db validation here
        if request.form['user_name'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return render_template('document.html')
    return render_template('index.html', error=error)

@app.route('/home', methods=['GET', 'POST'])
def homelink():
    error = None
    return render_template('home.html')

app.run(host='0.0.0.0', port=8080)