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
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                
                listen.adjust_for_ambient_noise(source, duration=0.2)
                audio = listen.listen(source)
                text = listen.recognize_google(audio)
                text = text.lower()  
                print("You said:", text)
                
                if "exit" in text:
                    print("Exiting program...")
                    break
    
        except sr.UnknownValueError:
            print("Could not understand audio")

if __name__ == '__main__':
    app.run(debug=True, port=5000)