document.addEventListener('DOMContentLoaded', function() {
    const apiKey = 'YOUR_API_KEY';  // Replace with the actual API key
    const countrySelect = document.getElementById('country');
    const stateSelect = document.getElementById('state');

    // Function to fetch and populate countries
    function fetchCountries() {
        fetch('/state/countries', {
           
        })
        .then(response => response.json())
        .then(data => {
            countrySelect.innerHTML = '';  // Clear existing options
            data.forEach(country => {
                const option = document.createElement('option');
                option.value = country;  // Assuming country is a string
                option.textContent = country;
                countrySelect.appendChild(option);
            });
        })
        .catch(error => console.error('Error fetching countries:', error));
    }

    // Event listener for country selection
    countrySelect.addEventListener('change', function() {
        const selectedCountry = countrySelect.value;
        console.log(`Selected country: ${selectedCountry}`);

        if (selectedCountry) {
            fetch(`/state/get_states/${selectedCountry}`, {
               
            })
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

    // Initial fetch of countries when the page loads
    fetchCountries();
});
