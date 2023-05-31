from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/five')
def five():
    directions = ["Left","South","East","Southeast","Up"]
    return render_template('five.html',directions=directions)
