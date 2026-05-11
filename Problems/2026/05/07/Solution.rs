impl Solution {
    pub fn max_value(nums: Vec<i32>) -> Vec<i32> {
        let mut stack: Vec<(i32, usize, usize)> = Vec::new();
        for i in 0..nums.len() {
            let mut cur = (nums[i], i, i);

            while let Some(top) = stack.last() {
                if top.0 > nums[i] {
                    let top = stack.pop().unwrap();
                    cur.0 = cur.0.max(top.0);
                    cur.1 = top.1;
                } else {
                    break;
                }
            }

            stack.push(cur);
        }

        let mut ans = nums.clone();
        for i in 0..stack.len() {
            for j in stack[i].1..=stack[i].2 {
                ans[j] = stack[i].0;
            }
        }

        ans
    }
}
