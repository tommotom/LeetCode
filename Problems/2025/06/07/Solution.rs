use std::collections::BinaryHeap;
use std::cmp::Ordering;

#[derive(Debug, PartialEq, Eq)]
struct Char {
    c: char,
    i: usize
}

impl Char {
    fn new(c: char, i: usize) -> Self {
        Self {
            c: c,
            i: i
        }
    }
}

impl PartialOrd for Char {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(&other))
    }
}

impl Ord for Char {
    fn cmp(&self, other: &Self) -> Ordering {
        other.c.cmp(&self.c).then(self.i.cmp(&other.i))
    }
}

impl Solution {
    pub fn clear_stars(s: String) -> String {
        let mut s: Vec<char> = s.chars().collect();
        let mut q: BinaryHeap<Char> = BinaryHeap::new();
        for i in 0..s.len() {
            if s[i] == '*' {
                let mut min = q.pop().unwrap();
                s[i] = ' ';
                s[min.i] = ' ';
            } else {
                q.push(Char::new(s[i], i));
            }
        }
        s.iter().filter(|c| **c != ' ').collect()
    }
}
