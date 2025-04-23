use std::collections::HashMap;

impl Solution {
    pub fn count_largest_group(n: i32) -> i32 {
        fn count(mut num: i32) -> i32 {
            let mut ret = 0;
            while num > 0 {
                ret += num % 10;
                num /= 10;
            }
            ret
        }
        let mut counter = HashMap::new();
        for num in 1..=n {
            *counter.entry(count(num)).or_insert(0) += 1;
        }
        let max = counter.values().reduce(|a, b| a.max(b)).unwrap();
        counter.values().filter(|v| v == &max).count() as i32
    }
}
