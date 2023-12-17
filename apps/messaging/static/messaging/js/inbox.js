'use strict'

// Select the container displaying the conversation
const convoContainer = document.querySelector('.convoContainer');

// Ensure scroll bar is located at the bottom of container upton refresh
convoContainer.scrollTop = convoContainer.scrollHeight;
convoContainer.lastElementChild.scrollIntoView(false);


document.addEventListener('DOMContentLoaded', function() {
    const messageTextarea = document.getElementById('messageTextarea');
    const messageForm = document.getElementById('messageForm');

    messageTextarea.addEventListener('keypress', function(event) {
        // Check if Enter key is pressed (Enter key code is 13)
        if (event.keyCode === 13 && !event.shiftKey) {
            // Prevent default Enter key behavior (newline in textarea)
            event.preventDefault();

            // Trigger form submission when Enter is pressed
            messageForm.submit();
        }
    });
});