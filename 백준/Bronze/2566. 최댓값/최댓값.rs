use std::io;

fn main() {
    let mut input = String::new();
    let mut matrix: Vec<Vec<i32>> = Vec::new();
    let mut loc = (0, 0);
    let mut max: i32 = -1;

    for _ in 0..9 {
        io::stdin().read_line(&mut input).expect("입력 실패");
        let rows: Vec<i32> = input.split_whitespace().map(|s: &str| s.parse().expect("정수 입력")).collect();
        matrix.push(rows);
        input.clear();
    }

    for i in 0..9 {
        for j in 0..9 {
            if matrix[i][j] > max {
                max = matrix[i][j];
                loc.0 = i + 1;
                loc.1 = j + 1;
            }
        }
    }

    println!("{}", max);
    println!("{} {}", loc.0, loc.1);
}