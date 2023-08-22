use std::io;

fn main() {
    let mut input = String::new();

    io::stdin().read_line(&mut input)
        .expect("Falied to read line");

    let numbers: Vec<&str> = input.split_whitespace().collect();

    let a: i32 = match numbers[0].parse() {
        Ok(i) => i,
        Err(_e) => {
            -1
        }
    };
    
    let b: i32 = match numbers[1].parse() {
        Ok(i) => i,
        Err(_e) => {
            -1
        }
    };

    println!("{}", a + b);
}