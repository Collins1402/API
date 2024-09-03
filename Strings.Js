//Convert a string to uppercase
function getUppercase(){
    let string = "application programming";
    let uppercaseString = string.toUpperCase();

    console.log("Uppercase string:", uppercaseString);
}

getUppercase();

// Extract a substring
function getSubstring(){
    let originalString = "JavaScript is fun";
    let substring = originalString.substring(10, 13);

    console.log("Substring:", substring);

}

getSubstring();


// Check if a string contains a specific word
function getSentence(){
    let sentence = "Application programming";
    let wordToCheck = "programming";
    let containsWord = sentence.includes(wordToCheck);
    if (containsWord) {
  console.log("The sentence contains the word \"programming\".");} 
  else {
  console.log("The sentence does not contain the word \"programming\".");
}

}


getSentence();
