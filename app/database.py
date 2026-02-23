import sqlite3
from flask import g

def get_db(app):
    if 'db' not in g:
        g.db = sqlite3.connect(app.config['DATABASE'])
    return g.db

def init_db(app):
    with app.app_context():
        db = sqlite3.connect(app.config['DATABASE'])
        db.execute('''CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            target TEXT,
            risk TEXT
        )''')
        db.commit()
