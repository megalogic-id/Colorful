const hexColorInput = document.getElementById("hex-color");
const colorPicker = document.getElementById("color-picker");
const colorPreview = document.getElementById("color-preview");

// Function to update the color picker and preview based on hex input
function updateFromHexInput() {
  const hexColor = hexColorInput.value;

  // Update the color picker value
  colorPicker.value = hexColor;

  // Update the background color of the preview box
  colorPreview.style.backgroundColor = hexColor;
}

// Function to update the color preview box and input text value
function updateColorPreview() {
  const hexColor = colorPicker.value;

  // Update the background color of the preview box
  colorPreview.style.backgroundColor = hexColor;

  // Update the input text value
  hexColorInput.value = hexColor;
}

// Add an event listener to the color picker input
colorPicker.addEventListener("input", updateColorPreview);

// Add an event listener to the hex color input
hexColorInput.addEventListener("input", updateFromHexInput);

// Trigger the initial update
updateColorPreview();

const colorCodeElements = document.querySelectorAll(".copy-color-code");

colorCodeElements.forEach((element) => {
  element.addEventListener("click", () => {
    const colorCode = element.getAttribute("data-color");
    copyToClipboard(colorCode);
    Swal.fire("Good job!", `You copied: ${colorCode}`, "success");
  });
});

// Function to copy text to clipboard
function copyToClipboard(text) {
  const textarea = document.createElement("textarea");
  textarea.value = text;
  document.body.appendChild(textarea);
  textarea.select();
  document.execCommand("copy");
  document.body.removeChild(textarea);
}
