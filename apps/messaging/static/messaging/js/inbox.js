'use strict'

// Select the container displaying the conversation
const convoContainer = document.querySelector('.convoContainer');

// Ensure scroll bar is located at the bottom of container upton refresh
convoContainer.scrollTop = convoContainer.scrollHeight;
convoContainer.lastElementChild.scrollIntoView(false);


// Ensure 'enter' key submits message
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('messageInput').addEventListener('keydown', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault(); // Prevent default behavior (new line)
            document.getElementById('messageForm').submit(); // Submit the form
        }
    });
});