from flask import Flask, request, jsonify
import speech_recognition as sr
import translate

listen = sr.Recognizer()

app = Flask(__name__)

@app.route('/')
def index():
    pass

@app.route('/get-text', methods=['POST', 'GET'])
def writtenTranslation():
    data = request.get_json()
    text = data.get('text')

@app.route('/get-speech', methods=['POST', 'GET'])
def spokenTranslation():
    data = request.get_json()

if __name__ == '__main__':
    app.run(debug=True, port=5000)