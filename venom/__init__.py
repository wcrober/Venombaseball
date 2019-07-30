from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = 'd5591cc74c68d8d2cff7f13a3f308357'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ymkafnkv:Sp0wyYklup8_qNYn-uAotIN4CUiwSk_L@otto.db.elephantsql.com:5432/ymkafnkv'
db = SQLAlchemy(app)

from venom import routes