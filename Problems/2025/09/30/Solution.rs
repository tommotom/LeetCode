impl Solution {
    pub fn triangular_sum(nums: Vec<i32>) -> i32 {
        if nums.len() == 1 {
            return nums[0];
        }
        let mut arr = Vec::new();
        for i in 1..nums.len() {
            arr.push((nums[i] + nums[i-1]) % 10);
        }
        Self::triangular_sum(arr)
    }
}
