impl Solution {
    pub fn mirror_distance(n: i32) -> i32 {
        fn reverse(mut n: i32) -> i32 {
            let mut arr = Vec::new();
            while n > 0 {
                arr.push(n % 10);
                n /= 10;
            }
            let mut ret = 0;
            for num in arr {
                ret *= 10;
                ret += num;
            }
            ret
        }
        (n - reverse(n)).abs()
    }
}
