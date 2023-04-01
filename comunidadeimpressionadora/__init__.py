from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import sqlalchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a1f5105eaf0db9b3fb69853150250679'

if os.getenv("DATABASE_URL"):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

from comunidadeimpressionadora import models
engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
if not engine.has_table("usuario"):
    with app.app_context():
        database.drop_all()
        database.create_all()
        print("A base de dados foi criada com sucesso")
else:
    print("A base de dados já existe")

from comunidadeimpressionadora import routes
