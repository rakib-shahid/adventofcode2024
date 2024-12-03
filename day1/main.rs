use std::collections::HashMap;
use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;

fn part1() -> std::io::Result<i32> {
    let f = File::open("input.txt")?;
    let mut left: Vec<i32> = Vec::new();
    let mut right: Vec<i32> = Vec::new();
    let reader = BufReader::new(f);
    for line in reader.lines() {
        let line = line?;
        let mut nums = line.split_whitespace();
        let num1: i32 = nums.next().unwrap().parse().unwrap();
        left.push(num1);
        let num2: i32 = nums.next().unwrap().parse().unwrap();
        right.push(num2);
    }
    left.sort();
    right.sort();
    let mut out = 0;
    for i in 0..left.len() {
        out += (left[i] - right[i]).abs();
    }
    Ok(out)
}

fn part2() -> std::io::Result<i32> {
    let f = File::open("input.txt")?;
    let reader = BufReader::new(f);
    let mut left: Vec<i32> = Vec::new();
    let mut frequency: HashMap<i32, i32> = HashMap::new();
    for line in reader.lines() {
        let line = line?;
        let mut temp = line.split_whitespace().map(|x| x.parse::<i32>().unwrap());
        let lnum = temp.next().unwrap();
        let rnum = temp.next().unwrap();
        left.push(lnum);
        *frequency.entry(rnum).or_insert(0) += 1;
    }
    let mut out = 0;
    for val in left {
        out += val
            * match frequency.get(&val) {
                Some(val) => val,
                None => &0,
            };
    }
    Ok(out)
}

fn main() {
    let part1_result = part1().unwrap();
    let part2_result = part2().unwrap();
    println!("Part 1: {}\nPart 2: {}", part1_result, part2_result);
}
