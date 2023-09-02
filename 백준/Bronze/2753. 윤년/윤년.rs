use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("잘못된 입력");
    let year: i32 = input.trim().parse().expect("정수 입력");
    
    if year % 400 == 0 || (year % 4 == 0 && year % 100 != 0) {
        println!("1");
    } else { println!("0"); }
}