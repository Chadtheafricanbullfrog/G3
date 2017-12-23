from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE users
             (id text, name text)''')

# Insert a row of data
c.execute("INSERT INTO users VALUES ('1','Chad')")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

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
