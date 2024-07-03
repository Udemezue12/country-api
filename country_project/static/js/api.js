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
        if (data.api_key) {
            window.location.href = `/secure/display_api_key?api_key=${data.api_key}`;
        } else {
            alert(`Error: ${data.error}`);
        }
    })
    .catch(error => console.error('Error:', error));
});
