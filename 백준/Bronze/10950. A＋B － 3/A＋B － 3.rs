use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read input");
    let count: i32 = input.trim().parse().expect("Invalid input");

    for _ in 0..count {
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Failed to read input");
        let values: Vec<i32> = input
            .split_whitespace()
            .map(|s| s.parse().expect("Invalid input"))
            .collect();

        let a = values[0];
        let b = values[1];
        println!("{}", a + b);
    }
}
