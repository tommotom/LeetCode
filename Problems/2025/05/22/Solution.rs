use std::collections::BinaryHeap;
use std::cmp::Reverse;

impl Solution {
    pub fn max_removal(n: Vec<i32>, mut q: Vec<Vec<i32>>) -> i32 {
        let (mut h, mut d) = (BinaryHeap::new(), vec![0; n.len() + 1]);
        q.sort_unstable();
        let (mut lvl, mut j) = (0, 0);
        for i in 0..n.len() {
            while j < q.len() && q[j][0] == i as i32 {
                h.push(q[j][1] as usize);
                j += 1;
            }
            lvl += d[i];
            while n[i] > lvl && h.len() > 0 && *h.peek().unwrap() >= i {
                d[h.pop().unwrap() + 1] -= 1;
                lvl += 1;
            }
            if n[i] > lvl { return -1 }
        }
        h.len() as _
    }
}
