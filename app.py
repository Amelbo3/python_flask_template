from flask import url_for, render_template
from flask import Flask

app = Flask(__name__)




@app.route('/')
def index():
    return url_for('index')

@app.route('/login')
def login():
    return render_template('login.html', title='Login')

@app.route('/register')
def register():
    return render_template('register.html', title='Register')

@app.route('/profile')
def profile():
    return render_template('profile.html', title='Profile')

@app.route('/user/<username>')
def user(username):
    return f'{username}\'s profile'


#print(url_for('profile', username='John Doe'))