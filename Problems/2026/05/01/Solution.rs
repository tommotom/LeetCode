impl Solution {
    pub fn max_rotate_function(nums: Vec<i32>) -> i32 {
        let sum: i32 = nums.iter().sum();
        let n = nums.len();
        let mut f = 0;
        for i in 0..nums.len() {
            f += (i as i32) * nums[i];
        }
        let mut ans = f;
        for i in (0..(nums.len())).rev() {
            f += sum;
            f -= (n as i32) * nums[i];
            ans = ans.max(f);
        }
        ans
    }
}
