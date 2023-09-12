use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("입력을 읽을 수 없습니다");

    let input = input.trim();

    let is_palindrome = is_palindrome(input);

    if is_palindrome { println!("1"); }
    else { println!("0"); } 
}

fn is_palindrome(s: &str) -> bool {
    let reversed: String = s.chars().rev().collect();
    s == reversed
}