use std::collections::BinaryHeap;
use std::cmp::Reverse;

impl Solution {
    pub fn is_zero_array(nums: Vec<i32>, mut queries: Vec<Vec<i32>>) -> bool {
        queries.sort_by(|a, b| a[0].cmp(&b[0]));
        let mut q = BinaryHeap::new();
        let mut r = 0;
        for i in 0..nums.len() {
            while r < queries.len() && queries[r][0] <= (i as i32) {
                q.push(Reverse(queries[r][1]));
                r += 1;
            }
            while q.len() > 0 && q.peek().unwrap().0 < (i as i32) {
                q.pop();
            }
            if nums[i] > q.len() as i32 {
                return false;
            }
        }
        true
    }
}
