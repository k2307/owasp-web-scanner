from flask import Flask
from .routes import main
from .database import init_db

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev'
    app.config['DATABASE'] = 'instance/scans.db'
    init_db(app)
    app.register_blueprint(main)
    return app
