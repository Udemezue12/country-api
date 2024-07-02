document.addEventListener('DOMContentLoaded', function() {
    function fetchCountries() {
        fetch('https://country-api-1.onrender.com//state/countries')
            .then(response => response.json())
            .then(data => {
                const countrySelect = document.getElementById('country');
                countrySelect.innerHTML = '';  // Clear existing options
                data.forEach(country => {
                    const option = document.createElement('option');
                    option.value = country[0];  // country code
                    option.textContent = country[1];  // country name
                    countrySelect.appendChild(option);
                });
            })
            .catch(error => console.error('Error fetching countries:', error));
    }

    fetchCountries();
});
