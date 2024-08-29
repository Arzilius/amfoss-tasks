use std::io;

fn print_diamond(n: usize) {
    if n < 1 {
        println!("Number should be greater than 1");
        return;
    }

    let mid = n / 2;

    // Upper part of the diamond
    for i in (1..=n).step_by(2) {
        let spaces = mid - i / 2;
        println!("{}{}", " ".repeat(spaces), "*".repeat(i));
    }

    // Lower part of the diamond
    if n % 2 == 0 {
        for i in (1..n).rev().step_by(2) {
            let spaces = mid - i / 2 + 1;
            println!("{}{}", " ".repeat(spaces - 1), "*".repeat(i));
        }
    } else {
        for i in (1..n-1).rev().step_by(2) {
            let spaces = mid - i / 2;
            println!("{}{}", " ".repeat(spaces), "*".repeat(i));
        }
    }
}

fn main() {
    let mut input = String::new();
    println!("Enter the number of rows for the diamond: ");
    io::stdin().read_line(&mut input).expect("Failed to read input");
    let n: usize = input.trim().parse().expect("Please enter a valid number");

    print_diamond(n);
}

