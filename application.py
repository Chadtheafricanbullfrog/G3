from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

# test comment

@app.route('/')
def hello_world():
    return render_template('Z.html', test_variable="1234567 hello")

@app.route('/B')
def Hello():
    return render_template('B.html')


@app.route('/Go')
def Go():
    return render_template('Go.html')


@app.route('/A')
def A():
    return render_template('A.html')


@app.route('/C')
def over_the_valley():
    return render_template('C.html')


@app.route('/D')
def D():
    return render_template('D.html')


@app.route('/E')
def E():
    return render_template('E.html')


@app.route('/F')
def F():
    return render_template('F.html')


@app.route('/G')
def G():
    return render_template('G.html')
