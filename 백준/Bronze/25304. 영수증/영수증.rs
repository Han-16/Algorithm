use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("잘못된 입력");
    let mut total_price: i32 = input.trim().parse().expect("정수입력");
    input.clear();

    io::stdin().read_line(&mut input).expect("잘못된 입력");
    let total_count: i32 = input.trim().parse().expect("정수입력");
    input.clear();

    for _ in 0..total_count {
        io::stdin().read_line(&mut input).expect("Invalid Input");
        let price: Vec<i32> = input
                .split_whitespace()
                .map(|s: &str| s.parse().expect("정수입력"))
                .collect();
        let price = price[0] * price[1];
        total_price -= price;
        input.clear();
    } 
    if total_price == 0 {
        println!("Yes");
    }  else { println!("No"); }
}