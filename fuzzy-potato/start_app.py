from flask import Flask, jsonify, abort, make_response, request, url_for, render_template
from app import *
from storyline import *



app = Flask(__name__)


@app.route('/fuzzy-potato')
@app.route('/fuzzy-potato/')
def game():
    return render_template('game.html')







if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)