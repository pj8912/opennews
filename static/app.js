// flash message timeout
setTimeout(function() {
    var flashMessage = document.getElementById('flash-message');
    if (flashMessage) {
        flashMessage.style.display = 'none';
    }
}, 3000);

// flash message remove button
function removeFlash() {
    const element = document.getElementById(`div_flash`);
    element.remove();
  }