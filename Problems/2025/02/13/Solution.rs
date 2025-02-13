use std::collections::BinaryHeap;
use std::cmp::Reverse;

impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32 {
        let mut q = BinaryHeap::new();
        for num in nums {
            q.push(Reverse(num as i64));
        }
        let mut ans = 0;
        loop {
            let &Reverse(min) = q.peek().unwrap();
            if min >= k as i64 || q.len() < 2 {
                return ans;
            }
            let Reverse(a) = q.pop().unwrap();
            let Reverse(b) = q.pop().unwrap();
            q.push((Reverse(2 * a.min(b) + a.max(b))));
            ans += 1;
        }
        -1
    }
}
