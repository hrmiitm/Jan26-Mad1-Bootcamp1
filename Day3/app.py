from flask import Flask, render_template, request, redirect, url_for
from models import db

app = Flask(__name__)


# database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

# Connect(db--app), Edit, create if not exist
db.init_app(app)
app.app_context().push()
db.create_all() # create/update the database









def get_current_user():
    user = None
    # user = {'username': 'hritik', 'email': 'hrithik999999@gmail.com'}
    return user

#------------------------------------------------
@app.route('/')
def home():
    user = get_current_user()
    return render_template('home.html', user=user)


@app.route('/access')
def access():
    return render_template('access.html')


# ------------------------------------------------
@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    return f'{email} - {password}'

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    email = request.form.get('email')
    password1 = request.form.get('password')
    password2 = request.form.get('password2')
    return f'{username} - {email} - {password1} - {password2}'

#-------------------------------------------------

if __name__  == '__main__':
    app.run(debug=True, host='0.0.0.0')