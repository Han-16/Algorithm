use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("입력 실패");

    let n: u64 = match input.trim().parse() {
        Ok(num) => num,
        Err(_) => {
            println!("유효한 숫자를 입력하세요");
            return;
        }
    };

    for i in 1..=9 {
        println!("{} * {} = {}", n, i, n * i);
    }
}