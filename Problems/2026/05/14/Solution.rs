impl Solution {
    pub fn is_good(mut nums: Vec<i32>) -> bool {
        nums.sort();
        let n = nums.len();
        if n == 1 {
            return false;
        }
        for i in 0..n-1 {
            if nums[i] != (i+1) as i32 {
                return false;
            }
        }
        nums[n-2] == nums[n-1]
    }
}
