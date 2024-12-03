use std::fs::File;
use std::io::BufReader;
use std::io::prelude::*;

fn part1() -> std::io::Result<()> {
    let f = File::open("input.txt")?;
    let reader = BufReader::new(f);
    for line in reader.lines() {
        let line = line?;
        let mut nums = line.split_whitespace();
        let num1: i32 = nums.next().unwrap().parse().unwrap();
        let num2: i32 = nums.next().unwrap().parse().unwrap();
        println!("{} {}", num1, num2);
    }

    Ok(())

}


fn main() {
    let _ = part1();
}