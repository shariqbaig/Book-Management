from flask import Flask

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:\\GIT Projects\\Book-Management\\database\\database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'learn'
