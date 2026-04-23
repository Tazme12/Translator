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
            document.getElementById("process").innerHTML = data.confirmation;
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
            let output = document.getElementById('output');
            let html = `<p>${data.phrase}</p>`;
            output.innerHTML = html;
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
            let output = document.getElementById('output');
            let html = `<p>${data.phrase}</p>`;
            output.innerHTML = html;
        } else {
            alert(data.error);
        }
    });
}