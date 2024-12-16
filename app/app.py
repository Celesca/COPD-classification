from flask import Flask
from WheezeCrackleModel import WheezeCrackleModel
from LungyNetModel import LungyNetModel

app = Flask(__name__)

WheezeCrackleModel = WheezeCrackleModel()
LungyNetModel = LungyNetModel()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"