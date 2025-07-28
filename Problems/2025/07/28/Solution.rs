impl Solution {
    pub fn count_max_or_subsets(nums: Vec<i32>) -> i32 {
        let max: i32 = nums.clone().into_iter().reduce(|a, b| a | b).unwrap();
        let mut ans = 0;
        for bit in 1..2_i32.pow(nums.len() as u32) {
            let mut num = 0;
            for i in 0..nums.len() {
                if ((1 << i) & bit) > 0 {
                    num |= nums[i];
                }
            }
            if num == max {
                ans += 1;
            }
        }
        ans
    }
}
