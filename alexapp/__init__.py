from flask import Flask
from flask_sqlalchemy import SQLAlchemy


#app = Flask(__name__)
#Load configuration variables from ../instance/config.py
#app.config.from_pyfile('config.py')
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')

    db.app = app
    db.init_app(app)

    from .views import dev_blue
    app.register_blueprint(dev_blue)

    return app


