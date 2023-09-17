use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("입력을 읽을 수 없음");

    let parts: Vec<&str> = input.trim().split_whitespace().collect();
    let n_str = parts[0];
    let b: u32 = parts[1].parse().expect("정수 입력");

    let chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ".to_string();

    let mut result: u64 = 0;
    let mut base: u64 = 1;

    for char in n_str.chars().rev() {
        if let Some(index) = chars.find(char) {
            result += index as u64 * base;
            base *= b as u64;
        } else { panic!("입력 오류"); }
    }

    println!("{}", result);
}