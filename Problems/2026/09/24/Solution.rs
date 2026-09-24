impl Solution {
    pub fn smallest_index(nums: Vec<i32>) -> i32 {
        fn sum(mut num: i32) -> i32 {
            let mut ret = 0;
            while num > 0 {
                ret += num % 10;
                num /= 10;
            }
            ret
        }
        for i in 0..nums.len() {
            if sum(nums[i]) == i as i32 {
                return i as i32;
            }
        }
        -1
    }
}
