use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;

fn part1() -> std::io::Result<i32> {
    let mut out = 0;
    let f = File::open("input.txt")?;
    let reader = BufReader::new(f);
    let lines = reader.lines();
    for line in lines {
        let line = line?;
    }

    Ok(out)
}
fn part2() -> std::io::Result<i32> {
    let mut out = 0;
    let f = File::open("input.txt")?;
    let reader = BufReader::new(f);
    let lines = reader.lines();
    for line in lines {
        let line = line?;
    }

    Ok(out)
}

fn main() {
    let p1_result = part1().unwrap();
    let p2_result = part2().unwrap();
    println!("Part 1: {}\nPart 2: {}", p1_result, p2_result);
}
