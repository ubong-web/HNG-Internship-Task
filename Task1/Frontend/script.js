let searchBtn = document.getElementById("search-btn");
let numberInp = document.getElementById("number-inp");
let result = document.getElementById("result");

searchBtn.addEventListener("click", () => {
  let number = numberInp.value;
  let finalURL = `https://24f4plfe8f.execute-api.us-east-1.amazonaws.com/api/classify-number?number=${number}`;
  
  console.log(finalURL);

  fetch(finalURL)
    .then((response) => response.json())
    .then((data) => {
      // Display the fun fact and properties from the Lambda response
      result.innerHTML = `
        <p><strong>Number:</strong> ${data.number}</p>
        <p><strong>Is Prime:</strong> ${data.is_prime}</p>
        <p><strong>Is Perfect:</strong> ${data.is_perfect}</p>
        <p><strong>Properties:</strong> ${data.properties.join(', ')}</p>
        <p><strong>Digit Sum:</strong> ${data.digit_sum}</p>
        <p><strong>Fun Fact:</strong> ${data.fun_fact}</p>
      `;
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
      if (number.length == 0) {
        result.innerHTML = `<h3>The input field cannot be empty</h3>`;
      } else {
        result.innerHTML = `<h3>Please enter a valid number or check your server connection.</h3>`;
      }
    });
});
