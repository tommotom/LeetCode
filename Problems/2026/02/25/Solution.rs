impl Solution {
    pub fn sort_by_bits(mut arr: Vec<i32>) -> Vec<i32> {
        fn count_bits(mut num: i32) -> i32 {
            let mut ret = 0;
            while num > 0 {
                ret += num % 2;
                num /= 2;
            }
            ret
        }
        arr.sort_by(|&a, &b| {
            let a_count = count_bits(a);
            let b_count = count_bits(b);
            if a_count == b_count {
                return a.cmp(&b);
            }
            a_count.cmp(&b_count)
        });
        arr
    }
}
