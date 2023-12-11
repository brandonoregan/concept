'use strict'

document.addEventListener('DOMContentLoaded', function() {
    // Initial value of the condition
    var display_login = true; // Set it to true or false based on your initial requirement

    // Function to toggle the condition
    function toggleCondition() {
        display_login = !display_login; // Toggle the value (true becomes false, false becomes true)
        // Refresh the content based on the updated condition
        refreshContent();
    }

    // Function to refresh the content based on the condition
    function refreshContent() {
        var elementsToDisplay = document.querySelectorAll('.element-to-display'); // Change this selector to match the elements you want to display/hide

        elementsToDisplay.forEach(function(element) {
            if (display_login) {
                element.style.display = 'block'; // Show the element
            } else {
                element.style.display = 'none'; // Hide the element
            }
        });
    }

    // Event listener for the button click to toggle the condition
    document.getElementById('toggleButton').addEventListener('click', toggleCondition);

    // Initial content display based on the initial condition
    refreshContent();
});