impl Solution {
    pub fn min_element(nums: Vec<i32>) -> i32 {
        fn digit_sum(mut num: i32) -> i32 {
            let mut ret = 0;
            while num > 0 {
                ret += num % 10;
                num /= 10;
            }
            ret
        }

        nums.iter().map(|&num| digit_sum(num)).min().unwrap()
    }
}
