from flask import Flask
from WheezeCrackleModel import WheezeCrackleModel

app = Flask(__name__)

WheezeCrackleModel = WheezeCrackleModel()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"