
// JavaScript functions to toggle visibility

// Column form visibility
function toggleColumnVisibility() {
    // Get the column_number input field
    const columnNumberInput = document.querySelector('[name="column_number"]');

    // Get the divs that should be shown/hidden
    const content1Div = document.getElementById('column_1');
    const content2Div = document.getElementById('column_2');
    const content3Div = document.getElementById('column_3');

    // If column_number has a value, show the divs, otherwise hide them
    if (columnNumberInput.value === '1') {
        content1Div.classList.remove('d-none');
    } else if (columnNumberInput.value === '2') {
        content1Div.classList.remove('d-none');
        content2Div.classList.remove('d-none');
    } else if (columnNumberInput.value === '3') {
        content1Div.classList.remove('d-none');
        content2Div.classList.remove('d-none');
        content3Div.classList.remove('d-none');
    } else {
        content1Div.classList.add('d-none');
        content2Div.classList.add('d-none');
        content3Div.classList.add('d-none');
    }
}
 
// Background type form visibility
function toggleBackgroundTypeVisibility(element){

    // Get the background input fields
    const backgroundColorDiv = document.getElementById('backgroundDiv_color');
    const backgroundImageDiv = document.getElementById('backgroundDiv_image');

    // Switch between background color and background image
    if (element.id === 'color') {
        backgroundColorDiv.classList.remove('d-none');
        backgroundImageDiv.classList.add('d-none');
    } else {
        backgroundImageDiv.classList.remove('d-none');
        backgroundColorDiv.classList.add('d-none');
    }
}

// Slider form type visibility
function toggleColumnSliderVisibility(element) {

    // Content and Slider sections input fields
    const contentSection = document.getElementById('content_form');
    const sliderSection = document.getElementById('slider_form');

    contentSection.classList.add('d-none');
    sliderSection.classList.add('d-none');

    // Switch visibility between Content and Slider section
    if (element.value === 'content') {
    contentSection.classList.remove('d-none');
    } else if (element.value === 'slider') {
    sliderSection.classList.remove('d-none');
    }
}

// 3D effect
document.addEventListener('mousemove', e =>{

    // Get and save mouse coordinates
    Object.assign(document.documentElement,{
    style:`
    --move-x: ${(e.clientX - window.innerWidth / 2) * 0.015}deg;
    --move-y: ${(e.clientY - window.innerWidth / 2) * -0.015}deg;
    `
    })
})

let column_number = document.querySelector('[name="column_number"]');
column_number.setAttribute('min', 1);
column_number.setAttribute('max', 3);
column_number.addEventListener('input', toggleColumnVisibility);