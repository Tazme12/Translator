# Translator

A web-based language translator that supports both text and speech input, built with Flask and vanilla JavaScript.

## Features

- Translate text into multiple languages
- Speech recognition input via microphone
- Simple, clean web interface

## Supported Languages

| Language   | Code |
|------------|------|
| English    | en   |
| French     | fr   |
| Spanish    | es   |
| Portuguese | pt   |
| German     | de   |

## Project Structure

```
Translator/
├── src/
│   ├── app.py        # Flask backend
│   └── script.js     # Frontend logic
├── static/
│   └── css/
│       └── style.css
├── assets/
│   └── microphone.png
├── index.html
└── requirements.txt
```

## Requirements

- Python 3.13+
- PyAudio (for microphone input)

## Installation

1. Clone the repository and navigate to the project folder.

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask server:
   ```bash
   python src/app.py
   ```

2. Open `index.html` in your browser.

3. Select a target language from the dropdown.

4. Either type text and click **Translate**, or click the microphone button to speak a phrase.

## Dependencies

| Package           | Purpose                        |
|-------------------|--------------------------------|
| Flask             | Web server / API               |
| flask-cors        | Cross-origin request handling  |
| translate         | Text translation via MyMemory  |
| SpeechRecognition | Microphone speech-to-text      |
| PyAudio           | Audio input for microphone     |

## Author

Cameron Thornton