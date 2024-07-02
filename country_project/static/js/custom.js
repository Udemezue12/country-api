// custom.js

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('generate-api-key-form').addEventListener('submit', function(event) {
        event.preventDefault();

        fetch('/secure/generate_api_key', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            const displayElement = document.getElementById('api-key-display');
            if (data.api_key) {
                displayElement.textContent = `Your API Key: ${data.api_key}`;
            } else {
                displayElement.textContent = `Error: ${data.error}`;
            }
        })
        .catch(error => console.error('Error:', error));
    });
});
