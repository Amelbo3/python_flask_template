from app import app
from flask import url_for, render_template
from forms import LoginForm


@app.route('/api')
def api():
    return {"nom":"Amadou"}

@app.route('/')
def index():
    return render_template('index.html')

    
    return render_template('login.html', title=title)

@app.route('/register')
def register():
    return render_template('register.html', title='Register')

@app.route('/profile')
def profile():
    return render_template('profile.html', title='Profile')

@app.route('/user/<username>')
def user(username):
    return f'{username}\'s profile'

@app.route("/login", methods=['GET'])
def login():
    form = LoginForm()
    
    return render_template('login.html', title='Login', form=form)