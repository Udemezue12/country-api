document.addEventListener('DOMContentLoaded', function() {
    const countrySelect = document.getElementById('country');
    const stateSelect = document.getElementById('state');

    countrySelect.addEventListener('change', function() {
        const selectedCountry = countrySelect.value;
        console.log(`Selected country: ${selectedCountry}`);

        if (selectedCountry) {
            fetch(`https://country-api-1.onrender.com/state/get_states/${selectedCountry}`)
                .then(response => response.json())
                .then(data => {
                    console.log(data);  // Log the response data to see what's returned
                    stateSelect.innerHTML = '<option value=""></option>';  // Clear previous options
                    data.forEach(state => {
                        const option = document.createElement('option');
                        option.value = state;
                        option.textContent = state;
                        stateSelect.appendChild(option);
                    });
                })
                .catch(error => console.error('Error fetching states:', error));
        } else {
            stateSelect.innerHTML = '<option value=""></option>';
        }
    });
});
