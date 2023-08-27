// Get references to the input, button, and output elements
const textInput = document.getElementById("textInput");
const submitButton = document.getElementById("submitButton");
const outputDiv = document.getElementById("output");

// Add a click event listener to the button
submitButton.addEventListener("click", function () {
    // Get the text entered by the user
    const enteredText = textInput.value;

    // Check if the entered text is not empty
    if (enteredText.trim() !== "") {
        // Clear the input field
        textInput.value = "";

        // Create a new paragraph element to display the entered text
        const paragraph = document.createElement("p");
        paragraph.textContent = enteredText;

        // Append the paragraph to the output div
        outputDiv.appendChild(paragraph);
    }
});