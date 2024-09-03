//Calculate Area
function Area(){
    let length = 10; 
    let width = 5; 
    let area = length * width;

    console.log("The area of the rectangle is:", area);

}

Area();

//Calculate remainder
function getRemainder(){
    let dividend = 17;
    let divisor = 5;
    let remainder = dividend % divisor;

console.log("The remainder is:", remainder);
}

getRemainder();

//Swapping variables
function swapVariables(){
    let x = 10;
    let y = 20;

    // Swap the values
    x = x + y;
    y = x - y;
    x = x - y;

    console.log(x); 
    console.log(y); 
}