from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

#app = Flask(__name__)
#Load configuration variables from ../instance/config.py
#app.config.from_pyfile('config.py')
db = SQLAlchemy()
login = LoginManager()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')

    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)

    login.init_app(app)

    from .views import blog
    app.register_blueprint(blog)

    return app
