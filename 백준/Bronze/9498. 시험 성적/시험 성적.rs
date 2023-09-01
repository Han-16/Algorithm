use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("잘못된 입력");
    let score: i32 = input.trim().parse().expect("정수 입력");

    let grade = match score {
        90..=100 => "A",
        80..=89 => "B",
        70..=79 => "C",
        60..=69 => "D",
        _ => "F",
    };

    println!("{}", grade);
}