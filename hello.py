from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    math = 2 + 3
    return render_template('hello_world.html', math=math)