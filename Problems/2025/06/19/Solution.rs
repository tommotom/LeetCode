impl Solution {
    pub fn partition_array(mut nums: Vec<i32>, k: i32) -> i32 {
        nums.sort();
        let mut partition = 1;
        let mut min = nums[0];
        for i in 1..nums.len() {
            if nums[i] - min > k {
                partition += 1;
                min = nums[i];
            }
        }
        partition
    }
}
