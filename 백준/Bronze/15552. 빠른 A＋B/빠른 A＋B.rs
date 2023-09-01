use std::io::{self, BufRead, Write};

fn main() {
    let stdin = io::stdin();
    let mut reader = stdin.lock();

    let stdout = io::stdout();
    let mut writer = io::BufWriter::new(stdout);

    let mut input_line = String::new();
    reader.read_line(&mut input_line).unwrap();
    let t: i32 = input_line.trim().parse().unwrap();

    for _ in 0..t {
        let mut input_line = String::new();
        reader.read_line(&mut input_line).unwrap();
        let nums: Vec<i32> = input_line
            .split_whitespace()
            .map(|s| s.parse().unwrap())
            .collect();
        
        let a = nums[0];
        let b = nums[1];
        let result = a + b;
        
        writeln!(writer, "{}", result).unwrap();
    }
}
