use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("입력 실패");
    let mut n: i32 = input.trim().parse().expect("fail to parse");
    let mut cnt: i32 = n;
    let mut gap: i32 = 1;

    while cnt > 1 {
        if cnt % 2 == 1 {
            n = n - gap;
        }
        cnt = (cnt + 1) / 2;
        gap = gap * 2;
    }
    println!("{n}");
}
