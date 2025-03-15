impl Solution {
    pub fn maximum_candies(candies: Vec<i32>, k: i64) -> i32 {
        fn isValid(candies: &Vec<i32>, num: i32, k: i64) -> bool {
            let mut children = 0;
            for candy in candies {
                children += (candy / num) as i64;
            }
            children >= k
        }

        let mut l = 1;
        let mut r = *candies.iter().max().unwrap() + 1;
        while l < r {
            let m = l + (r - l) / 2;
            if isValid(&candies, m, k) {
                l = m + 1;
            } else {
                r = m;
            }
        }
        l - 1
    }
}
