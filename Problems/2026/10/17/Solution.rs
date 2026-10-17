use std::collections::HashMap;

impl Solution {
    pub fn min_swaps(mut nums: Vec<i32>) -> i32 {
        fn digit_sum(mut num: i32) -> i32 {
            let mut ret = 0;
            while num > 0 {
                ret += num % 10;
                num /= 10;
            }
            ret
        }
        let mut sorted: Vec<i32> = nums.clone().into_iter().collect();
        sorted.sort_by(|a, b| if digit_sum(*a) == digit_sum(*b) {a.cmp(&b)} else {digit_sum(*a).cmp(&digit_sum(*b))});

        let mut index = HashMap::new();
        for (i, num) in nums.iter().enumerate() {
            index.insert(*num, i);
        }
        let mut ans = 0;
        for (i, num) in sorted.iter().enumerate() {
            if nums[i] != *num {
                let j = index.get(num).copied().unwrap();
                index.insert(nums[i], j);
                index.insert(*num, i);
                nums[j] = nums[i];
                nums[i] = *num;
                ans += 1;
            }
        }
        ans
    }
}
