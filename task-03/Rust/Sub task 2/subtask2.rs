use std::fs;
use std::io::{self, Write};

fn main() -> io::Result<()> {
    let input_filename = "input.txt";
    let output_filename = "output.txt";

    // Read the content of input.txt
    let content = fs::read_to_string(input_filename)?;
    
    // Write the content to output.txt
    let mut output_file = fs::File::create(output_filename)?;
    output_file.write_all(content.as_bytes())?;

    println!("Content successfully written to {}", output_filename);
    Ok(())
}

