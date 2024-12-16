import os
from flask import Flask, request, jsonify
from WheezeCrackleModel import WheezeCrackleModel
from LungyNetModel import LungyNetModel

app = Flask(__name__)

WheezeCrackleModel = WheezeCrackleModel()
LungyNetModel = LungyNetModel()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/upload", methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file:
        # Save the file to a temporary location
        file_path = os.path.join("/tmp", file.filename)
        file.save(file_path)
        
        # Read the file and pass it to the model
        with open(file_path, 'rb') as f:
            audio_data = f.read()
        
        # Assuming the model has a method called `predict` that takes audio data
        result_wheeze_crackle = WheezeCrackleModel.predict(audio_data, mode='mfcc')
        result_lungynet = LungyNetModel.predict(audio_data)
        
        # Clean up the temporary file
        os.remove(file_path)
        
        return jsonify({
            "message": "File successfully uploaded",
            "result_wheeze_crackle": result_wheeze_crackle,
            "result_lungynet": result_lungynet
        }), 200