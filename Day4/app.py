from flask import Flask, render_template, request, redirect, url_for, session
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'ADFADSFA'

# Connect(db--app), Edit, create if not exist
db.init_app(app)
app.app_context().push()
db.create_all() # create/update the database

#---------------------------------------------
@app.route('/')
def home():
    id = session.get('id')
    if id:
        user = User.query.filter_by(id=id).first()
    else:
        user = None
    return render_template('home.html', user=user)

@app.route('/access')
def access():
    curr_user = None
    return render_template('access.html', user=curr_user)

#--------------------------------------------


# Login register logout
# -----> Take the data -----> do the task -------> redirect to pages
@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email') # String or None
    password = request.form.get('password') # String or None

    # Data Vaidation
    # Check email/passwrod in Table(Class) User
    # User.query.filter_by(email=email, password=password) # [], [<user1> , ...]
    user = User.query.filter_by(email=email, password=password).first() # <user1>

    # LogIn
    if user:
        session['id'] = user.id

    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('id')
    return redirect(url_for('access'))

#--------------------------------------------





@app.route('/register')
def register():
    return redirect(url_for('access'))


if __name__ == '__main__':
    app.run(debug=True)
