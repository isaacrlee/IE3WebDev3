from flask import request, render_template, Flask
import requests
import time
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/')
def index():
    hours = get_hours()
    return render_template('index.html', hours=hours)
    # return render_template('index.html')


@app.route('/', methods=['POST'])
def index_post():
    netid = request.form['netid']
    password = request.form['password']
    balance = get_balance(netid, password)
    return render_template('index.html', balance=balance)


def get_balance(netid, password):
    text = get_html_auth(
        'https://go.dosa.northwestern.edu/uhfs/foodservice/balancecheck', netid, password)
    soup = BeautifulSoup(text, 'html.parser')
    tag = soup.find('table', style='width: 400px;')
    return tag


def get_hours():
    text = get_html(
        'https://northwestern.sodexomyway.com/dining-choices/opennow.html')
    soup = BeautifulSoup(text, 'html.parser')
    tag = soup.find('div', id='opennow_locations', class_='desktopLocations')
    return tag


def get_html(site_url):
    r = requests.get(site_url)
    return r.text.encode(r.encoding)


def get_html_auth(site_url, username, password):
    r = requests.get(site_url, auth=(username, password))
    return r.text.encode(r.encoding)
