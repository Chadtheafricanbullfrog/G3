from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)
import sqlite3

# conn = sqlite3.connect('database.db')
# c = conn.cursor()

# Create table
# c.execute('''CREATE TABLE users
             # (id text, name text)''')

# Insert a row of data
# c.execute("INSERT INTO users VALUES ('1','Chad')")

# Save (commit) the changes
# conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
# conn.close()

# test comment

@app.route('/')
def hello_world():

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("INSERT INTO users VALUES ('1','bun')")
    conn.commit()
    conn.close()

    return render_template('Z.html', test_variable="1234567 hello")

@app.route('/B')
def Hello():

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("INSERT INTO users VALUES ('4','door')")
    conn.commit()
    conn.close()

    return render_template('B.html')



@app.route('/Go')
def Go():

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("INSERT INTO users VALUES ('9','twine')")
    conn.commit()
    conn.close()

    return render_template('Go.html')

#1-5-18 work on cleaning up tables in d.db

@app.route('/A')
def A():

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("INSERT INTO users VALUES ('3','tree')")
    conn.commit()
    conn.close()

    return render_template('A.html')


@app.route('/C')
def over_the_valley():

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("INSERT INTO users VALUES ('2','chew')")
    conn.commit()
    conn.close()

    return render_template('C.html')


@app.route('/D')
def D():

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("INSERT INTO users VALUES ('5','clive')")
    conn.commit()
    conn.close()

    return render_template('D.html')


@app.route('/E')
def E():

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("INSERT INTO users VALUES ('6','wicks')")
    conn.commit()
    conn.close()

    return render_template('E.html')


@app.route('/F')
def F():

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("INSERT INTO users VALUES ('7','heaven')")
    conn.commit()
    conn.close()

    return render_template('F.html')


@app.route('/G')
def G():

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("INSERT INTO users VALUES ('8','mate')")
    conn.commit()
    conn.close()

    return render_template('G.html')


@app.route('/Chapter_1')
def Chapter_1():

    return render_template('Chapter_1.html')


@app.route('/Chapter_2')
def Chapter_2():

    return render_template('Chapter_2.html')
