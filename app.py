import requests as requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('home.html', name='Home',)

@app.route('/game')
def generate_game():



if __name__ == '__main__':
    app.run()
