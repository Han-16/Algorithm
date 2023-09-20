use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("입력을 읽을 수 없음");
    input.clear();

    io::stdin().read_line(&mut input).expect("입력을 읽을 수 없음");
    let solve: Vec<i32> = input
                    .trim()
                    .split_whitespace()
                    .map(|s: &str| s.parse().expect("정수를 입력하세요"))
                    .collect();

    let mut max_length: i32 = 0;
    let mut answer: i32 = 0;

    for i in solve {
        if i == 0 {
            if answer > max_length {
                max_length = answer;
            }
            answer = 0;
        }
        else {
            answer += 1;
        }
    }
    if answer > max_length {
        max_length = answer;
    }

    println!("{}", max_length);
}