// While Loops 
function getWhileLoops(){
    let number = 1;

    while (number <= 20) {
    console.log(number);
    number++;
}

}
getWhileLoops();

// For loops
function getForLoops(){
    for (let i = 1; i <= 10; i++) {
        let multiple = 3 * i;
        console.log("The Result is:", multiple);
}

}

getForLoops();

// Iteration
function getIteration(){
    let names = ["Alice", "Bob", "Charlie", "David"];

    for (let i = 0; i < names.length; i++) {
        let name = names[i];
        console.log("Hello, " + name + "!");
}

}

getIteration();
