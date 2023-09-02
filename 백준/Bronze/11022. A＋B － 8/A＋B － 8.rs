use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("잘못된 입력");
    let test_case: i32 = input.trim().parse().expect("정수 입력");
    input.clear();

    for i in 1..=test_case {
        io::stdin().read_line(&mut input).expect("잘못된 입력");
        let numbers: Vec<i32> = input.split_whitespace().map(|s: &str| s.parse().expect("정수 입력")).collect();
        println!("Case #{}: {} + {} = {}", i, numbers[0], numbers[1], numbers[0] + numbers[1]);
        input.clear();
    }
}