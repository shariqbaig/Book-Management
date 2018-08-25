from flask import Flask

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:\\PythonLearning\\FlashLearning\\database\\database.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kaslvkfqfygxmf:fffcc3cff3e070261c8ace2e9341832649b2ad6c0bcaa454dfb94bf6ebcb13f4@ec2-50-17-194-129.compute-1.amazonaws.com/d1brshler38pdm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'learn'
