from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import sqlalchemy
from sqlalchemy import inspect, Inspector

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a1f5105eaf0db9b3fb69853150250679'

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'


from comunidadeimpressionadora import models


engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
inspection = sqlalchemy.inspect(engine)
if not sqlalchemy.engine.reflection.Inspector.has_table(inspection, "usuario"):
    with app.app_context():
        database.drop_all()
        database.create_all()
        print("Base de dados Criados com Sucesso!!")
else:
    print("Base de dados ja existentes")

from comunidadeimpressionadora import routes
