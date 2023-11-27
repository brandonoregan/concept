'use strict'

// Reviews Slider
// Reviews Slider

const config2 = {
    individualItem: '.album-item2', // class of individual item
    carouselWidth: 1000, // in px
    carouselId: '#album-rotator2', // carousel selector
    carouselHolderId: '#album-rotator2-holder', // carousel should be <div id="carouselId"><div id="carouselHolderId">{items}</div></div>
}


// Async function for generating webGL waves


document.addEventListener("DOMContentLoaded", function(e) {

    // Get items
    const el = document.querySelector(config2.individualItem);
    const elWidth = parseFloat(window.getComputedStyle(el).width) + parseFloat(window.getComputedStyle(el).marginLeft) + parseFloat(window.getComputedStyle(el).marginRight);
    
    // Track carousel
    let mousedown = false;
    let movement = false;
    let initialPosition = 0;
    let selectedItem;
    let currentDelta = 0;

    document.querySelectorAll(config2.carouselId).forEach(function(item) { 
        item.style.width = `${config2.carouselWidth}px`;
    });
    
    document.querySelectorAll(config2.carouselId).forEach(function(item) {
        item.addEventListener('pointerdown', function(e) {
            mousedown = true;
            selectedItem = item;
            initialPosition = e.pageX;
            currentDelta = parseFloat(item.querySelector(config2.carouselHolderId).style.transform.split('translateX(')[1]) || 0;
        }); 
    });
    
    const scrollCarousel = function(change, currentDelta, selectedItem) {
        let numberThatFit = Math.floor(config2.carouselWidth / elWidth);
        let newDelta = currentDelta + change;
        let elLength = selectedItem.querySelectorAll(config2.individualItem).length - numberThatFit;
        if(newDelta <= 0 && newDelta >= -elWidth * elLength) {
            selectedItem.querySelector(config2.carouselHolderId).style.transform = `translateX(${newDelta}px)`;
        } else {
            if(newDelta <= -elWidth * elLength) {
                selectedItem.querySelector(config2.carouselHolderId).style.transform = `translateX(${-elWidth * elLength}px)`;
            } else if(newDelta >= 0) {
                selectedItem.querySelector(config2.carouselHolderId).style.transform = `translateX(0px)`;
            }
        }
    }

    document.body.addEventListener('pointermove', function(e) {
        if(mousedown == true && typeof selectedItem !== "undefined") {
            let change = -(initialPosition - e.pageX);
            scrollCarousel(change, currentDelta, document.body);
            document.querySelectorAll(`${config2.carouselId} a`).forEach(function(item) {
                item.style.pointerEvents = 'none';
            });
            movement = true;
        }
    });
    
    ['pointerup', 'mouseleave'].forEach(function(item) {
        document.body.addEventListener(item, function(e) {
            selectedItem = undefined;
            movement = false;
            document.querySelectorAll(`${config2.carouselId} a`).forEach(function(item) {
                item.style.pointerEvents = 'all';
            });
        });
    });

    document.querySelectorAll(config2.carouselId).forEach(function(item) {
        let trigger = 0;
        item.addEventListener('wheel', function(e) {
            if(trigger !== 1) {
                ++trigger;
            } else {
                let change = e.deltaX * -3;
                let currentDelta = parseFloat(item.querySelector(config2.carouselHolderId).style.transform.split('translateX(')[1]) || 0;
                scrollCarousel(change, currentDelta, item);
                trigger = 0;
            }
            e.preventDefault();
            e.stopImmediatePropagation();
            return false;
        });
    });
});