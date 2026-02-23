from flask import Flask
from .routes import main
from .database import init_db
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev'
    app.config['DATABASE'] = os.path.join('/tmp', 'scans.db')

    init_db(app)
    app.register_blueprint(main)
    return app
