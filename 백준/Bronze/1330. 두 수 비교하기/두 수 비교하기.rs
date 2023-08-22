use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input)
        .expect("입력오류");

    let numbers: Vec<&str> = input.split_whitespace().collect();

    let a: i32 = match numbers[0].parse() {
        Ok(parsed_num) => parsed_num,
        Err(_) => {
            println!("잘못된 입력");
            return;
        }
    };

    let b: i32 = match numbers[1].parse() {
        Ok(parsed_num) => parsed_num,
        Err(_) => {
            println!("잘못된 입력");
            return;
        }
    };

    if a > b { println!(">"); }
    else if a < b { println!("<"); }
    else { println!("=="); }
    
}