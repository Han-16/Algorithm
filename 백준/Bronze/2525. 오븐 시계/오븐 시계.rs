use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("잘못된 입력");

    let mut current: Vec<i32> = input
                    .split_whitespace()
                    .map(|s: &str| s.parse().expect("정수 입력"))
                    .collect();

    input.clear();
    io::stdin().read_line(&mut input).expect("잘못된 입력");
    let time: i32 = input.trim().parse().expect("정수 입력");

    current[1] += time;
    current[0] += (current[1]) / 60;
    current[0] = current[0] % 24;
    current[1] = current[1] % 60;
    println!("{} {}", current[0], current[1]);
}