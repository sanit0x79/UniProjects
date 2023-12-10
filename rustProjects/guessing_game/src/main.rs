use std::io; // loads the input output library "standard (std)"
use rand::Rng;
use std::cmp::Ordering;

fn main(){ // main function
    println!("Guess the number"); // printing string to the screen, println! if not calling for function, else use println

    let secret_number = rand::thread_rng().gen_range(1..=100);

    println!("The secret number is {secret_number}");

    println!("Please input your guess");

    let mut guess = String::new(); // create variable to store user input. The :: indicates that new is a function associated with the String type (associated function)
    // let apples = 5, creates a variable named apples with a value of 5
    // mut means that the variable is mutable, which means it's value can be changed, a variable is imutable by standard
    // let mut guess = String::new(); creates a mutable variable with a currently bound empty instance of a string
    io::stdin()
        .read_line(&mut guess) // reads the input and assigns it to mutable variable "guess", & indicates that this argument is a reference, references are imutable by standard
        .expect("Failed to read line!"); // rust has an expect method. If this instance of result is an 'Err' (error) value, expect will cause the program to crash and display the message

    println!("You guessed: {guess}");

}