use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("잘못된 입력");
    let nx: Vec<i32> = input
                    .split_whitespace()
                    .map(|s: &str| s.parse().expect("정수 입력"))
                    .collect();

    let x: i32 = nx[1];
    input.clear();

    io::stdin().read_line(&mut input).expect("잘못된 입력");
    let numbers: Vec<i32> = input
                    .split_whitespace()
                    .map(|s: &str| s.parse().expect("정수 입력"))
                    .collect();

    for i in numbers {
        if i < x {
            print!("{} ", i);
        }        
    }
}