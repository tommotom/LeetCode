impl Solution {
    pub fn concatenated_binary(n: i32) -> i32 {
        fn to_bin(mut num: i64) -> Vec<i64> {
            let mut ret = Vec::new();
            while num > 0 {
                ret.push(num % 2);
                num /= 2;
            }
            ret.into_iter().rev().collect()
        }

        let n = n as i64;
        let m = 1000000007_i64;
        let mut ans = 0_i64;
        for mut num in 1_i64..=n {
            for b in to_bin(num) {
                ans = (ans * 2 + b) % m;
            }
        }
        ans as i32
    }
}
