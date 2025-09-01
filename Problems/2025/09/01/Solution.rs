use std::collections::BinaryHeap;
use std::cmp::Ordering;

struct Class {
    gain: f64,
    pass: i32,
    total: i32,
}

impl PartialEq for Class {
    fn eq(&self, other: &Self) -> bool {
        self.gain == other.gain
    }
}

impl Eq for Class {}

impl PartialOrd for Class {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        self.gain.partial_cmp(&other.gain)
    }
}

impl Ord for Class {
    fn cmp(&self, other: &Self) -> Ordering {
        self.partial_cmp(other).unwrap()
    }
}

impl Solution {
    pub fn max_average_ratio(classes: Vec<Vec<i32>>, extra_students: i32) -> f64 {
        fn gain(pass: i32, total: i32) -> f64 {
            (pass + 1) as f64 / (total + 1) as f64 - pass as f64 / total as f64
        }

        let mut heap = BinaryHeap::new();
        for c in &classes {
            heap.push(Class { gain: gain(c[0], c[1]), pass: c[0], total: c[1] });
        }

        let mut extra = extra_students;
        while extra > 0 {
            let mut top = heap.pop().unwrap();
            top.pass += 1;
            top.total += 1;
            top.gain = gain(top.pass, top.total);
            heap.push(top);
            extra -= 1;
        }

        let mut sum = 0.0;
        while let Some(c) = heap.pop() {
            sum += c.pass as f64 / c.total as f64;
        }

        sum / classes.len() as f64
    }
}
