use std::fs::File;
use std::io::{self, BufRead, Write};

fn print_diamond(n: usize) -> String {
    if n < 1 {
        return "Number should be greater than 1\n".to_string();
    }

    let mut result = String::new();
    let mid = n / 2;

    // Upper part of the diamond
    for i in (1..=n).step_by(2) {
        let spaces = mid - i / 2;
        result.push_str(&" ".repeat(spaces));
        result.push_str(&"*".repeat(i));
        result.push('\n');
    }

    // Lower part of the diamond
    if n % 2 == 0 {
        for i in (1..n).rev().step_by(2) {
            let spaces = mid - i / 2 + 1;
            result.push_str(&" ".repeat(spaces - 1));
            result.push_str(&"*".repeat(i));
            result.push('\n');
        }
    } else {
        for i in (1..n - 1).rev().step_by(2) {
            let spaces = mid - i / 2;
            result.push_str(&" ".repeat(spaces));
            result.push_str(&"*".repeat(i));
            result.push('\n');
        }
    }

    result
}

fn main() -> io::Result<()> {
    let input_file = File::open("input.txt")?;
    let reader = io::BufReader::new(input_file);
    let n: usize = reader.lines().next().unwrap()?.trim().parse().unwrap();

    let diamond = print_diamond(n);

    let mut output_file = File::create("output.txt")?;
    output_file.write_all(diamond.as_bytes())?;

    println!("File transfer was successful");
    Ok(())
}

