impl Solution {
    pub fn construct_transformed_array(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut res = Vec::new();
        for i in 0..n {
            let mut j = nums[i] + i as i32;
            while j < 0 {
                j += n as i32;
            }
            j %= n as i32;
            res.push(nums[j as usize]);
        }
        res
    }
}
