use std::collections::HashMap;

impl Solution {
    pub fn min_mirror_pair_distance(nums: Vec<i32>) -> i32 {
        fn reverse(mut num: i32) -> i32 {
            let mut arr = Vec::new();
            let mut l = 0;
            while num > 0 {
                arr.push(num % 10);
                num /= 10;
                l += 1;
            }
            let mut ret = 0;
            for i in 0..l {
                ret *= 10;
                ret += arr[i];
            }
            ret
        }

        let mut seen_at = HashMap::new();
        let mut ans = i32::MAX;
        for j in 0..nums.len() {
            if seen_at.contains_key(&nums[j]) {
                let i = seen_at.get(&nums[j]).unwrap();
                ans = ans.min((j - i) as i32);
            }
            seen_at.insert(reverse(nums[j]), j);
        }
        if ans == i32::MAX {-1} else {ans}
    }
}
