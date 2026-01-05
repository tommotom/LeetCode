use std::collections::HashMap;

impl Solution {
    pub fn sum_four_divisors(nums: Vec<i32>) -> i32 {
        fn factors(mut num: i32) -> HashMap<i32, i32> {
            let mut map = HashMap::new();
            let mut d = 2;
            while num > 1 {
                while num > 1 && num % d == 0 {
                    *map.entry(d).or_insert(0) += 1;
                    num /= d;
                }
                d += 1;
            }
            map
        }

        fn to_sum(num: i32) -> i32 {
            let map = factors(num);
            if map.len() == 1 {
                for (&k, &v) in &map {
                    return if v == 3 {1 + num + k + k * k} else {0};
                }
            }
            if map.len() == 2 {
                let mut ret = 1 + num;
                for (&k, &v) in &map {
                    if v > 1 {
                        return 0;
                    }
                    ret += k;
                }
                return ret;
            }
            0
        }

        nums.iter().map(|&num| to_sum(num)).sum()
    }
}
