from flask_sqlalchemy import SQLAlchemy # Class

db = SQLAlchemy() # Instance/Object

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    # Roles
    isUser = db.Column(db.Boolean, default=True)
    isCreator = db.Column(db.Boolean, default=False)
    isAdmin = db.Column(db.Boolean, default=False)

    # Is User Blacklisted
    isBlacklisted = db.Column(db.Boolean, default=False)
