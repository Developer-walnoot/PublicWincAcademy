from flask import Flask, render_template, redirect, url_for

__winc_id__ = '9263bbfddbeb4a0397de231a1e33240a'
__human_name__ = 'templates'

app = Flask(__name__)

@app.route('/')
def index(title="Index"):
    return render_template('index.html', name=title)

@app.route('/home')
def home():
    return redirect('/')

@app.route('/about')
def about(title="About"):
    return render_template('about.html', name=title)

@app.route('/account')
def account(title="Account"):
    return render_template('account.html', name=title)
