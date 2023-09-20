use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("입력을 읽을 수 없음");

    let length: Vec<f32> = input
                        .trim()
                        .split_whitespace()
                        .map(|s: &str| s.parse().expect("정수를 입력하세요"))
                        .collect();
    let answer: f32 = length[0] * length[1] * 0.5;
    println!("{:.1}", answer);
}