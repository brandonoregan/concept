'use strict'

// Select the convoContainer element
const convoContainer = document.querySelector('.convoContainer');

// Scroll to the bottom of the container
convoContainer.scrollTop = convoContainer.scrollHeight;
convoContainer.lastElementChild.scrollIntoView(false); // Scroll to the last element
