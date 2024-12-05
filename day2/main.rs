use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;

fn isvalid(report: &Vec<i32>) -> bool {
    let mut sorted_report = report.clone();
    sorted_report.sort();
    let mut reversed_report = sorted_report.clone();
    reversed_report.reverse();
    if *report != sorted_report && *report != reversed_report {
        return false;
    }
    for i in 0..report.len() - 1 {
        if !(0 < (report[i] - report[i + 1]).abs() && (report[i] - report[i + 1]).abs() <= 3) {
            return false;
        }
    }
    return true;
}

fn part1() -> std::io::Result<i32> {
    let mut out = 0;
    let f = File::open("input.txt")?;
    let reader = BufReader::new(f);
    let lines = reader.lines();
    for line in lines {
        let line = line?;
        let report = line
            .split_whitespace()
            .map(|x| x.parse::<i32>().unwrap())
            .collect::<Vec<i32>>();
        if isvalid(&report) {
            out += 1;
        }
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
        let report = line
            .split_whitespace()
            .map(|x| x.parse::<i32>().unwrap())
            .collect::<Vec<i32>>();
        if isvalid(&report) {
            out += 1;
        } else {
            for i in 0..report.len() {
                let mut temp = report.clone();
                temp.remove(i);
                if isvalid(&temp) {
                    out += 1;
                    break;
                }
            }
        }
    }

    Ok(out)
}

fn main() {
    let p1_result = part1().unwrap();
    let p2_result = part2().unwrap();
    println!("Part 1: {}\nPart 2: {}", p1_result, p2_result);
}
