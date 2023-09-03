use std::io;

fn main() {
    let black = vec![1, 1, 2, 2, 2, 8];
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("잘못된 입력");
    let white: Vec<i32> = input
                    .split_whitespace()
                    .map(|s: &str| s.parse().expect("정수 입력"))
                    .collect();

    let len = white.len();

    for i in 0..len {
        print!("{} ", black[i] - white[i]);
    }
}