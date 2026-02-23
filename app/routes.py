from flask import Blueprint, render_template, request
from .scanner import run_scan

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        target = request.form['target']
        result = run_scan(target)
    return render_template('index.html', result=result)
