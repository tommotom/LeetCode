use std::collections::BinaryHeap;

impl Solution {
    pub fn count_non_decreasing_subarrays(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let mut ans: i64 = 0;
        let mut operations: i64 = 0;
        let mut q: BinaryHeap<(i32, usize)> = BinaryHeap::new();
        let mut cnt: Vec<Vec<usize>> = vec![Vec::new(); n];
        let mut pos: Vec<usize> = vec![n; n];
        let mut st: Vec<usize> = Vec::new();

        let mut left = 0usize;
        for right in 0..n {
            while let Some(&top) = st.last() {
                if nums[right] >= nums[top] {
                    pos[top] = right;
                    st.pop();
                } else {
                    break;
                }
            }
            if let Some(&top) = st.last() {
                cnt[top].push(right);
            }
            st.push(right);

            q.push((nums[right], right));
            let max_val = q.peek().unwrap().0;
            operations += std::cmp::max(0, (max_val - nums[right]) as i64);

            while operations > k as i64 {
                for &i in &cnt[left] {
                    let pr = std::cmp::min(pos[i], right + 1);
                    operations -= ((nums[left] - nums[i]) as i64) * ((pr - i) as i64);
                }
                left += 1;
            }

            while let Some(&(_, idx)) = q.peek() {
                if idx < left {
                    q.pop();
                } else {
                    break;
                }
            }

            ans += (right - left + 1) as i64;
        }

        ans
    }
}
