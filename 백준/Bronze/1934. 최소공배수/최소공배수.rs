use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("입력 읽기 실패");
    let cnt: i32 = input.trim().parse().expect("파싱 실패");

    for _ in 0..cnt {
        input.clear();
        io::stdin().read_line(&mut input).expect("입력 읽기 실패");
        let numbers: Vec<u64> = input
                            .trim()
                            .split_whitespace()
                            .map(|s: &str| s.parse().expect("파싱 실패"))
                            .collect();
        let answer: u64 = lcm(numbers[0], numbers[1]);
        println!("{answer}");
    }
}

fn gcd(a: u64, b: u64) -> u64 {
    if b == 0 { a }
    else { gcd(b, a % b) }   
}

fn lcm(a: u64, b: u64) -> u64 {
    (a * b) / gcd(a, b)
}