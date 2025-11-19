// 1. Get references to elements on the page
const billInput = document.getElementById("bill");
const tipInput = document.getElementById("tip");
const calculateBtn = document.getElementById("calculate");
const totalDisplay = document.getElementById("total-display");
const tipAmountDisplay = document.getElementById("tip-amount");
const totalAmountDisplay = document.getElementById("total-amount");

// 2. When user clicks the Calculate button:
calculateBtn.addEventListener("click", function(event) {
    event.preventDefault();     // stop form from refreshing

    // 3. Red the values from the inputs
    const bill = parseFloat(billInput.value);
    const tipPercent = parseFloat(tipInput.value);

    // 4. Validate that both inputs are numbers
    if (isNaN(bill) || isNaN(tipPercent)) {
        totalDisplay.textContent = "Please enter both values.";
        return;
    }

    // 5. Convert percent to decimal (e.g., 15 -> 0.15)
    const tipDecimal = tipPercent / 100;

    // 6. Calculate total
    const tipAmount = bill * tipDecimal;
    const total = bill + tipAmount

    // 7. Update the page with the result (2 decimal places)
    totalDisplay.textContent = `$${total.toFixed(2)}`;
    tipAmountDisplay.textContent = `$${tipAmount.toFixed(2)}`;
    totalAmountDisplay.textContent = `$${total.toFixed(2)}`

});