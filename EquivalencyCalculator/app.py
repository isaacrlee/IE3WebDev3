from flask import render_template, Flask
from menu import menu

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', menu=menu)