from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///fakepinterest.db'
app.config["SECRET_KEY"] = 'c0896d3261cebbd7e245528044f5aec9'  # chave gerada a partir da execução do gera_chave.py
app.config["UPLOAD_FOLDER"] = 'static/fotos_posts'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'homepage'

from fakepinterest import routes
