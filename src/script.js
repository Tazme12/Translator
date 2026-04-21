function getLanguage() {
    const language = document.getElementById('language-select').value;

    fetch("http://127.0.0.1:5000/choose-language", {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ language: language })
    })
    .then(response => {
        console.log("Response status: ", response.status);
        return response.json();
    })
    .then(data => {
        if(data.success) {
            alert(data.success);
        } else {
            alert(data.error);
        }
    });
}

function getTextInput() {
    const text = document.getElementById('text').value;

    fetch("http://127.0.0.1:5000/get-text", {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: text })
    })
    .then(response => {
        console.log("Response status: ", response.status);
        return response.json();
    })
    .then(data => {
        if(data.success) {
            alert(data.message);
        } else {
            alert(data.error);
        }
    });
}

function getSpeechInput() {
    fetch("http://127.0.0.1:5000/get-speech", {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({})
    })
    .then(response => {
        console.log("Response status: ", response.status);
        return response.json();
    })
    .then(data => {
        if(data.success) {
            alert(data.message);
        } else {
            alert(data.error);
        }
    });
}