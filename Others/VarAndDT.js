//Declaring variables
function getSomething(){
    let user_name="Collins";
    let age=19;
    let isStudent=true;

    console.log(user_name);
    console.log(age);
    console.log(isStudent);

}

getSomething();

//Converting a String
function add(stringNum){
    let number=stringNum;
    return number+10;
}

let ans=add(42);
console.log(ans);


//Creating a null varriable and an undefined one
function nullVariable(){
    let nullVar = null;
    let undefinedVar;
    
    console.log(nullVar);
    console.log(undefinedVar);
}

nullVariable();

