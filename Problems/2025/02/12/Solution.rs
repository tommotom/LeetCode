use std::collections::HashMap;

impl Solution {
    pub fn maximum_sum(nums: Vec<i32>) -> i32 {
        let mut maxs = HashMap::new();
        let mut ans = -1;
        for num in nums {
            let sum = Self::sum_of_digits(num);
            if let Some(v) = maxs.get(&sum) {
                ans = ans.max(v + num);
                maxs.insert(sum, num.max(*v));
            } else {
                maxs.insert(sum, num);
            }
        }
        ans
    }

    fn sum_of_digits(mut num: i32) -> i32 {
        let mut ret = 0;
        while num > 0 {
            ret += num % 10;
            num /= 10;
        }
        ret
    }
}
