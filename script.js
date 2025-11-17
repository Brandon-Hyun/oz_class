const display = document.getelentById('dispaly')

function clearDisplay() {
    display.innerText = '';
}

function deleteLast() {
    display.innerText = display.innerText.slice(0,-1);
}

function appendToDisplay(value) {
    display.innerText += value;
}

function calculateResult() {
    try {
        display.innerText = eval(display.innerText);
    } catch {
        display.innerText = 'error';
    }
}