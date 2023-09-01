use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("입력을 읽을 수 없습니다.");
    input.clear();    

    io::stdin().read_line(&mut input).expect("입력을 읽을 수 없습니다.");
    let numbers: Vec<i32> = input
                        .split_whitespace()
                        .map(|s: &str| s.parse().expect("정수 입력하세요."))
                        .collect();
    input.clear();

    io::stdin().read_line(&mut input).expect("입력을 읽을 수 없습니다.");
    let value: i32 = input.trim().parse().expect("정수 입력하세요.");

    let mut count: i32 = 0;

    for &n in &numbers {
        if n == value { count += 1; }
    }

    println!("{}", count);
}