const slider = document.getElementById('difficulty-slider');
const output = document.getElementById('difficulty-value');
slider.oninput = function() {
    output.textContent = this.value;
}