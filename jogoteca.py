from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

csrf=CSRFProtect(app)

bcrypt = Bcrypt(app)

from views_jogos import *
from views_user import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)