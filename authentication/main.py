import os

from flask import Flask, redirect, render_template, request, session, url_for
from helpers import get_users, hash_password
from create_user import create_user

__winc_id__ = '8fd255f5fe5e40dcb1995184eaa26116'
__human_name__ = 'authentication'

app = Flask(__name__)

app.secret_key = os.urandom(16)

user_list = create_user() # add user denis with hashed password to the list.
correct_password = user_list["Denis"]
print(user_list)

def correct_combo(username, password):
    hashed_password = user_list[username]
    if hashed_password  == hash_password(password):
        return True
    
@app.route('/home')
def redirect_index():
    return redirect(url_for('index'))


@app.route('/')
def index():
    return render_template('index.html', title='Index')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/lon')
def lon():
    return render_template('lon.html', title='League of Nations')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if correct_combo(username, password) is True:
            return redirect(url_for('dashboard', title=username))
        else:
            return render_template('login.html', error=True)       
    return render_template('login.html', title="login")

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', title="dashboard")


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    # YOUR SOLUTION HERE
    pass

