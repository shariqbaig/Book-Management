from flask_sqlalchemy import SQLAlchemy
from settings import app
import json

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def json(self):
        return {'username': self.username, 'password': self.password}

    def __repr__(self):
        book_object = {
            'username': self.username,
            'password': self.password
        }
        return json.dumps(book_object)

    def username_password_match(_username, _password):
        user = User.query.filter_by(username=_username).filter_by(
            password=_password).first()
        if user is None:
            return False
        else:
            return True

    def getAllUsers():
        return [User.json(user) for user in User.query.all()]

    def createUser(_username, _password):
        new_user = User(username=_username, password=_password)
        db.session.add(new_user)
        db.session.commit()
