from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
@app.roue('/home')
def homepage():
    return render_template('home.html')

@app.route('/about')
def about_page():
    return '<h1>This is about page</h1>'