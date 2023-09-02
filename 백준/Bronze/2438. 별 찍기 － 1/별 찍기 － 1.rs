use std::{io, i32};

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("잘못된 입력");
    let cnt: i32 = input.trim().parse().expect("정수 입력");

    for i in 1..=cnt {
        for _ in 0..i {
            print!("*");
        }
        println!();
    }
}