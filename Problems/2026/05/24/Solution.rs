use std::cmp::Ordering;
use std::collections::BinaryHeap;

#[derive(Copy, Clone, Eq, PartialEq)]
struct State {
    height: i32,
    i: usize,
}

impl Ord for State {
    fn cmp(&self, other: &Self) -> Ordering {
        other.height.cmp(&self.height)
    }
}

impl PartialOrd for State {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Solution {
    pub fn max_jumps(arr: Vec<i32>, d: i32) -> i32 {
        let d = d as usize;
        let mut q = BinaryHeap::new();
        for i in 0..arr.len() {
            q.push(State { height: arr[i], i });
        }
        let mut jump = vec![1; arr.len()];
        while let Some(cur) = q.pop() {
            let i = cur.i;
            let (mut l_max, mut r_max) = (0, 0);

            for x in 1..=d {
                let r = i + x;
                if r < arr.len() {
                    if arr[i] < arr[r] && r_max < arr[r] {
                        jump[r] = jump[r].max(jump[i] + 1);
                    }
                    r_max = r_max.max(arr[r]);
                }
                let l = i - x;
                if i >= x {
                    if arr[i] < arr[l] && l_max < arr[l] {
                        jump[l] = jump[l].max(jump[i] + 1);
                    }
                    l_max = l_max.max(arr[l]);
                }
            }
        }
        *jump.iter().max().unwrap()
    }
}
