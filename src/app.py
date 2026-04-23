from flask import Flask, request, jsonify
from flask_cors import CORS
import speech_recognition as sr
from translate import Translator

listen = sr.Recognizer()

app = Flask(__name__)
CORS(app)

translator = Translator(from_lang='en', to_lang='en')

@app.route('/')
def index():
    pass

@app.route('/choose-language', methods=['GET', 'POST'])
def chooseLanguage():
    data = request.get_json()
    language = data.get('language')

    if language == 'none':
        return jsonify({'success': False, 'error': 'Please select a language.'})
    
    translator.__init__(from_lang='en', to_lang=language)
    return jsonify({'success': True, 'confirmation': 'Language selected'})

@app.route('/get-text', methods=['GET', 'POST'])
def writtenTranslation():
    data = request.get_json()
    text = data.get('text')

    if text == '':
        return jsonify({'success': False, 'error': 'Please enter text to translate.'})
    
    else:
        translation = translator.translate(text)
        return jsonify({'success': True, 'phrase': translation})

@app.route('/get-speech', methods=['GET', 'POST'])
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

                else:
                    translation = translator.translate(text)
                    return jsonify({'success': True, 'phrase': translation})
    
        except sr.UnknownValueError:
            print("Could not understand audio")

if __name__ == '__main__':
    app.run(debug=True, port=5000)