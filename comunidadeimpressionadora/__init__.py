from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import inspect, Inspector


app = Flask(__name__)

app.config['SECRET_KEY'] = 'a1f5105eaf0db9b3fb69853150250679'

if os.getenv("DATABASE_URL"):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Yoiti/PycharmProjects/SiteComunidade/comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'


from comunidadeimpressionadora import models


engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
ins = inspect(engine)
existe = ins.dialect.has_table(engine.connect(), "usuario")
if not existe:
    with app.app_context():
        database.drop_all()
        database.create_all()
    print("Base de dados Criados com Sucesso!!")
else:
    print("Base de dados ja existentes")

from comunidadeimpressionadora import routes
